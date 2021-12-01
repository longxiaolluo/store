usergroup = {"12345678": {"name": "小明", "pwd": 123456, "money": 10, 'country': "中国", 'privince': '河北', 'street': '中华街',
                          'door': '101'},
             "87654321": {"name": "小红", "pwd": 654321, "money": 20, 'country': "中国", 'privince': '河北', 'street': '中华街',
                          'door': '101'}}

money = 0
bankname = '中国工商银行'


def jinru():
    while True:
        print("**************************\n"
              "*       中国工商银行        *\n"
              "*       账户管理系统        *\n"
              "**************************\n"

              "*1.开户\n"
              "*2.存钱\n"
              "*3.取钱\n"
              "*4.转账\n"
              "*5.查询\n"
              "*6.Bye！\n"
              "***************************")
        a = int(input("请输入您需要的业务："))
        if a == 1:
            kaihu()
        elif a == 2:
            cunqian()
        elif a == 3:
            quqian()
        elif a == 4:
            zhuanzhang()
        elif a == 5:
            chaxun()
        elif a == 6:
            tuichu()
        else:
            print("输入错误")


def kaihu():
    import random
    while True:
        zhanghao = str(random.randint(10000000, 99999999))
        print("您的账号为", zhanghao)
        name = input("请输入您的姓名")
        pwd = input("请输入您的密码")
        if pwd.isdigit() and len(pwd) == 6:
            pwd = int(pwd)
            country = input("请输入您的国家")
            privince = input("请输入您的省份")
            street = input("请输入您的街道")
            door = input("请输入您的门牌号")
            gift = usrsadd(zhanghao, name, pwd, country, privince, street, door)
            print(usergroup)
            if gift == 1:
                print("开户成功")
                info = '''
                                                                        ------工商银行------
                                                                        1、账号：%s
                                                                        2、姓名：%s
                                                                        3、密码：%s
                                                                        4、国家：%s
                                                                        5、省份：%s
                                                                        6、街道：%s
                                                                        7、门牌号：%s
                                                                        8、余额：%s
                                                                  '''
                print(info % (zhanghao, name, pwd, country, privince, street, door, usergroup[zhanghao]['money']))
                break
            elif gift == 2:
                print("用户重复")
            elif gift == 3:
                print("客户已满")
        else:
            print("密码错误，请重新输入")


def usrsadd(zhanghao, name, pwd, country, privince, street, door):
    if zhanghao in usergroup:
        return 2
    if len(usergroup) >= 100:
        return 3
    usergroup[zhanghao] = {
        "name": name,
        "pwd": pwd,
        "country": country,
        "privince": privince,
        "street": street,
        "door": door,
        "bankname": bankname,
        "money": 0
    }
    return 1


def cunqian():
    print(usergroup)
    zhanghao = input("请输入您的账号")
    savemoney = int(input("请输入您要存的金额"))
    gift = cun_qian(zhanghao, savemoney)
    if gift == 1:
        print("存款成功")
        print("当前账户为：", usergroup[zhanghao]['money'])
    if gift == False:
        print("账户错误")


def cun_qian(zhanghao, savemoney):
    if zhanghao in usergroup.keys():
        usergroup[zhanghao]["money"] += savemoney
        return 1
    else:
        return False


def quqian():
    while True:
        zhanghao = input("请输入您的账号")
        pwd = int(input("请输入您的密码"))
        drawmoney = int(input("请输入您要取的金额"))
        gift = qu_qian(zhanghao, pwd, drawmoney)
        if gift == 3:
            print("余额不足")
        if gift == 2:
            print("密码错误")
        if gift == 1:
            print("取款成功")


def qu_qian(zhanghao, pwd, drawmoney):
    if zhanghao in usergroup.keys() and usergroup[zhanghao]["money"] >= drawmoney and pwd in \
            usergroup[zhanghao]["password"]:
        usergroup[zhanghao]["money"] -= drawmoney
        print("您当前的余额为", usergroup[zhanghao]["money"])
    elif drawmoney > usergroup[zhanghao]["money"] and zhanghao in usergroup.keys() and pwd in \
            usergroup[zhanghao]["password"]:
        return 3
    elif zhanghao in usergroup.keys() and usergroup[zhanghao]["money"] >= drawmoney and pwd != \
            usergroup[zhanghao]["password"]:
        return 2
    else:
        return 1


def zhuanzhang():
    shiftto = input("请输入您转入的账号")
    zhanghao = input("请输入您转出的账号")
    pwd = int(input("请输入您转出账号的密码"))
    money = int(input("请输入您的转账金额："))
    gift = zhuan_zhang(shiftto, zhanghao, pwd, money)
    if gift == 3:
        print("转账成功")
    if gift == 2:
        print("密码错误")
    if gift == 1:
        print("账户不存在")


def zhuan_zhang(shiftto, zhanghao, pwd, money):
    if zhanghao in usergroup.keys() and zhanghao in usergroup.keys():
        if pwd == usergroup[zhanghao]["password"]:
            if money <= usergroup[zhanghao]['money']:
                usergroup[zhanghao]['money'] -= money
                usergroup[shiftto]['money'] += usergroup[zhanghao]['money'] - money
            else:
                return 3
        else:
            return 2
    else:
        return 1


def chaxun():
    zhanghao = input("请输入您要查询的账户")
    pwd = int(input("请输入您的密码"))
    gift = cha_xun(zhanghao, pwd)
    if gift == 1:
        print("查询成功")
        info = '''
                                                                                ------工商银行------
                                                                                1、账号：%s
                                                                                2、姓名：%s
                                                                                3、密码：%s
                                                                                4、国家：%s
                                                                                5、省份：%s
                                                                                6、街道：%s
                                                                                7、门牌号：%s
                                                                                8、余额：%s
                                                                          '''
        print(info % (zhanghao, usergroup[zhanghao]['name'], usergroup[zhanghao]['pwd'], usergroup[zhanghao]['country'],
                      usergroup[zhanghao]['privince'], usergroup[zhanghao]['street'], usergroup[zhanghao]['door'],
                      usergroup[zhanghao]['money']))
    if gift == 2:
        print("密码错误")
    if gift == 3:
        print("账户不存在")


def cha_xun(zhanghao, pwd):
    if zhanghao in usergroup.keys():
        if pwd == usergroup[zhanghao]["pwd"]:
            return 1
        else:
            return 2
    else:
        return 3


def tuichu():
    print("Bye!")


jinru()
