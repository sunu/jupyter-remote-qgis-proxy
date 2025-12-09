import psutil

from .logger import logger
from .qgis.utils import open_qgis


def is_process_running(process_name):
    """
    Checks if a process with the given name is running.
    """
    for process in psutil.process_iter():
        try:
            if process.name().lower() == process_name.lower():
                # Check if the process is not a zombie
                if process.status() != psutil.STATUS_ZOMBIE:
                    return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return False


def start_qgis(action, url, project_name, layer_name):
    """Starts QGIS if necessary.

    If we have an action and a URL, we will start QGIS with those parameters.
    If not and we just want to open QGIS without opening a specific project,
    we will check if QGIS is already running. If it is not running, we will start it.
    If it is running, we will skip starting QGIS.
    """
    if action and url:
        logger.info(
            f"Starting QGIS with action: {action}, url: {url}, project_name: {project_name}, layer_name: {layer_name}"
        )
        open_qgis(action, url=url, project_name=project_name, layer_name=layer_name)
    elif not is_process_running("qgis"):
        logger.info("QGIS is not running, starting QGIS")
        open_qgis()
    else:
        logger.info("QGIS is already running, skipping start")
