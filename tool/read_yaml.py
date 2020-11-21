import os

import yaml

from config import BASE_PATH
from tool.get_log import GetLogger

log = GetLogger.get_log()


def read_yaml(filename):
    log.info(f"读取参数化文件{filename}")
    file_path = BASE_PATH + os.sep + "data" + os.sep + filename
    arr = []
    with open(file_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f).values()
        # print(data)
        # for a in data:
        #     arr.append(tuple(a.values()))
        # return arr
        for a in data:
            arr.append(tuple(a))
        return arr


if __name__ == '__main__':
    print(read_yaml('login11.yaml'))
