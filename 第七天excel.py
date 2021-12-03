import xlrd
import numpy as np
wb=xlrd.open_workbook(filename=r"百度合作单位-人员管理-二期.xls",encoding_override=True)
st=wb.sheet_by_index(0)
ll=st.ncols
hh=st.nrows
'''
l=st.col_values(1,1) #列 （第几列，第几行开始，第几行结束）
h=st.row_values()   #行  （第几行，第几列开始，第几列结束）
cellvalue=st.cell_value(5,4)   #范围 （第几行，第几列）
print(cellvalue)
a)	统计所有表格中有多少人
b)	统计办电信，联通，移动的用户数量（14,17开头为电信）（13开头为移动）（15开头为联通）
c)	总公司男女人数
d)	年龄超过45岁的老员工人数
e)	薪资高于8000元的高薪人员数量和薪资低于3000的底薪人员数量
f)	统计去传媒公司的工作的人员数量
g)	统计一下可能在疫情高危地区的人数（高危地区：黑龙江，北京，福建，四川）
'''
# print("表格共有",hh-1,"人")
# num=st.col_values(5,1)
# telecomm=0
# link=0
# move=0
# for c in num:
#     a=c[:2]
#     if a=='14' or a=='17':
#         telecomm+=1
#     elif a =='13':
#         move+=1
#     elif a=='15':
#         link+=1
# print("电信用户为：",telecomm,'移动用户为',move,'联通用户为',link)

# num=st.col_values(8,1)
# men=0
# man=0
# for n in num:
#     if n=='男':
#         man+=1
#     elif n=='女':
#         men+=1
# print('男生人数',man,'女生人数',men)

# num=st.col_values(11,1)
# quantity=0
# for i in num:
#     if i>8000 or i<3000:
#         quantity+=1
# print("高于八千低于三千的人数和为",quantity)

# num=st.col_values(13,1)
# n=0
# for i in num:
#     if '传媒' in i:
#         n+=1
# print("去传媒公司人数数量",n)

num=st.col_values(9,1)
sum=0
for i in num:
    if '黑龙江' in i or '北京'in i or '福建'in i or '四川'in i:
        sum+=1
print("去高危地区人数为",sum)