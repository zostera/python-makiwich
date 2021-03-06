#!/usr/bin/env python

import os
import sys
import re

from setuptools import setup

# get version without importing
with open("maki/__init__.py", "rb") as f:
    VERSION = str(re.search('__version__ = "(.+?)"', f.read().decode("utf-8")).group(1))

package_name = "python-makiwich"

if sys.argv[-1] == "publish":
    os.system("python setup.py sdist")
    os.system("twine upload -r pypi dist/%s-%s.tar.gz" % (package_name, VERSION))
    sys.exit()

if sys.argv[-1] == "tag":
    os.system("git tag -a v{} -m 'tagging v{}'".format(VERSION, VERSION))
    os.system("git push && git push --tags")
    sys.exit()


setup(
    name=package_name,
    version=VERSION,
    description="Create markers with maki icons for leaflet",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/zostera/python-makiwich",
    author="Jan Pieter Waagmeester",
    author_email="jieter@zostera.nl",
    license="ISC",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
    keywords="Maki icon markers",
    packages=["maki", "maki.contrib"],
    install_requires=["xmltodict"],
    include_package_data=True,
    package_data={"maki": ["maki/img/*.svg", "maki/img/icons/*.svg"]},
)
