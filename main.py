import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


def getmazefilepath():
    filetypes = (
        ('JPEG', '*.jpg'),
        ('PNG', '*.png')
    )

    return filedialog.askopenfilename(
        title='Open a file',
        filetypes=filetypes
    )


def main():
    """Initialize TK and begin loop"""
    window = tk.Tk()
    window.title("Maze Solver")
    window.geometry("500x500")
    frm = ttk.Frame(window, padding=10)
    frm.grid()
    ttk.Label(frm, text="Select an unsolved maze").grid(column=0, row=0)
    ttk.Button(frm, command=getmazefilepath, text="Open").grid(column=1, row=0)
    window.mainloop()


if __name__ == "__main__":
    main()
