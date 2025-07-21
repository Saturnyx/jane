from gui import *

if __name__ == "__main__":
    root = tk.Tk()
    MainApplication(root).grid(row=0, column=0, sticky="nsew")
    root.rowconfigure(0, weight=1)
    root.columnconfigure(0, weight=1)
    root.mainloop()
