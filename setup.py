import sys
from setuptools import setup, find_packages

setup(name="meshcat",
    version="0.0.18",
    description="WebGL-based visualizer for 3D geometries and scenes",
    url="https://github.com/rdeits/meshcat-python",
    download_url="https://github.com/rdeits/meshcat-python/archive/v0.0.18.tar.gz",
    author="Robin Deits",
    author_email="mail@robindeits.com",
    license="MIT",
    packages=find_packages("src"),
    package_dir={"": "src"},
    test_suite="meshcat",
    entry_points={
        "console_scripts": [
            "meshcat-server=meshcat.servers.zmqserver:main"
        ]
    },
    install_requires=[
      "ipython >= 5",
      "u-msgpack-python >= 2.4.1",
      "numpy >= 1.14.0" if sys.version_info >= (3, 0) else "numpy >= 1.14.0, < 1.17",
      "tornado >= 4.0.0" if sys.version_info >= (3, 0) else "tornado >= 4.0.0, < 6.0",
      "pyzmq >= 17.0.0"
    ],
    zip_safe=False,
    include_package_data=True
)
