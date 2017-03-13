@echo off
REM runas /user:binzhe1x@CCR 
echo edit reg ...
reg delete "HKEY_CLASSES_ROOT\lnkfile" /v IsShortcut /f 
echo restart explorer now...
taskkill /f /im explorer.exe 
start explorer.exe