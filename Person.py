'''
    人：
        属性：姓名，性别，年龄，身高
        行为：吃，学习，打游戏，睡觉
    1.封装
        1.1 先将属性隐藏
            __属性
        1.2 提供set/Get用于间接赋值和间接取值
'''
import time
# class Person:
#     __username = ""
#     __sex = ""
#     __age = 0
#     __high = 0.0
#
#
#     def setHigh(self,high):
#         if high > 2.72  or high  < 0:
#             print("身高非法！ 别瞎弄！")
#         else:
#             self.__high = high
#
#     def getHigh(self):
#         return self.__high
#
#     def setSex(self,sex):
#         if sex != "男" and sex != "女":
#             print("你是泰国来的吗？")
#         else:
#             self.__sex = sex
#
#     def getSex(self):
#         return self.__sex
#
#
#
#     def setAge(self,age):
#         if age > 120  or age < 0:
#             print("年龄非法，禁止输入！")
#         else:
#             self.__age  = age
#
#     def getAge(self):
#         return  self.__age
#
#     def setUsername(self,username):
#         if username == "":
#             print("姓名不能为空！别瞎弄！")
#             return 1
#         else:
#             self.__username = username
#
#     def getUsername(self):
#         return self.__username
#
#
#
#     def eat(self,eatName):
#         print(self.__username ,"正在吃",eatName)
#
#     def learn(self,subject,hour):
#         print(self.__username,"正在学习",subject,",已经学了",hour,"小时！")
#
#     def playGame(self,gameName,hour):
#         print(self.__username,"正在玩【",gameName,"】")
#         for i in range(2):
#             print(".",end="")
#             time.sleep(1)
#         print("[timi-光子工作室]")
#         print("游戏已经玩了",hour,"小时！")
#
#     def sleep(self,hour):
#         print(self.__username,"正在睡觉，已经睡了",hour,"小时！")
#
#     def showMe(self):
#         print("我叫",self.__username,"，今年",self.__age,",身高",self.__high,"，我是",self.__sex,"性")
#
# p = Person()
#
# # p.username = "刘备"
# loop=1
# while loop==1:
#     loop=p.setUsername(input('输入name'))
#     print(loop)
#
# p.age = -56
# p.setAge(-56)
# # p.high = 1.76
# p.setHigh(1.76)
# # p.sex = "男"
# p.setSex("男")

#
# p.eat("小汉堡")
# p.learn("匡扶汉室",2)
# p.playGame("三国志",10)
# p.sleep(10)
#
# p.showMe()

# high=p.getHigh()
# print(high)
# class cup:
#     __colour=''#颜色
#     __volume=0#容积
#     __textture=''#材质
#     __high=0#高度
#
#     def setcolour(self,colour):
#         if colour=='':
#             print("输入正确的颜色")
#         else:
#             self.__colour = colour
#     def getcolour(self):
#         return self.__colour
#     def setvolume(self,volume):
#         if volume=='':
#             print("请输入正确的容积")
#         else:
#             self.__volume=volume
#     def getvolume(self):
#         return self.__volume
#     def settexture(self,textture):
#         if textture=='':
#             print("请输入正确的材质")
#         else:
#             self.__textture=textture
#     def gettextture(self):
#         return self.__textture
#     def sethigh(self,high):
#         if high>30 or high<0:
#             print("输入正确的高度")
#         else:
#             self.__high=high
#     def gethigh(self,high):
#         return self.__high
#     def show(self):
#         print("杯子的颜色为：",self.__colour,'容积为：',self.__volume,'材质为：',self.__textture,'杯子的高度为：',self.__high)
#
# c=cup()
# c.setcolour('蓝色')
# c.setvolume(1000)
# c.settexture('不锈钢')
# c.sethigh(20)
# c.show()



class airconditioner:
    __brand=''#品牌
    __money=0
    def setbrand(self,brand):
        if brand=='':
            print("输入错误")
        else:
            self.__brand=brand
    def getbrand(self):
        return self.__brand
    def setmoney(self,money):
        if money<0 or money=='':
            print("输入错误")
        else:
            self.__money=money
    def getmoney(self):
        return self.__money
    def action(self):
        for i in range(3):
            print(".",end="")
            time.sleep(2)
        print('您的空调开机了')
    def shutdown(self):
        print('您的空调即将关机')

        for j in range(10,0,-1):
            print(j)
            time.sleep(1)
        print("您的空调已经关机")
    def show(self):
        print('您的空调品牌为：',self.__brand,'你的空调价格为：',self.__money)
a=airconditioner()
a.setbrand('格力')
a.setmoney(int(input("请输入您的价格")))
a.action()
a.show()
a.shutdown()
















