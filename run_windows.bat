@echo off

::check for python installation
python --version 2>NUL 1>NUL
if errorlevel 1 goto InstallPython


python --version | find "3." 2>NUL 1>NUL
if not errorlevel 1 goto HasPython

::Python is not installed
::%~dp0 tells the current directory 
::start "" "path" opens app in new window and simply "path" opens app in same window
::/qn is for quiet install

:InstallPython
echo Installing Python 3
"%~dp0/Installation packages/python-3.4.0.msi" /qn 

::If python is already installed then run the server (HasPython is a goto statement)

:HasPython
echo Server is Running 
cd %~dp0
start "" "main/index.html"
python -m http.server --bind localhost --cgi 8000

