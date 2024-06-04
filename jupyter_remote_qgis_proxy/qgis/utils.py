import pathlib
import subprocess
import uuid

def open_qgis(action="add_vector_layer", **kwargs):
    current_file_path = pathlib.Path(__file__).parent.resolve()
    # script to zoom to the first layer
    zoom_script_path = f"{current_file_path}/scripts/zoom.py"
    # script to maximize the window
    maximize_script_path = f"{current_file_path}/scripts/maximize.py"
    if not action or not kwargs.get("url"):
        subprocess.Popen(["qgis", "--nologo", "--code", maximize_script_path])
        return

    available_templates = ("add_vector_layer",)
    if action not in available_templates:
        raise ValueError(f"Action {action} not available. Choose from {available_templates}")

    with open(f"{current_file_path}/templates/{action}.qgs") as f:
        action_template = f.read()
    project_name = kwargs.get("project_name", "new project")
    file_path = f"/tmp/{project_name}.qgs"
    with open(file_path, "w") as f:
        layer_args = {
            "layer_name": kwargs.get("layer_name", "Vector Layer"),
            "layer_src": f"/vsicurl/{kwargs['url']}",
            "layer_id": str(uuid.uuid4()),
        }
        project_file_content = action_template.format(**layer_args)
        f.write(project_file_content)
    subprocess.Popen(["qgis", "--nologo", "--project", file_path, "--code", zoom_script_path, "--code", maximize_script_path])
