# Name：林
# Time： 2020/11/5 10:50
user_list = [{'name': '1', 'tel': '123', 'email': '123'},
             {'name': '2', 'tel': '234', 'email': '234'},
             {'name': '3', 'tel': '345', 'email': '345'},
             {'name': '4', 'tel': '456', 'email': '456'},
             {'name': '5', 'tel': '567', 'email': '567'}]


def add_user():
    name = input('请输入姓名：')
    tel = input('请输入手机号：')
    for users in user_list:
        if users['tel'] == tel:
            print('此电话号码已经存在')
            break
    else:
        email = input('请输入邮箱：')
        for users in user_list:
            if users['email'] == email:
                print('此邮箱已经存在！')
                break
        else:
            user = {'name': name, 'tel': tel, 'email': email}
            user_list.append(user)
    for i in user_list:
        print(i)


def check_number(n):
    if n.isdigit():
        number = int(n)
        if 0 <= number < len(user_list):
            return True
    return False


def del_user():
    number = input('请输入您要删除的序号（序号从0开始）：')
    if check_number(number):
        # 当输入的序号合法后
        user = user_list[int(number)]
        print(f'您要删除的信息为：{user}')
        answer = input('您确定要删除吗？（yes or no）：')
        if answer.lower() == 'y' or answer.lower() == 'yes':
            user_list.pop(int(number) - 1)
    else:
        print('输入的序号不合法！')
    for i in user_list:
        print(i)


def modify_user():
    number = input('请输入您要修改的序号（序号从0开始）：')
    if check_number(number):
        user = user_list[int(number)]
        print(f'您要修改的信息为：{user}')
        new_name = input('请输入新的姓名：')
        new_tel = input('请输入新的电话号码：')
        for user in user_list:
            if user['tel'] == new_tel:
                print('此电话号码已经存在')
                modify_user()
                return
        else:
            new_email = input('请输入新的邮箱：')
            for user in user_list:
                if user['email'] == new_email:
                    print('此邮箱地址已经存在！')
                    modify_user()
                    return
            else:
                answer = input('您确定要修改吗？（yes or no）：')
                if answer.lower() == 'y' or answer.lower() == 'yes':
                    user['name'] = new_name
                    user['tel'] = new_tel
                    user['email'] = new_email


def query_user():
    query_name = input('请输入您要查找的姓名：')
    for user in user_list:
        if user['name'] == query_name:
            print(f'您查找的信息为：{user}')
            return
    else:
        print('没有您要找的信息！')


def show_all():
    print('序号      姓名        手机号        邮箱')
    for i, item in enumerate(user_list):
        print(i, '\t\t ', item['name'], '\t\t ', item['tel'], '\t\t ', item['email'])


def exit_system():
    # print('退出系统成功')
    answer = input('亲，确定要退出吗？（yes or no）：')
    return answer.lower() == 'y' or answer.lower() == 'yes'
    # print(answer.lower())
    # exit(0)


def star():
    while True:
        print("""-----------------------------------
        01-名片管理系统 V1.0
            1.添加名片
            2.删除名片
            3.修改名片
            4.查询名片
            5.显示所有名片
            6.退出系统
-----------------------------------""")
        operator = input('请输入要进行的操作（数字）：')
        if operator == '1':
            add_user()
        elif operator == '2':
            del_user()
        elif operator == '3':
            modify_user()
        elif operator == '4':
            query_user()
        elif operator == '5':
            show_all()
        elif operator == '6':
            is_exit = exit_system()
            if is_exit:
                # flag = False
                break
        else:
            print('输入有误请重新输入！')


if __name__ == '__main__':
    star()
