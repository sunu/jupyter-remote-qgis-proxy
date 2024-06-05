# Jupyter Remote QGIS Proxy

Run QGIS inside a remote Desktop on Jupyter and open remote data sources.

This is based on [jupyter-remote-desktop-proxy](https://github.com/jupyterhub/jupyter-remote-desktop-proxy).

## Usage

For now, use this as part of [nasa-qgis-image](https://github.com/sunu/nasa-qgis-image/tree/qgis-proxy). To run locally:

1. Clone the repository and checkout the `qgis-proxy` branch:

    ```bash
    git clone git@github.com:sunu/nasa-qgis-image.git
    cd nasa-qgis-image
    git checkout qgis-proxy
    ```
2. Build the image:

    ```bash
    docker build -t qgis .
    ```
3. Run the Jupyter lab server:

    ```bash
    docker run -it -p 8888:8888 --security-opt seccomp=unconfined qgis
    ```
4. Open remote vector data in your browser by going to a URL like:

    ```
    http://127.0.0.1:8888/qgis/?action=add_vector_layer&url=https://raw.githubusercontent.com/flatgeobuf/flatgeobuf/master/test/data/countries.fgb&layer_name=countries-fgb&project_name=countries
    ```
