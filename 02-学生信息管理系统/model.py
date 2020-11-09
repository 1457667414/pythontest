# Name：林
# Time： 2020/11/5 16:16
import tools


class Teacher(object):
    def __init__(self, name, password):
        self.name = name
        self.password = tools.password_salt(password)


class Student(object):
    def __init__(self, s_id, name, age, gender, tel):
        self.s_id = s_id
        self.name = name
        self.age = age
        self.gender = gender
        self.tel = tel
