import pathlib
import subprocess
import uuid
from urllib.parse import quote

from jupyter_remote_qgis_proxy.logger import logger


def open_qgis(action="add_vector_layer", **kwargs):
    """
    Open QGIS with a specific action and layer source.
    """
    current_file_path = pathlib.Path(__file__).parent.resolve()
    # script to zoom to the first layer
    zoom_script_path = f"{current_file_path}/scripts/zoom.py"
    # script to maximize the window
    maximize_script_path = f"{current_file_path}/scripts/maximize.py"
    if not action or not kwargs.get("url"):
        subprocess.Popen(["qgis", "--nologo", "--code", maximize_script_path])
        return

    available_templates = ("add_vector_layer", "add_xyz_tile_layer")
    if action not in available_templates:
        raise ValueError(
            f"Action {action} not available. Choose from {available_templates}"
        )

    with open(f"{current_file_path}/templates/{action}.qgs") as f:
        action_template = f.read()
    project_name = kwargs.get("project_name", "new project")
    qgis_projects_dir = pathlib.Path.home() / "qgis-projects"
    qgis_projects_dir.mkdir(exist_ok=True)
    file_path = qgis_projects_dir / f"{project_name}.qgs"
    with open(file_path, "w") as f:
        if action == "add_xyz_tile_layer":
            logger.info(f"XYZ Tile Layer URL: {kwargs['url']}")

            url = kwargs["url"]
            url_parts = url.split("?")
            if len(url_parts) > 1:
                base_url = url.split("?")[0]
                query_string = url.split("?")[1]
                separator = "\n\n\n\n\n"
                query_string = query_string + separator
                encoded_query_string = quote(query_string, safe="")
                url = base_url + "?" + encoded_query_string

            layer_src = f"http-header:referer=&amp;type=xyz&amp;url={url}&amp;zmax=18&amp;zmin=0"
            layer_args = {
                "layer_name": kwargs.get("layer_name", "XYZ Tile Layer"),
                "layer_src": layer_src,
                "layer_id": str(uuid.uuid4()),
            }
        else:
            layer_args = {
                "layer_name": kwargs.get("layer_name", "Vector Layer"),
                "layer_src": f"/vsicurl/{kwargs['url']}",
                "layer_id": str(uuid.uuid4()),
            }
        project_file_content = action_template.format(**layer_args)
        f.write(project_file_content)
    subprocess.Popen(
        ["qgis", "--nologo", "--project", str(file_path), "--code", zoom_script_path]
    )
