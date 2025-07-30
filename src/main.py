import sys
import sys
import sys
import os

try:
    from src.gui import *
except ImportError:
    try:
        base_dir = os.path.abspath(os.path.dirname(__file__))
    except NameError:
        base_dir = os.path.abspath(os.path.dirname(sys.argv[0]))  # type: ignore
    sys.path.insert(0, base_dir)
    from src.gui import *
except:
    from gui import *

if __name__ == "__main__":
    root = tk.Tk()  # type: ignore
    MainApplication(root).grid(row=0, column=0, sticky="nsew")  # type: ignore
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    root.mainloop()
