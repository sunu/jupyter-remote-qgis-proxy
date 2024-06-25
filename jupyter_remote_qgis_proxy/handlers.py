from jupyter_remote_desktop_proxy.handlers import DesktopHandler
from tornado import web
from tornado.ioloop import IOLoop

from .utils import start_qgis


class QgisHandler(DesktopHandler):
    @web.authenticated
    async def get(self):
        await super().get()
        action = self.get_argument("action", None)
        url = self.get_argument("url", None)
        project_name = self.get_argument("project_name", "new project")
        layer_name = self.get_argument("layer_name", "Vector Layer")

        IOLoop.current().call_later(
            delay=3,
            callback=lambda: start_qgis(
                action=action, url=url, project_name=project_name, layer_name=layer_name
            ),
        )
