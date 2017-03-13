set dirpath=%~dp0
cd /D %dirpath%
start C:\Python27\python.exe Cycling_Report.py -p all
dir
timeout 10