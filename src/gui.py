import tkinter as tk
import os
import settings

ASSETS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")
ICON_PATH = os.path.join(ASSETS_DIR, "icon.ico")


class MainApplication(tk.Frame):
    def __init__(self, parent, config=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.config = config or settings.load()
        self.set_window()
        self.set_icon()
        # ...rest of GUI setup...

    def set_window(self):
        win_cfg = self.config.get("windows", {}).get("main", {})
        width = win_cfg.get("width", 800)
        height = win_cfg.get("height", 600)
        x = win_cfg.get("x", 0)
        y = win_cfg.get("y", 0)
        self.parent.title("JANE")
        screen_width = self.parent.winfo_screenwidth()
        screen_height = self.parent.winfo_screenheight()
        pos_x = int(screen_width / 2 - width / 2 + x)
        pos_y = int(screen_height / 2 - height / 2 + y)
        self.parent.geometry("{}x{}+{}+{}".format(width, height, pos_x, pos_y))

    def set_icon(self):
        if os.path.exists(ICON_PATH):
            try:
                self.parent.iconbitmap(ICON_PATH)
            except Exception as e:
                print("[ERR] Could not set window icon: {}".format(e), flush=True)
        else:
            print("[ERR] Icon file not found at {}".format(ICON_PATH), flush=True)
