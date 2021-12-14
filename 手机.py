'''
    诺基亚：
        打电话：对方号码，来电铃声，归属地

        打电话：对方号码，来电铃声，归属地，提示信息，大头贴，录音
'''
# import time
# class  OldPhone:
#     phoneNumber = ""
#     voice = ""
#     address = ""
#
#     def call(self,number):
#         print(self.phoneNumber,"正在给",number,"打电话。本机归属地:",self.address,"。")
#         print("正在响铃：",self.voice)
#         for i in range(8):
#             print(".",end="")
#             time.sleep(1)
#         print("对方已接通!")
#
#
# class NewPhone(OldPhone):
#     information = ""
#     picture = ""
#     mic = False
#
#     def call(self,number):
#         # 老功能老代码执行
#         super().call(number)
#
#         # 新功能自己来做
#         self.mic = True
#         print("已经开启了录音功能！设置对方大头贴为：",self.picture,"【对方是：",self.information,"】")
#
#
# phone = NewPhone()
# phone.phoneNumber = "13552648187"
# phone.voice = "江南style"
# phone.picture = "野猪佩奇"
# phone.information = "快递诈骗"
# phone.address  = "北京移动"
#
# phone.call("15556897458")


'''
i.	人：年龄，性别，姓名。

ii.	现在有个工种，工人：年龄，性别，姓名 。行为：干活。请用继承的角度来实现该类。

iii.	现在有学生这个工种，学生：年龄，性别，姓名，学号。行为：学习，唱歌。请结合上面的几个题目用继承的角度来实现。
'''
# class person:
#     age=0
#     sex=''
#     name=''
#     def capacity(self):
#         print(self.name,self.age,'岁',self.sex)
#
# class newperson(person):
#     work=''
#     def study(self):
#         super().capacity()
#         print('工作是',self.work)
# class nnewperson(newperson):
#     nwork=''
#     sang=''
#     def nstydy(self):
#         super().study()
#         print(self.nwork,"唱的歌为",self.sang)
#
# nn=nnewperson()
# nn.name='小明'
# nn.nwork='学生'
# nn.sang='月亮之上'
# nn.age=20
# nn.nstydy()

class chu:
    __name=''
    __age=0
    __work=''
    def setname(self,name):
        if name=='':
            print('输入错误')
        else:
            self.__name=name
    def getname(self):
        return self.__name
    def setage(self,age):
        if self.__age=='':
            print('输入错误')
        else:
            self.__age=age
    def getage(self):
        return self.__age
    def setwork(self,work):
        if work=='':
            print('输入错误')
        else:
            self.__work=work
    def getwork(self):
        return self.__work

class chuzi(chu):
    def study(self):
        print(self.getage(),'岁的',self.getname(),'正在',self.getwork())

class chuzii(chuzi):
    nwork = ''
    def nstudy(self):
        super().study()
        print('还在', self.nwork)
x=chuzii()
x.setname('小明')
x.setage(20)
x.setwork('炒菜')
x.nwork='蒸饭'
x.nstudy()