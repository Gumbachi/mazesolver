import tkinter as tk
from tkinter import filedialog
from pathfinding.bfs import breadth_first_search

from pathfinding.mapping import build_binary_map, draw_path


def getmazefilepath():
    """Fetch the filepath for the maze to solve."""
    root = tk.Tk()
    root.wm_attributes('-topmost', True)
    root.withdraw()
    filetypes = [
        ("image", ".jpeg"),
        ("image", ".png"),
        ("image", ".jpg")
    ]

    return filedialog.askopenfilenames(
        title='Open the maze image',
        filetypes=filetypes,
        initialdir="./"
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

        array = build_binary_map(fp[0])
        path, visited = breadth_first_search(array)
        solution = draw_path(array, path, visited)

        solution.show()
        solution.save("./solved_mazes/solved_maze.png")


if __name__ == "__main__":
    main()
