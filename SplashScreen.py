# -*- coding: utf-8 -*-
"""
/***************************************************************************
 SplashScreen
                                 A QGIS plugin
 Fake SplashScreen for QGIS.
                             -------------------
        begin                : 2017-05-22
        copyright            : (C) 2017 All4Gis.
        email                : franka1986@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation either version 2 of the License, or     *
 #   any later version.                                                    *
 *                                                                         *
 ***************************************************************************/
"""

try:
    import sys
    from pydevd import *
except:
    None

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtCore import QCoreApplication
from PyQt4.Qt import QApplication

from qgis.core import *
from qgis.gui import *
 
import gui.generated.resources_rc
import qgis.utils
 
class SplashScreen():
    def __init__(self, iface):
 
        self.iface = iface
        
        self.windowTitle = 'GIS Desktop'  
        
        self.app = QApplication.instance()
        self.QApp = QCoreApplication.instance() 

        if self.QApp == None:
            self.QApp = QApplication(sys.argv)

        self.QApp.startingUp()
        self.QApp.processEvents()
        self.app.startDragTime()
        
        self.iface.initializationCompleted.connect(self.customization)
        QtGui.qApp.processEvents()

    def initGui(self):
        QSettings().setValue("/qgis/hideSplash", True)
        QtGui.qApp.processEvents()

        icon = QIcon(":/fake_images/images/logo.png")
        self.app.setWindowIcon(icon)
        self.iface.mainWindow().setWindowIcon(icon)

        self.iface.mainWindow().setWindowTitle(self.windowTitle)  
 
        QtGui.qApp.processEvents()
        
        if not self.iface.mainWindow().isVisible():
            self.splash_pix = QPixmap(':/fake_images/images/splash.png')
            self.splash = QSplashScreen(self.splash_pix, Qt.WindowStaysOnTopHint)
            self.splash.setMask(self.splash_pix.mask())
            self.splash.show()
            QtGui.qApp.processEvents()
            
        return
            
    def run(self):
        pass

    def unload(self):
        QtGui.qApp.processEvents()
        self.iface.initializationCompleted.disconnect(self.customization)
        return

    def customization(self):         
        self.splash.finish(self.iface.mainWindow())
        self.iface.mainWindow().setWindowTitle(self.windowTitle)  
        QtGui.qApp.processEvents()   
