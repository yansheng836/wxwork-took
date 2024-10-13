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
file_utils.remove_duplicate_content(directory)
