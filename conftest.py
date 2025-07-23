import sys, os

# Insert the src directory into sys.path so `import src…` just works
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
