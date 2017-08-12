#/usr/bin/env python
#coding=utf-8

import logging

logger = logging.getLogger()   #日志对象

logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")  #输出格式对象

fh = logging.FileHandler('test1.log')  #日志处理对象，表示像文件输出

ch = logging.StreamHandler()  #日志处理对象，表示像终端输出


fh.setFormatter(formatter)  # 输出采用什么样的格式

ch.setFormatter(formatter)

#给logger添加handller
logger.addHandler(fh)
logger.addHandler(ch)



logger.debug("debug message")
logger.info("info message")
logger.warning("warning message")
logger.error("error message")
logger.critical("critical message")
