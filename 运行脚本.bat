::@echo Off
::@echo on
echo 正在安装必要工具包……
pip install -r requirements.txt

echo 正在安装运行脚本……
py main.py
pause
exit
