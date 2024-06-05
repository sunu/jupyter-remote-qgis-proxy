import psutil
import time

from .logger import logger
from .qgis.utils import open_qgis


def is_process_running(process_name):
  """
  Checks if a process with the given name is running.
  """
  for process in psutil.process_iter():
    try:
      if process.name().lower() == process_name.lower():
        return True
    except (psutil.NoSuchProcess, psutil.AccessDenied):
      pass
  return False


def wait_for_condition(condition, timeout=10):
  """
  Waits for a condition to be true for a specified timeout.

  Args:
      condition: A callable that returns True when the condition is met.
      timeout: The maximum time in seconds to wait (default: 10).

  Returns:
      True if the condition becomes true before the timeout, False otherwise.
  """
  start_time = time.time()
  while time.time() - start_time < timeout:
    if condition():
      return True
    time.sleep(0.5)
  return False


def start_qgis(action, url, project_name, layer_name):
    """Starts QGIS and waits for websockify to start if necessary."""
    logger.info("Waiting for websockify to start")
    is_websockify_running = lambda: is_process_running("websockify")
    running = wait_for_condition(is_websockify_running, timeout=10)
    logger.info(f"Websockify is running: {running}")
    logger.info("Starting QGIS")
    if action and url:
        open_qgis(action, url=url, project_name=project_name, layer_name=layer_name)
    elif not is_process_running("qgis"):
        open_qgis()
