"""
演示面向对象: 继承的基础语法
"""

# 演示单继承
class Phone:
    IMEI = None     # 序列号
    producer = "ITCAST" # 厂商

    def call_by_4g(self):
        print("4g通话")


class Phone2022(Phone):

    face_id = "10001" #面部识别id

    def call_by_5g(self):
        print("2022年新功能:5g通话")

phone =  Phone2022()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()

# 演示多继承
class NFCReader:
    nfc_type = "第五代"
    producer = "HM"

    def read_card(self):
        print("NFC读卡")

    def write_card(self):
        print("NFC写卡")

class RemoteControl:
    rc_type = "红外遥控"

    def control(self):
        print("红外遥控开启了")


class MyPhone(Phone,NFCReader,RemoteControl):
    pass #补充语法，不产生语法错误


new_phone = MyPhone()
new_phone.call_by_4g()
new_phone.read_card()
new_phone.write_card()
new_phone.control()

# 演示多继承下, 父类成员名一致的场景
print(new_phone.producer)  #此时会按照从左到右为优先级，即先继承的保留

#复写父类成员变量和成员方法
class New_Phone(Phone):

    producer = "HuaWei"

    def call_by_4g(self):
        print("开启CPU单核模式,确保通话的时候省电")

        #方式一
        print("使用4g网络进行通话")
        print(f"父类的厂商是：{Phone.producer}")
        Phone.call_by_4g(self)
        
        print("关闭CPU单核模式,确保性能")

phone = New_Phone()
phone.call_by_4g()
print(phone.producer)

# 在子类中，调用父类成员
