import tkinter as tk
from tkinter import messagebox, filedialog
import tkinter.ttk as ttk
import os
import settings
import ctypes

ASSETS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "assets")
ICON_PATH = os.path.join(ASSETS_DIR, "icon.ico")
FILE_PATH =  ""


class MainApplication(tk.Frame):
    def __init__(self, parent, config=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.config = config or settings.load()
        self.theme = settings.theme()
        self.set_dpi()
        self.set_window()
        self.set_icon()
        self.toolbar()
        self.text_widget = self.editor()

    def set_dpi(self):
        if hasattr(ctypes, "windll"):
            try:
                ctypes.windll.shcore.SetProcessDpiAwareness(1)
            except Exception as e:
                try:
                    ctypes.windll.user32.SetProcessDPIAware()
                except Exception as e:
                    print("[ERR] Could not set DPI awareness: {}".format(e), flush=True)

    def set_window(self):
        self.parent.title("JANE")
        width = self.config["windows"]["main"]["width"]
        height = self.config["windows"]["main"]["height"]
        x = self.config["windows"]["main"]["x"]
        y = self.config["windows"]["main"]["y"]
        screen_width = self.parent.winfo_screenwidth()
        screen_height = self.parent.winfo_screenheight()
        pos_x = int((screen_width - width) / 2)
        pos_y = int((screen_height - height) / 2)
        self.parent.geometry("{}x{}+{}+{}".format(width, height, pos_x, pos_y))

    def set_icon(self):
        if os.path.exists(ICON_PATH):
            try:
                self.parent.iconbitmap(ICON_PATH)
            except Exception as e:
                print("[ERR] Could not set window icon: {}".format(e), flush=True)
        else:
            print("[ERR] Icon file not found at {}".format(ICON_PATH), flush=True)

    def toolbar(self):
        def open_file():
            global FILE_PATH
            FILE_PATH = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
            if FILE_PATH:
                with open(FILE_PATH, "r", encoding="utf-8") as f:
                    self.text_widget.delete("1.0", tk.END)
                    self.text_widget.insert(tk.END, f.read())
                self.parent.title("JANE - {}".format(os.path.basename(FILE_PATH)))

        def save_file():
            global FILE_PATH
            if FILE_PATH != "":
                with open(FILE_PATH, "w", encoding="utf-8") as f:
                    f.write(self.text_widget.get("1.0", tk.END))
            elif FILE_PATH:
                with open(FILE_PATH, "w", encoding="utf-8") as f:
                    f.write(self.text_widget.get("1.0", tk.END))
            else:
                FILE_PATH = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
                self.parent.title("JANE - {}".format(os.path.basename(FILE_PATH)))
        
        def action_close():
            self.parent.quit()

        def info():
            dialog = tk.Toplevel(self.parent)
            dialog.title("About JANE")
            dialog.transient(self.parent)
            dialog.grab_set()
            dialog.resizable(False, False)
            dialog.iconbitmap(ICON_PATH)
            dialog.configure(bg=self.theme["colors"]["background"])

            title = tk.Label(
                dialog,
                text="JANE",
                font=(
                    self.theme["fonts"]["ui-heading"],
                    self.theme["fonts"]["ui-heading-size"],
                    "bold",
                ),
                fg=self.theme["colors"]["text"],
                bg=self.theme["colors"]["background"],
            )
            title.pack(padx=24, pady=(24, 0))

            text = tk.Label(
                dialog,
                text="Just Another Notepad Editor\n\nS.Harshal\nVersion 0.1.0\nMIT License",
                font=("Segoe UI", 12),
                fg=self.theme["colors"]["text"],
                bg=self.theme["colors"]["background"],
            )
            text.pack(padx=24, pady=(0, 12))

            btn = tk.Button(
                dialog,
                text="OK",
                font=(
                    self.theme["fonts"]["ui-text"],
                    self.theme["fonts"]["ui-text-size"],
                ),
                width=10,
                relief="ridge",
                command=dialog.destroy,
                bg=self.theme["colors"]["button"],
                fg=self.theme["colors"]["text"],
                activebackground=self.theme["colors"]["accent"],
                activeforeground=self.theme["colors"]["text"],
            )
            btn.pack(pady=(0, 20))

            dialog.update_idletasks()
            x = (
                self.parent.winfo_x()
                + (self.parent.winfo_width() - dialog.winfo_width()) // 2
            )
            y = (
                self.parent.winfo_y()
                + (self.parent.winfo_height() - dialog.winfo_height()) // 2
            )
            dialog.geometry("+{}+{}".format(x, y))

        menu_font = (
            self.theme["fonts"]["ui-text"],
            self.theme["fonts"]["ui-text-size"],
        )
        menubar = tk.Menu(
            self.parent,
            font=menu_font,
            background=self.theme["colors"]["background"],
            foreground=self.theme["colors"]["text"],
            activebackground=self.theme["colors"]["accent"],
            activeforeground=self.theme["colors"]["text"],
            borderwidth=self.config["windows"]["main"]["border-width"],
        )
        file_menu = tk.Menu(
            menubar,
            tearoff=0,
            font=menu_font,
            background=self.theme["colors"]["background"],
            foreground=self.theme["colors"]["text"],
            activebackground=self.theme["colors"]["accent"],
            activeforeground=self.theme["colors"]["text"],
            borderwidth=self.config["windows"]["main"]["border-width"],
        )
        file_menu.add_command(label="Open", command=open_file)
        file_menu.add_command(label="Save", command=save_file)
        file_menu.add_separator()
        file_menu.add_command(label="About", command=info)
        file_menu.add_command(label="Close", command=action_close)
        menubar.add_cascade(label="File", menu=file_menu)
        self.parent.config(menu=menubar)

        self.parent.bind('<Control-s>', lambda event: save_file())
        self.parent.bind('<Control-o>', lambda event: open_file()) 
        self.parent.bind('<Control-q>', lambda event: action_close())
        self.parent.bind('<Control-h>', lambda event: info())


        return menubar

    def editor(self):
        editor_frame = tk.Frame(self.parent, bg=self.theme["colors"]["background"])
        editor_frame.grid(row=0, column=0, sticky="nsew")
        self.parent.rowconfigure(0, weight=1)
        self.parent.columnconfigure(0, weight=1)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "Custom.Vertical.TScrollbar",
            gripcount=0,
            background=self.theme["colors"]["scrollbar-background"],
            troughcolor=self.theme["colors"]["scrollbar-trough"],
            bordercolor=self.theme["colors"]["scrollbar-border"],
            arrowcolor=self.theme["colors"]["scrollbar-arrow"],
            relief="flat",
            width=self.config["windows"]["main"]["scrollbar-width"],
            activerelief="groove",
            lightcolor=self.theme["colors"]["scrollbar-highlight"],
            darkcolor=self.theme["colors"]["scrollbar-shadow"],
            foreground=self.theme["colors"]["scrollbar-active-arrow"],
            disabledbackground=self.theme["colors"]["scrollbar-disabled-background"],
            disabledforeground=self.theme["colors"]["scrollbar-disabled-arrow"],
            hoverbackground=self.theme["colors"]["scrollbar-hover"],
        )
        style.configure(
            "Custom.Horizontal.TScrollbar",
            gripcount=0,
            background=self.theme["colors"]["scrollbar-background"],
            troughcolor=self.theme["colors"]["scrollbar-trough"],
            bordercolor=self.theme["colors"]["scrollbar-border"],
            arrowcolor=self.theme["colors"]["scrollbar-arrow"],
            relief="flat",
            width=self.config["windows"]["main"]["scrollbar-width"],
            activerelief="groove",
            lightcolor=self.theme["colors"]["scrollbar-highlight"],
            darkcolor=self.theme["colors"]["scrollbar-shadow"],
            foreground=self.theme["colors"]["scrollbar-active-arrow"],
            disabledbackground=self.theme["colors"]["scrollbar-disabled-background"],
            disabledforeground=self.theme["colors"]["scrollbar-disabled-arrow"],
            hoverbackground=self.theme["colors"]["scrollbar-hover"],
        )

        text_widget = tk.Text(
            editor_frame,
            wrap=tk.NONE,
            font=(
                self.theme["fonts"]["editor-text"],
                self.theme["fonts"]["editor-text-size"],
            ),
            bg=self.theme["colors"]["background"],
            fg=self.theme["colors"]["text"],
            insertbackground=self.theme["colors"].get(
                "caret", self.theme["colors"]["text"]
            ),
            selectbackground=self.theme["colors"]["selection-background"],
            selectforeground=self.theme["colors"]["selection-text"],
            undo=True,
            borderwidth=0,
            relief="flat",
            padx=self.config["windows"]["main"]["padding-x"],
            pady=self.config["windows"]["main"]["padding-y"],
            blockcursor=True,
        )

        y_scroll = ttk.Scrollbar(
            editor_frame,
            orient=tk.VERTICAL,
            style="Custom.Vertical.TScrollbar",
            command=text_widget.yview,
        )
        x_scroll = ttk.Scrollbar(
            editor_frame,
            orient=tk.HORIZONTAL,
            style="Custom.Horizontal.TScrollbar",
            command=text_widget.xview,
        )

        text_widget["yscrollcommand"] = y_scroll.set
        text_widget["xscrollcommand"] = x_scroll.set

        text_widget.grid(row=0, column=0, sticky="nsew")
        y_scroll.grid(row=0, column=1, sticky="ns")
        x_scroll.grid(row=1, column=0, sticky="ew")

        editor_frame.rowconfigure(0, weight=1)
        editor_frame.columnconfigure(0, weight=1)

        text_widget.focus_set()

        return text_widget
