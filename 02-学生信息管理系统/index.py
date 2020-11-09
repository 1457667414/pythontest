# Name：林
# Time： 2020/11/5 14:17
import sys

import file_manager
import model
import tools
import student_manager


def register():
    # 读取数据，查看文件里是否有数据如果文件不存在，默认保存一个空字典
    teacher = file_manager.read_json('teacher.json', {})
    while True:
        teacher_name = input('请输入账号(3~6位)：')
        if not 3 <= len(teacher_name) <= 12:
            print('账号不符合要求，请重新输入')
        elif teacher_name in teacher:
            print('注册失败！该账号已经注册过！')
        else:
            break
    while True:
        password = input('请输入密码(6~12位)：')
        if not 6 <= len(password) <= 12:
            print('密码不符合要求，请重新输入')
        else:
            print('注册成功！')
            break
    # teacher[teacher_name] = password
    # 用户名和密码都正确后，创建一个teacher对象，这时可以对数据进行加工
    # 比如加盐加密
    t = model.Teacher(teacher_name, password)
    teacher[t.name] = t.password
    file_manager.write_json('teacher.json', teacher)


def login():
    # 读取数据，查看文件里是否有数据如果文件不存在，默认保存一个空字典
    teacher = file_manager.read_json('teacher.json', {})
    while True:
        teacher_name = input('请输入老师账号：')
        if teacher_name not in teacher:
            print('登录失败！改账号没有注册！')
        else:
            break
    while True:
        password = input('请输入密码：')
        if teacher[teacher_name] == tools.password_salt(password):
            print('登录成功！')
            student_manager.name = teacher_name
            student_manager.show_manager()
            break
        else:
            print('密码错误，登陆失败！')


def start():
    content = file_manager.read_file('welcome.txt')
    while True:
        operator = input(content + '\n请选择（1~3）：')
        if operator == '1':
            login()
        elif operator == '2':
            register()
        elif operator == '3':
            answer = input('确定要退出吗？（y or n）：')
            if answer.lower() == 'y':
                # break
                # exit(0)
                sys.exit(0)
            else:
                print('输入有误！')
        else:
            print('输入有误')


if __name__ == '__main__':
    start()
