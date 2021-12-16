'''
    进程：
        正在进行的程序
    线程：
        1.Thread类：多线程类
        2.子类继承Thread类。资格执行多线程
        3.重写run方法，写任务代码
        4.启动线程。
'''
# from threading import  Thread
#
#
# class PCmanager(Thread):
#
#     def run(self):
#         for i in range(1000000):
#             print("嘻嘻！，电脑管家成功杀了",i,"个毒！")
#
# class PC360(Thread):
#
#     def run(self):
#         for i in range(1000000):
#             print("嘻嘻！，360管家成功杀了",i,"个毒！")
#
# pc = PCmanager()
# pc1 = PC360()
#
# pc.start()
# pc1.start()
# '''
#     多线程 + 接口技术：
#     抢票：
#         有500张票，刘备，张飞，关二爷三个同时抢票，谁抢算谁的，看谁抢的多。
#
# '''

from threading import Thread

import  time



count=0#蛋挞数量
lock=3
class time_(Thread):

    def run(self) -> None:
        global lock
        time.sleep(20)
        lock=0






class cook(Thread):#做蛋挞
    cookname = ''
    con =0
    def run(self) -> None:
        global count
        global lock

        while True:

            if lock!=0 and count<500:
                count+=1
                self.con +=1

            elif count==500:
                time.sleep(3)
            elif lock==0:
                print(self.cookname, '已经做了', self.con, '个蛋挞','挣了',self.con*1.5)
                break
eggmoney=3#蛋挞单价
cob=0

class client(Thread):
    clientname=''
    countbuy = 0  # 购买数量
    money = 5000  # 余额
    def run(self) -> None:
        global count
        global money
        global eggmoney
        global lock
        global cob
        while True:

            if lock!=0 and count>0 and self.money>eggmoney:
                # if self.money>eggmoney:
                    self.countbuy+=1
                    cob +=1
                    count-=1
                    self.money-=eggmoney
                # else:
                #     print('余额不足')
            elif lock==0:
                print("客户买了", self.countbuy, '个蛋挞', '剩下', self.money, '余额')
                break

# consumergoods=0#消费总金额
# class cashier(Thread):
#     cookwage = 0  # 厨师工资
#     def run(self) -> None:#工资
#         global countbuy
#         global cookwage
#         self.cookwage = countbuy * 1.5
#         print('厨师工资为',self.cookwage)
#         consumergoods=countbuy*3
#         print('消费总金额为',consumergoods)




t1=time_()
t1.start()
c1=cook()
c2=cook()
c3=cook()
c1.cookname='张三'
c2.cookname='张四'
c3.cookname='张五'
c1.start()
c2.start()
c3.start()
cl1=client()
cl2=client()
cl3=client()
cl4=client()
cl5=client()
cl6=client()
cl1.clientname='李三'
cl2.clientname='李四'
cl3.clientname='李五'
cl4.clientname='李六'
cl5.clientname='李七'
cl6.clientname='李八'
cl1.start()
cl2.start()
cl3.start()
cl4.start()
cl5.start()
cl6.start()














