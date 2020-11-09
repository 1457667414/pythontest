# Name：林
# Time： 2020/11/5 15:01
base_dir = './files/'
import json


def read_file(file_name):
    try:
        with open(base_dir + file_name, 'r', encoding='utf8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print('文件未找到')


def write_json(file_name, data):
    with open(base_dir + file_name, 'w', encoding='utf8') as file:
        # 利用json模块将data以json数据写入file文件
        json.dump(data, file)


def read_json(file_name, default_data):
    try:
        with open(base_dir + file_name, 'r', encoding='utf8') as file:
            return json.load(file)
    except FileNotFoundError:
        return default_data
