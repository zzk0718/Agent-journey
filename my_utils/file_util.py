def print_file_info(file_name):
    f = None
    try:
        f = open(file_name, "r", encoding="utf-8")
        content = f.read()
        print("文件内容：\n", content)
    except FileNotFoundError:
        print("文件出现异常")
    except Exception as e:
        print(f"读取文件出错：{e}")
    finally:
        # 明确判断是否不为None
        if f is not None:
            f.close()

def append_to_file(file_name, data):
    """追加写入文件"""
    with open(file_name, "a", encoding="utf-8") as f:
        f.write(data)