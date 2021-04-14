#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-hubspot",
    version="0.1.0",
    description="Singer.io tap for extracting data",
    author="Stitch",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_hubspot"],
    install_requires=[
        "requests",
        "singer-sdk",
        "singer-tools",
    ],
    entry_points="""
    [console_scripts]
    tap-hubspot=tap_hubspot.tap:cli
    """,
    packages=["tap_hubspot"],
    package_data = {
        "schemas": ["tap_hubspot/schemas/*.json"]
    },
    include_package_data=True,
)
