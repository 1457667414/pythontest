# Name：林
# Time： 2020/11/5 19:50
import file_manager
import model
import index

name = ''


def add_student():
    all_students_data = file_manager.read_json(name + '.json', {})
    if not all_students_data:
        students = []
        num = 0
    else:
        students = all_students_data['all_student']
        num = all_students_data['num']
    while True:
        s_name = input('请输入学生姓名：')
        s_age = input('请输入学生年龄：')
        s_gender = input('请输入学生性别：')
        s_tel = input('请输入电话号码：')
        num += 1
        # 字符串的zfill方法：在字符串的前面补0
        s_id = 'stu' + str(num).zfill(4)
        # 创建一个学生对象
        s = model.Student(s_id, s_name, s_age, s_gender, s_tel)
        # 将学生对象以字典的方式存如列表
        students.append(s.__dict__)
        # 将信息拼装后存在json文件里
        stu_data = {'all_student': students, 'num': len(students)}
        file_manager.write_json(name + '.json', stu_data)
        choice = input('添加成功！\n1.继续\n2.返回\n请选择（1~2)：')
        if choice == '1':
            pass
        elif choice == '2':
            break
        else:
            print('输入有误！')
            break


def show_student():
    x = input('1.查看所有的学生\n2.根据姓名查找\n3.根据学号查找\n4.返回：\n请选择(1~4):')
    y = file_manager.read_json(name + '.json', {})
    students = y.get('all_student', [])
    key = value = ''
    if not students:
        print('该老师还没有学员，请添加学员！')
        return
    if x == '1':
        pass
    elif x == '2':
        key = 'name'
        value = input('请输入要查询的姓名：')
    elif x == '3':
        key = 's_id'
        value = input('请输入要查找的学号：')
    elif x == '4':
        return
    else:
        print('输入有误')
        return

    students = filter(lambda s: s.get(key, '') == value, students)
    if not students:
        print('未找到您输入的学员')
        return
    for student in students:
        print('学号：{s_id}；姓名：{name}；性别：{gender}；年龄：{age}；TEL：{tel}'.format(**student))


def modify_student():
    print('修改学生信息暂未实现！')


def delete_student():
    y = file_manager.read_json(name + '.json', {})
    all_students = y.get('all_student', [])
    key = value = ''
    num = input('1.按姓名删除\n2.按学号删除\n3.返回\n请选择(1~3)：')
    if not all_students:
        print('该老师还没有学员，请添加学员！')
        return
    if num == '1':
        key = 'name'
        value = input('请输入要删除的名字：')
    elif num == '2':
        key = 's_id'
        value = input('请输入要删除的学号：')
    else:
        return
    students = list(filter(lambda s: s.get(key, '') == value, all_students))
    if not students:
        print('没有找到对应的学生')
        return
    for i, student in enumerate(students):
        print('{x} 学号：{s_id}；姓名：{name}；性别：{gender}；年龄：{age}；TEL：{tel}'.format(x=i, **student))
    n = input('请输入需要删除的学生的标号(0~{}),或者按q-返回：'.format(i))
    if not n.isdigit() or not 0 <= int(n) <= i:
        if n.lower() == 'q':
            return
        print('输入的内容不合法')
    answer = input('确定要删除学号：{s_id}；姓名：{name}；性别：{gender}；年龄：{age}；TEL：{tel}吗？输入(y or n)：'.format(**student))
    if answer.lower() == 'y':
        all_students.remove(students[int(n)])
        y['all_student'] = all_students
        file_manager.write_json(name + '.json', y)
    else:
        return


def return_now():
    print('退出成功！')
    index.start()


def show_manager():
    while True:
        content = file_manager.read_file('students_page.txt') % name
        print(content)
        operator = input('选择1~5：')
        if operator == '1':
            add_student()
        elif operator == '2':
            show_student()
        elif operator == '3':
            modify_student()
        elif operator == '4':
            delete_student()
        elif operator == '5':
            return_now()
            return
        else:
            print('输入有误！')
