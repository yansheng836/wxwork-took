#!/bin/bash
# 把小于10kb的照片，当做是表情包（当然实际上不止这些，因为在企微表情包就是图片来的，好像没有什么规律，暂时只是按照大小来计算）
find ./2023-11 -size -10K
find ./2023-11 -size -10K rm -rf 