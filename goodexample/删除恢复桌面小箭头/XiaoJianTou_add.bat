@echo off
echo edit reg...
reg add "HKEY_CLASSES_ROOT\lnkfile" /v IsShortcut /f 
echo restart explorer ...
taskkill /f /im explorer.exe 
start explorer.exe