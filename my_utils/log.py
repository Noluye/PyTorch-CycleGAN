# -*- coding: utf-8 -*-
"""
@File  : log.py
@Author: Yulong He
@Date  : 2020/6/4 15:31
@Desc  : 
"""
import logging
import coloredlogs

# Create a logging manager: support both stream output and file output.
FMT_STR = "%(asctime)s %(filename)s %(funcName)s line(%(lineno)s) %(levelname)s - %(message)s"
FMT_DATE = "%Y-%m-%d %H:%M:%S"

logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler(filename="log.txt")
file_handler.setLevel(logging.WARNING)
file_handler.setFormatter(logging.Formatter(FMT_STR, FMT_DATE))
logger.addHandler(file_handler)

coloredlogs.install(level='DEBUG', logger=logger, fmt=FMT_STR, datefmt=FMT_DATE)
