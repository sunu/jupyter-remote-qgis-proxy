import os
import logging

from jupyter_remote_desktop_proxy.handlers import DesktopHandler
from tornado import web

from .qgis.utils import open_qgis

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class QgisHandler(DesktopHandler):
    @web.authenticated
    async def get(self):
        logging.info("Starting QGIS")
        action = self.get_argument("action", None)
        url = self.get_argument("url", None)
        project_name = self.get_argument("project_name", "new project")
        layer_name = self.get_argument("layer_name", "Vector Layer")
        if action and url:
            open_qgis(action, url=url, project_name=project_name, layer_name=layer_name)
        await super().get()
