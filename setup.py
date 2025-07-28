from distutils.core import setup
import py2exe
import sys
import os
import shutil

# Ensure py2exe is a command-line argument
if "py2exe" not in sys.argv:
    sys.argv.append("py2exe")

APP_NAME = "JANE"
VERSION = "1.0"
DESCRIPTION = "JANE - A simple Python Tkinter editor for Windows XP (Python 3.4)"
AUTHOR = "Saturnyx"
ICON_PATH = os.path.join("assets", "icon.ico")

# Data files to include (assets, data)
data_files = [
    ("assets", [os.path.join("assets", "icon.ico")]),
    (
        "data",
        [os.path.join("data", "settings.json"), os.path.join("data", "theme.json")],
    ),
    # gui.py and settings.py are now included as part of the src package
]

MAIN_SCRIPT = os.path.join("src", "main.py")

setup(
    name=APP_NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    windows=[
        {
            "script": MAIN_SCRIPT,
            "icon_resources": [(0, ICON_PATH)],
        }
    ],
    options={
        "py2exe": {
            "includes": [
                "tkinter",
                "tkinter.messagebox",
                "tkinter.filedialog",
                "tkinter.ttk",
                "json",
                "pygments",
                "pygments.lexers.python",
                "pygments.token",
                "src.gui",
                "src.settings",
            ],
            "bundle_files": 3,
            "compressed": True,
            "optimize": 2,
            "dll_excludes": [
                "MSVCP90.dll",
            ],
            "packages": ["src"],
        }
    },
    data_files=data_files,
    zipfile=None,
)
# if os.path.exists("dist/assets"):
#     shutil.rmtree("dist/assets")
# if os.path.exists("assets"):
#     shutil.copytree("assets", "dist/assets")
# if os.path.exists("dist/data"):
#     shutil.rmtree("dist/data")
# if os.path.exists("data"):
#     shutil.copytree("data", "dist/data")
# # Post-build: copy gui.py and settings.py from src to dist
# import glob

# for fname in ["gui.py", "settings.py"]:
#     src_path = os.path.join("src", fname)
#     dst_path = os.path.join("dist", fname)
#     if os.path.exists(src_path):
#         shutil.copy2(src_path, dst_path)
