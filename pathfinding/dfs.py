"""Contains functions related to depth-first search algorithm."""

import numpy as np
from pathfinding.node import Node
import queue
import pathfinding.mapping as mp


def depth_first_search(arr, start=None, end=None):
    """Depth-First-Search Algorithm on a 2D Matrix of ints

    Args:
        arr (Numpy.ndarry): A 3D Array of positions with color lists
        start (tuple): Position to start at
        end (tuple): Position to end at
    """
    if not start:
        start = (0, 0)
    if not end:
        end = (arr.shape[0]-1, arr.shape[1]-1)

    # get start location
    src = Node(*start)

    # make queue and add starting point
    stack = queue.LifoQueue()
    stack.put(src)

    # 2d array for storing booleans for visited
    visited = set()
    visited.add(src.pos)

    while not stack.empty():
        current = stack.get()

        # check if complete
        if current.pos == end:
            return mp.reconstruct_path(src, current), visited

        # get and add neighbors to queue
        for neighbor in mp.get_neighbors(arr, current, True):
            # check if visited
            if neighbor in visited:
                continue

            stack.put(Node(*neighbor, current))
            visited.add(neighbor)
    return [], []
