@ECHO OFF
SET PCMachine= -------NAME OF PC HERE-------
ECHO.
ECHO Reboot %PCMachine% machine
ECHO.
shutdown /r /m \\%PCMachine% /t 0 /f
PAUSE