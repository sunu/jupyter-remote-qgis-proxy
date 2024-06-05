"""Zoom to the full extent of the first layer in the project"""

from qgis.core import QgsProject
import qgis.utils

# Get the QGIS interface
iface = qgis.utils.iface
iface.mainWindow().showMaximized()

# Get the active map canvas
canvas = iface.mapCanvas()

layers = QgsProject.instance().mapLayers().values()

for layer in layers:
    # Zoom to the full extent of the layer
    canvas.setExtent(layer.extent())
    canvas.refresh()
    break