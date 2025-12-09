import os

from setuptools import find_packages, setup

HERE = os.path.dirname(__file__)


with open("README.md") as f:
    readme = f.read()


setup(
    name="jupyter-remote-qgis-proxy",
    packages=find_packages(),
    version='0.0.1',
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    description="Run QGIS in a desktop environments on Jupyter",
    entry_points={
        'jupyter_serverproxy_servers': [
            'qgis-websockify = jupyter_remote_qgis_proxy.setup_websockify:setup_websockify',
        ]
    },
    install_requires=[
        'jupyter-server-proxy>=4.1.1',
        'jupyter-remote-desktop-proxy',
    ],
    include_package_data=True,
    keywords=["Interactive", "Desktop", "Jupyter"],
    license="BSD",
    long_description=readme,
    long_description_content_type="text/markdown",
    platforms="Linux",
    python_requires=">=3.8",
    url="https://jupyter.org",
    zip_safe=False,
    data_files=[
        (
            'etc/jupyter/jupyter_server_config.d',
            ['jupyter-config/jupyter_server_config.d/jupyter_remote_qgis_proxy.json'],
        ),
        (
            'etc/jupyter/jupyter_notebook_config.d',
            ['jupyter-config/jupyter_notebook_config.d/jupyter_remote_qgis_proxy.json'],
        ),
        (
            'etc/jupyter/jupyter_remote_qgis_proxy.d',
            [
                'jupyter_remote_qgis_proxy/qgis/scripts/maximize.py',
            ],
        ),
    ],
)
