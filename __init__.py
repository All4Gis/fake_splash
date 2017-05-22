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

import sys
import os
import site
 
# try:
#     sys.path.append("X:/eclipse/plugins/org.python.pydev_5.6.0.201703221358/pysrc")
# except:
#     None
    
def classFactory(iface):
    from SplashScreen import SplashScreen
    return SplashScreen(iface)