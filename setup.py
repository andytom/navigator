from distutils.core import setup

import navigator


setup(
    name="Navigator",
    version=navigator.__version__,
    author="Thomas O'Donnell",
    author_email="",
    url="https://github.com/Andytom/navigator",
    packages=["navigator"],
    long_description=open("README.rst").read(),
    install_requires=[
        "six == 1.3.0"
    ]
)
