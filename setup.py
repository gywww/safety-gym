#!/usr/bin/env python

from setuptools import setup
import sys

assert sys.version_info.major == 3 and sys.version_info.minor >= 6, \
    "Safety Gym is designed to work with Python 3.6 and greater. " \
    + "Please install it before proceeding."

setup(
    name='safety_gym',
    packages=['safety_gym'],
    install_requires=[
        'gym',             # 去掉版本号
        'joblib',          # (可选) 建议也去掉，以防万一
        'mujoco_py',       # (可选) 如果你有特定版本需求就不动它
        'numpy',           # 去掉版本号！这是最关键的
        'xmltodict',
    ],
)
