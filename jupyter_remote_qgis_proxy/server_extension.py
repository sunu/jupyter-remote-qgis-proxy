from pathlib import Path

from jupyter_server.utils import url_path_join
from jupyter_server_proxy.handlers import AddSlashHandler

from .handlers import QgisHandler

HERE = Path(__file__).parent


def load_jupyter_server_extension(server_app):
    """
    Called during notebook start
    """
    base_url = server_app.web_app.settings["base_url"]

    server_app.web_app.add_handlers(
        ".*",
        [
            (url_path_join(base_url, "/qgis"), AddSlashHandler),
            (url_path_join(base_url, "/qgis/"), QgisHandler),
        ],
    )
