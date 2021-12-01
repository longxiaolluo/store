# i=1 #循环
# a=0 #和
# j=0#最大数
# while True:
#     num=int(input("请输入一个数"))#输入的数值
#     if num>j:
#         j=num
#     a=a+num
#     print("当前总额为",a)
#     print("平均数为:", a / i)
#     print("最大数为",j)
#     i=i+1
#     if i==10:
#         break

# import random
# ran=random.randint(50,150)
# print(ran)

# a=int(input("请输入一个数"))
# b=int(input("请输入第二个数"))
# c=int(input("请输入第三个数"))
# if (a>0 and b>0 and c>0):
#     if (a+b>c and a+c>b and b+c>a):
#         print("可以构成三角形")
#         if(a==b and a!=c) or (b==c and b!=a) or (a==c and a!=b):
#             print("等腰三角形")
#         elif(a==b==c):
#             print("等边三角形")
#         elif(a*a+b*b==c*c) or (a*a+c*c==b*b) or (b*b+c*c==a*a):
#             print("直角三角形")
#         else:
#             print("普通三角形")
#     else:
#         print("不构成三角形")

# for i in range(9,0,-1):
#     for j in range(1,i+1):
#         print(j,'X',i,'=',j*i,' ',end="")
#     print()

# i=1
# a=input("请输入一个数：")
# while i<=int(a):
#     j=1
#     while j<=i:
#         print(j,'*',i,'=',j*i,' ',end="")
#         j+=1
#     print()
#     i+=1

# shuru=eval(input("请输入:"))
# hang=int(shuru/2)+1
# n=1
# for i in range(hang):
#     a = ' ' * ((shuru-n)//2)
#     b = '*' * n
#     print(a+b+a)
#     n+=2

# k=1
# a=0
# for i in range(1,21):
#    k*=i
#    a+=k
# print(a)

# tian=0
# qi=0
# while True:
#     qi=qi+3
#     tian =tian+1
#     if qi==20 or qi>20:
#         print("第",tian,"天青蛙爬了",qi,"米")
#         break
#     else:
#         qi = qi - 2

# tall=20
# i=0
# day=0
# while i<tall:
#     day +=1
#     i +=3
#     if i>tall or i== tall:
#         print(day,'天')
#         break
#     else:
#         i -=2

# A = 56
# B = 78
# i = 1
# while i <= 3:
#     yh = input("请输入用户名")
#     mm = input("请输入密码")
#     if yh == str('root'):
#         print("输入正确")
#         if mm == str('admin'):
#             print("输入正确")
#             while True:
#                 num = input("请输入+或-")
#                 if num == str('+'):
#                     print(A)
#                     print(B)
#                 elif num == str('-'):
#                     print(B)
#                     print(A)
#                 else:
#                     print("输入错误")
#                     break
#     else:
#         print("输入错误")
#         i += 1


# import random
# ju=0
# while True:
#     x = input('请按1开始抽取优惠卷')
#     if x == '1':
#         a = random.randint(1, 31)
#         if a < 11:
#             ju = 0.3
#             break
#         elif a > 10 and a < 31:
#             ju = 0.9
#             break
#         else:
#             ju = 0
#             break
#
#     else:
#         print('请输入正确数字')
# if ju==0.3:
#     print('您获得辣条3折卷')
# elif ju==0.9:
#     print('您获得威猛先生9折卷')
# else:
#     print('您获得免单卷')
# shopping=[
#     ["小米",10],
#     ["大米",30],
#     ["西红柿",50],
#     ["黄瓜",80],
#     ["胡萝卜",100],
#     ["辣条",50],
#     ["威猛先生",80],
# ]
# mycar=[]
# money=1000
# while True:
#     for i in enumerate(shopping):
#         print(i)
#     shop=input("请输入商品：")
#     if shop.isdigit():
#         shop=int(shop)
#         if shop<len(shopping):
#             if money>shopping[shop][1]:
#                 mycar.append(shopping[shop])
#                 if ju==0.3 and shop==5:
#                     money=money-shopping[shop][1]*ju*0.8
#                 elif ju==0.9 and shop==6:
#                     money=money-shopping[shop][1]*ju*0.8
#                 elif ju==0:
#                     money=money
#                 else:
#                     money-=shopping[shop][1]*0.8
#                 print("此商品已经加入购物车，您的余额为：",money)
#             else:
#                 print("余额不足")
#         else:
#             print("请输入正确的商品编号")
#     elif shop=='q' or shop=='Q':
#         print("再见，您的商品小票为：")
#         # for i in enumerate(mycar):
#         print(mycar)
#         break
#     else:print("您输入的有误")

# GDP=[36710.36,35427.10,29863.23,29667.39,27665.36,27650.45,27620.38,25369.20]
# #     0          1       2        3         4        5        6        7
# he=0
# for i in range(1,9):
#     he=he+GDP[0]
# print('前八城市GDP和为%.2f'%he)
# print('平均GDP为：%.2f'%(he/i))

# a = [1,5,21,30,15,9,30,24]
# he=0
# for j in a:
#     if (j%5)==0:
#         he+=j
# print(he)


# list=[1,2,3,4,5,6,7,8,9]
# print(list[::-1])

# from collections import Counter
# List = [1,4,7,5,8,2,1,3,4,5,9,7,6,1,10]
# a = Counter(List)
# print(a)

# l=[1]
# n=int(input("请输入层数"))
# for i in range(n):
#     print(l)
#     l.append(0)
#     l=[l[k]+l[k-1] for k in range (0,i+2)]


#
#
# l=[1]                         l[1,0]
# n=int(input('输入层数'))
# for i in range(n):
#     print(l)
#     l.append(0)
#     l=[l[K]+l[K-1] for K in range (0,i+2)]

# dict = {"k1":"v1","k2":"v2","k3":"v3"}
# for i in dict:
#     print(i)
# for i in dict:
#     print(dict[i])

# dict.update({"k4":"v4"})
# print(dict)

# Friuts = {
# 	    '苹果':12.3,  # 水果和单价
# 	    '草莓':4.5,
#         '香蕉':6.3,
#         '葡萄':5.8,
#         '橘子':6.4,
#         '樱桃':15.8
# }
# info={
#     '小明':{
#         'fruits':{'苹果':4,'草莓':13,'香蕉':10},
#         'money':0
#     },
#     '小刚':{
#         'fruits':{'葡萄':19, '橘子':12, '樱桃':30},
#         'money':0
#     }
# }
# for i in info['小明']['fruits']:
#     money=Friuts[i]*info['小明']['fruits'][i]
#     info['小明']['money']+=money
# print("小明的水果价格为",info['小明']['money'])
# for j in info['小刚']['fruits']:
#     money2=Friuts[j]*info['小刚']['fruits'][j]
#     info['小刚']['money']+=money2
# print("小刚的水果价格为",info['小刚']['money'])

# num=[21,56,10,21,56,10]
# def all_nums(num):
#       a={}
#       for i in set(num):
#             a[i]=num.count(i)
#       return a
# print(all_nums(num))

# names = [
#     ["刘备","56","男","106","IBM", 500 ,"50"],
#     ["大乔","19","女","230","微软", 501 ,"60"],
#     ["小乔", "19", "女", "210", "Oracle", 600, "60"],
#     ["张飞", "45", "男", "230", "Tencent", 700 , "10"]
# ]
# a1={'刘备':{'年龄':56,'性别':'男','编号':106,'任职公司':'IBM','薪资':500,'部门编号':50}}
# a2={'大乔':{'年龄':19,'性别':'女','编号':230,'任职公司':'微软','薪资':501,'部门编号':60}}
# a3={'小乔':{'年龄':19,'性别':'女','编号':210,'任职公司':'Oracle','薪资':600,'部门编号':60}}
# a4={'张飞':{'年龄':45,'性别':'男','编号':230,'任职公司':'Tencent','薪资':700,'部门编号':10}}


