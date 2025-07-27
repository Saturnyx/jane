from distutils.core import setup
import py2exe
import sys
import os
import shutil

sys.path.insert(0, os.path.abspath("src"))


class PostBuildCommand:
    def run(self):
        if os.path.exists("dist/assets"):
            shutil.rmtree("dist/assets")
        shutil.copytree("assets", "dist/assets")


setup(
    windows=[{"script": "src/main.py", "icon_resources": [(1, "assets/icon.ico")]}],
    options={
        "py2exe": {
            "includes": ["tkinter", "gui"],
            "bundle_files": 3,
            "compressed": True,
        }
    },
    zipfile=None,
    cmdclass={"build_exe": PostBuildCommand},
)
