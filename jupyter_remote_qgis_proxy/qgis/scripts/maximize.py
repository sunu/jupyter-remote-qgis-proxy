"""Maximize the QGIS window."""
import qgis.utils

# Get the QGIS interface
iface = qgis.utils.iface
iface.mainWindow().showMaximized()