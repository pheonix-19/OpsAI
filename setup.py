#!/usr/bin/env python3
"""
Setup Configuration for OpsAI
Package installation and dependency management for the AI operations platform.

Author: Ayush
GitHub: https://github.com/pheonix-19
Copyright (c) 2025
"""
# setup.py
from setuptools import setup, find_packages

setup(
    name='opsai',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)
