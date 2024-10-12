::@echo Off
::@echo on
echo 正在打包……

::运行方式1：用命令行生成
::参数说明
::--clean           清空上次生成的文件（默认不清空）
::-y                直接覆盖旧文件（如果不是单文件模式，且dist下已经有对应目录了，会提示是否覆盖）
::-i                指定Windows icon图标
::--version-file    指定软件版权信息
::-n                指定文件名
pyinstaller.exe --clean -y -F -i favicon.ico --version-file file_version_info.txt -n 企微的工具包 main.py

::运行方式2：用spec生成
::pyinstaller.exe xuanwu-excel2json.spec

pandoc README.md  -o .\dist\企微的工具包-使用说明.docx

mkdir        .\release\latest
del   /q/f   .\release\latest\*
copy .\dist  .\release\latest  /Y /D
copy .\*.xml .\release\latest  /Y /D

echo 打包结束，详见 ./release/latest 目录。
pause
exit
