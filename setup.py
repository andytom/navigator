from distutils.core import setup

setup(
    name="Navigator",
    version="0.0.1",
    author="Thomas O'Donnell",
    author_email="",
    url="",
    packages=["navigator"],
    long_description=open("README.md").read(),
    install_requires=[
        "six == 1.3.0"
    ]
)
