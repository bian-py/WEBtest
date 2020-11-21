import logging.handlers
import os

from config import BASE_PATH

"""
简单用法
def get_logging():
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=fmt, filename="./log/log01.log")
    return logging 
#     init包文件中自动实例化
"""


# 高级用法(单例模式）
class GetLogger:
    logger = None

    @classmethod
    def get_log(cls):
        if cls.logger is None:

            fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
            # 获取日志器
            cls.logger = logging.getLogger("admin")
            # 设置日志器级别
            cls.logger.setLevel(logging.INFO)
            # 获取处理器（控制台）
            sh = logging.StreamHandler()
            # 获取处理器（文件，以时间分割）
            path1 = BASE_PATH + os.sep + 'log' + os.sep + 'loginfo.log'
            path2 = BASE_PATH + os.sep + 'log' + os.sep + 'logerror.log'
            th = logging.handlers.TimedRotatingFileHandler(path1,
                                                           "midnight",
                                                           1,
                                                           30,
                                                           encoding="utf-8")
            th2 = logging.handlers.TimedRotatingFileHandler(path2,
                                                            "midnight",
                                                            1,
                                                            30,
                                                            encoding="utf-8")
            # 设置处理器级别
            sh.setLevel(logging.INFO)
            th.setLevel(logging.INFO)
            th2.setLevel(logging.ERROR)
            # 设置格式器
            fm = logging.Formatter(fmt)
            # 将格式器添加到处理器
            sh.setFormatter(fm)
            th.setFormatter(fm)
            th2.setFormatter(fm)
            # 将处理器添加到日志器中
            cls.logger.addHandler(sh)
            cls.logger.addHandler(th)
            cls.logger.addHandler(th2)

        return cls.logger


if __name__ == "__main__":
    logger = Getlogger.get_log()
    logger.info("这个info日志信息")
    logger.debug("这个debug日志信息")
    logger.error("这个error日志信息")
    logger.warning("这个warning日志信息")
    logger.critical("这个critical日志信息")
