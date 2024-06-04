from jupyter_remote_desktop_proxy.setup_websockify import setup_websockify as _setup_websockify


def setup_websockify():
    config = _setup_websockify()
    config["launcher_entry"] = {"title": "QGIS", "path_info": "qgis"}
    return config
