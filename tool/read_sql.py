import os

import pymysql

from config import db, BASE_PATH
from tool.get_log import GetLogger

log = GetLogger.get_log()


def read_sql(filename):
    """读取navicat转储文件，恢复表"""
    log.info(f'读取navicat转储文件{filename}，恢复表')
    path = BASE_PATH + os.sep + 'data' + os.sep + filename
    with open(path, 'r', encoding='utf-8') as f:
        sql_list = []
        for line in f.readlines():
            if line.startswith('SET'):
                sql_list.append(line.replace('\n', ''))
            elif line.startswith('DROP'):
                sql_list.append(line.replace('DROP', 'TRUNCATE').replace(' IF EXISTS', '').replace('\n', ''))
            elif line.startswith('INSERT'):
                sql_list.append(line.replace('\n', ''))
            else:
                pass

    conn = pymysql.connect(db['db1']['host'],
                           db['db1']['user'],
                           db['db1']['password'],
                           db['db1']['database'],
                           db['db1']['port'],
                           charset='utf8'
                           )
    c = conn.cursor()
    for sql in sql_list:
        c.execute(sql)
    conn.commit()
    c.close()
    conn.close()
    log.info('数据库初始化恢复成功！')


if __name__ == '__main__':
    read_sql('tp_users.sql')
