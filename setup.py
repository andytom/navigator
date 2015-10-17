from setuptools import setup, find_packages
import codecs
import os
import re


here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    # intentionally *not* adding an encoding option to open
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name="Navigator",
    version=find_version('navigator','__init__.py'),
    author="Thomas O'Donnell",
    author_email="",
    license="BSD 3-Clause License",
    url="https://github.com/Andytom/navigator",
    packages=find_packages(),
    description="A framework to create simple, interactive command line tools.",
    long_description=read("README.rst"),
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ),
    install_requires=["six"],
    tests_require=["mock"]
)
