from distutils.core import setup
import py2exe
import sys
import os
import shutil

if "py2exe" not in sys.argv:
    sys.argv.append("py2exe")

APP_NAME = "JANE"
VERSION = "1.2.1"
DESCRIPTION = "JANE - A simple Python Tkinter editor for Windows XP (Python 3.4)"
AUTHOR = "Saturnyx"
ICON_PATH = os.path.join("assets", "icon.ico")

data_files = [
    ("assets", [os.path.join("assets", "icon.ico")]),
    (
        "data",
        [os.path.join("data", "settings.json"), os.path.join("data", "theme.json")],
    ),
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
                "pygments.lexers.c_cpp",
                "pygments.lexers.jvm",
                "pygments.lexers.markup",
                "pygments.lexers.math",
                "pygments.lexers.scripting",
                "pygments.lexers.configs",
                "pygments.lexers.data",
                "pygments.lexers.dotnet",
                "pygments.lexers.agile",
                "pygments.lexers.asm",
                "pygments.lexers.business",
                "pygments.lexers.compiled",
                "pygments.lexers.functional",
                "pygments.lexers.other",
                "pygments.lexers.parsers",
                "pygments.lexers.prolog",
                "pygments.lexers.templates",
                "pygments.lexers.textedit",
                "pygments.lexers.web",
                "pygments.lexers.math",
                "pygments.lexers.special",
                "pygments.lexers.dsls",
                "pygments.lexers.rebol",
                "pygments.lexers.sql",
                "pygments.lexers.shell",
                "pygments.lexers._mapping",
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
