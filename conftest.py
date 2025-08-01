#!/usr/bin/env python3
"""
Pytest Configuration for OpsAI
Test configuration and path setup for the AI operations platform.

Author: Ayush
GitHub: https://github.com/pheonix-19
Copyright (c) 2025
"""
import sys, os

# Insert the src directory into sys.path so `import src…` just works
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
