#!/bin/bash
# 把小于10kb的照片，当做是表情包（当然实际上不止这些，因为在企微表情包就是图片来的，好像没有什么规律，暂时只是按照大小来计算）
find ./ -type f -size -15k -exec rm -f {} \;
find ./ -type f -name "*charset*" -exec rm -f {} \;
find ./ -type f -name ".WeDrive" -exec rm -f {} \;
find ./ -type d -empty -exec rm -rf {} \;
