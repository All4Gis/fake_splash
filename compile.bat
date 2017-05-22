@ECHO OFF
set BASE=C:\OSGeo4W64

 
set PATH=%BASE%\bin;%PATH%
set PATH=%PATH%;%BASE%\apps\qgis\bin

call "%BASE%\bin\o4w_env.bat"

cd /d %~dp0

@ECHO ON

call pyrcc4 ui\resources.qrc -o gui\generated\resources_rc.py

@ECHO OFF

GOTO END

:ERROR
   echo "Compile Error"
   set ERRORLEVEL=%ERRORLEVEL%
   pause  
:END

::pause
 