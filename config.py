import os

# 文件路径配置信息
BASE_PATH = os.path.dirname(__file__)
# print(BASE_PATH,os.path)

# 数据库连接配置信息
db = {
    'db1':
    {'host': '192.168.128.128',
     'user': 'root',
     'password': 'root',
     'database': 'tpshop2.0',
     'port': 3306,
     }
}
