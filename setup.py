import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    x = "Win32GUI"

setup(  name = "Sorting Algorithm Visualizer",
        version = "0.1",
        description = "Watch how sorting algorithms work with this python program made in pygame!",
        options = {"build_exe": {"packages": ["pygame", "pygame_widgets"], }},
        executables = [Executable("sorter.py")])