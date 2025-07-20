import tkinter as tk
import os


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        parent.title("JANE")
        screen_width = parent.winfo_screenwidth()
        screen_height = parent.winfo_screenheight()

        parent.geometry("800x600")
        # TODO: create the rest of your GUI here


if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
