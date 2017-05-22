## Fake Splash Screen for QGIS	

With this plugin, you can modify the QGIS splash without having to compile the core.
The current image and icon are a simple joke, but you can change them and compile the plugin with your own image and icon like, for example, your company logo.

![](images/splash.png?raw=true)

## How to compile the plugin

If you want to change the image, open the [images](https://github.com/All4Gis/fake_splash/tree/master/images) folder and modify the files [logo.png](images/logo.png?raw=true) and [splash.png](images/splash.png?raw=true) (if you don't want to modify the code, make sure that these files have the same name and extension as indicated).
Once you have done this, open the [compile.bat](https://github.com/All4Gis/fake_splash/tree/master/compile.bat) file and set the variable `BASE` to the path to your **QGIS** or **OSGEO4W** installation and make sure that the variable `PATH` is also correct. Now, you only have to run it and open the generated folder where you will find the `.py` for the dialog and the resources file.

Open qgis and you will see your new splash and logo.

**compile.bat**

```bat
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
```

## Notes

If after uninstalling the plugin, the qgis splash is not shown, open the python console and execute the following command:

```
from qgis.PyQt.QtCore import *
QSettings().setValue("/qgis/hideSplash", False)
```

**TODO** 

- Restore Qgis to the original state if the plugin is uninstalled or deactivated (icon, splash and title)

## Donations
Want to buy me a beer (or gadget)? Please use Paypal button on the project page, [![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.me/all4gis) , or contact me directly.

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?button=donate&business=5329N9XX4WQHY&item_name=FakeSplash+Plugin&quantity=&amount=&currency_code=EUR&shipping=&tax=&notify_url=&cmd=_donations&bn=JavaScriptButton_donate&env=www)
 
If this plugin is useful for you, consider to donate to the author.


[© All4gis 2017]
