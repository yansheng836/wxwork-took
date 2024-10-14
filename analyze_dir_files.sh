#!/bin/bash

#date_str=`date +'%Y%m%d-%H%M'`
date_str=`date +'%Y年%m月%d日%H%M'`
echo 当前时间为：$date_str

#echo `date` >> count_dir_files.txt
for dir in */; do
   echo "${dir%/} contains $(find "${dir%/}" -type f | wc -l) files" >> count_dir_files-$date_str.txt
done
#echo '' >> count_dir_files.txt

du --max-depth 1 -h > du--max-depth-1-h-$date_str.txt

find > find-$date_str.txt
