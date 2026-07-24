import streamlit as st
import os
from openai import OpenAI
from datetime import datetime
import json

# 页面配置必须是第一个 Streamlit 命令
st.set_page_config(
    page_title="AI智能伙伴",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

# ========== 工具函数（必须在调用之前定义）==========

def generate_session_name():
    return datetime.now().strftime("%Y-%m-%d %H-%M-%S")


def delete_session(session_name):
    try:
        if os.path.exists(f"sessions/{session_name}.json"):
            os.remove(f"sessions/{session_name}.json")
            if session_name == st.session_state.current_session:
                st.session_state.messages = []
                st.session_state.current_session = generate_session_name()
    except Exception as e:
        st.error("删除会话失败！")


def load_sessions():
    session_list = []
    if os.path.exists("sessions"):
        file_list = os.listdir("sessions")
        for filename in file_list:
            if filename.endswith(".json"):
                session_list.append(filename[:-5])
    return session_list


def load_session(session_name):
    try:
        if os.path.exists(f"sessions/{session_name}.json"):
            with open(f"sessions/{session_name}.json", "r", encoding="utf-8") as f:
                session_data = json.load(f)
                st.session_state.messages = session_data["messages"]
                st.session_state.nick_name = session_data["nick_name"]
                st.session_state.nature = session_data["nature"]
                st.session_state.current_session = session_name
    except Exception as e:
        st.error("加载会话失败！")


def save_session():
    if st.session_state.current_session:
        session_data = {
            "nick_name": st.session_state.nick_name,
            "nature": st.session_state.nature,
            "current_session": st.session_state.current_session,
            "messages": st.session_state.messages
        }
        if not os.path.exists("sessions"):
            os.mkdir("sessions")
        with open(f"sessions/{st.session_state.current_session}.json", "w", encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=2)


# ========== 会话状态初始化 ==========
if "messages" not in st.session_state:
    st.session_state.messages = []

if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小美"

if "nature" not in st.session_state:
    st.session_state.nature = "活泼开朗的江南姑娘"

if "current_session" not in st.session_state:
    st.session_state.current_session = generate_session_name()


# ========== 系统提示词 ==========
system_prompt = """
你叫%s,现在是用户的真实伴侣,请完全代入伴侣角色.:
规则：
1. 每次只回1条消息
2. 匹配用户的语言
3. 回复简短，像微信聊天一样
4. 有需要的话可以用❤️🌸等emoji表情
5. 用符合伴侣性格的方式对话
6. 回复的内容，要充分体现伴侣的性格特征

伴侣性格：
- %s

你必须严格遵守上述规则来回复用户。
"""


# ========== 创建 AI 客户端 ==========
client = OpenAI(api_key=os.environ.get("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com")


# ========== 主界面 ==========
st.title("AI智能伙伴")

st.text(f"会话名称: {st.session_state.current_session}")

for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    else:
        st.chat_message("assistant").write(message["content"])


# ========== 侧边栏 ==========
with st.sidebar:
    st.subheader("AI控制面板")

    if st.button("新建会话", width="stretch", icon="🖊️"):
        save_session()
        if st.session_state.messages:
            st.session_state.messages = []
            st.session_state.current_session = generate_session_name()
            save_session()
            st.rerun()

    st.text("会话历史")
    session_list = load_sessions()
    for session in session_list:
        col1, col2 = st.columns([4, 1])

        with col1:
            if st.button(
                session,
                width="stretch",
                icon="📝",
                key=f"load_{session}",
                type="primary" if session == st.session_state.current_session else "secondary"
            ):
                load_session(session)
                st.rerun()

        with col2:
            if st.button("", width="stretch", icon="❌️", key=f"delete_{session}"):
                delete_session(session)
                st.rerun()

    st.subheader("伴侣信息")
    nick_name = st.text_input("昵称", value=st.session_state.nick_name, placeholder="请输入昵称")
    if nick_name:
        st.session_state.nick_name = nick_name

    nature = st.text_area("性格", value=st.session_state.nature, placeholder="请输入性格")
    if nature:
        st.session_state.nature = nature


# ========== 消息输入与 AI 回复 ==========
prompt = st.chat_input("请输入您要问的问题")

if prompt:
    st.chat_message("user").write(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": system_prompt % (st.session_state.nick_name, st.session_state.nature)},
            *st.session_state.messages
        ],
        stream=True
    )

    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        full_response = ""
        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                full_response += chunk.choices[0].delta.content
                response_placeholder.write(full_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})
    save_session()
