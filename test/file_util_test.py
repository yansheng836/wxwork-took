#!/usr/bin/env python
# -*-coding:utf-8 -*-
"""
@author: yansheng
@file: file_util_test.py
@time: 2024/10/13
"""
# import utils.image_utils
from utils import file_utils

directory = r'D:\WXWork\1688850205828112\Cache\File\2021-09'
directory = r'D:\WXWork\1688850205828112\Cache\File\2021-11'
# directory = r'C:\Users\荷塘月色\Documents\Navicat\PostgreSQL\pgsql-backup-sql-v2.4.10-20241020-荣耀\Premium\logs'
# directory = r'C:\Users\荷塘月色\Documents\Navicat\PostgreSQL\pgsql-backup-sql\Premium\logs'
# directory = r'C:\Users\荷塘月色\Documents\Navicat\Premium\logs'
file_utils.remove_duplicate_content_file(directory)
