::@echo Off
::@echo on
echo ���ڴ������

::���з�ʽ1��������������
::����˵��
::--clean           ����ϴ����ɵ��ļ���Ĭ�ϲ���գ�
::-y                ֱ�Ӹ��Ǿ��ļ���������ǵ��ļ�ģʽ����dist���Ѿ��ж�ӦĿ¼�ˣ�����ʾ�Ƿ񸲸ǣ�
::-i                ָ��Windows iconͼ��
::--version-file    ָ�������Ȩ��Ϣ
::-n                ָ���ļ���
pyinstaller.exe --clean -y -F -i favicon.ico --version-file file_version_info.txt -n ��΢�Ĺ��߰� main.py

::���з�ʽ2����spec����
::pyinstaller.exe xuanwu-excel2json.spec

pandoc README.md  -o .\dist\��΢�Ĺ��߰�-ʹ��˵��.docx

mkdir        .\release\latest
del   /q/f   .\release\latest\*
copy .\dist  .\release\latest  /Y /D
copy .\*.xml .\release\latest  /Y /D

echo ������������ ./release/latest Ŀ¼��
pause
exit
