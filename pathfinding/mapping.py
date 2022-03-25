"""Module containing functions that all of the algorithms make use of."""

from PIL import Image
import numpy as np
from os.path import sep


def build_binary_map(path):
    """Builds a numpy array of 1s and 0s illustrating the map."""
    img = Image.open(path)
    return np.array(img)


def reconstruct_path(start, end):
    """Reconstruct path from start to end."""
    path = []
    current = end
    while current.parent:
        path.append(current)
        current = current.parent
    path.append(current)

    if path[-1] == start:
        return path[::-1]  # Reverse the path
    else:
        return []


def get_neighbors(array, current, diagonals=True):
    """Generator that yields all neighbors of a node."""
    poschanges = [(0, 1), (0, -1), (1, 0), (-1, 0),
                  (1, 1), (1, -1), (-1, 1), (-1, -1)]

    # add diagonals if specified
    if not diagonals:
        poschanges = poschanges[:4]

    width, height, _ = array.shape

    neighbors = []

    for poschange in poschanges:
        neighbor = (current.row + poschange[0], current.col + poschange[1])

        # check if in bounds
        if not (0 <= neighbor[0] < width and 0 <= neighbor[1] < height):
            continue

        # check for walls
        if np.any(array[neighbor]):
            neighbors.append(neighbor)

    return neighbors


def draw_path(array, path, visited=None):
    """Draw visited nodes and the path and display maze"""
    if visited:
        for pos in visited:
            array[pos] = np.array([255, 0, 0])

    for node in path:
        array[node.pos] = np.array([0, 255, 0])

    img = Image.fromarray(array)

    return img
