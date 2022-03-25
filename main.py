import tkinter as tk
from tkinter import filedialog


def getmazefilepath():
    """Fetch the filepath for the maze to solve."""
    root = tk.Tk()
    root.wm_attributes('-topmost', True)
    root.withdraw()
    filetypes = [
        ("image", ".jpeg"),
        ("image", ".png"),
        ("image", ".jpg"),
    ]

    return filedialog.askopenfilenames(
        title='Open the maze image',
        filetypes=filetypes,
        initialdir="%USERPROFILE%"
    )


def main():
    """Begin loop"""

    while True:
        print("Select an Image (Q to quit) (Enter to continue) >> ", end="")
        if input().upper() == "Q":
            return

        fp = getmazefilepath()

        if not fp:
            continue

        print(f"PROCESSSING {fp}")


if __name__ == "__main__":
    main()
