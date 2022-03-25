"""Contains functions related to Breadth-First-Search"""


import numpy as np
from pathfinding.node import Node
import queue
import pathfinding.mapping as mp
from collections import defaultdict


def breadth_first_search(arr, start=None, end=None):
    """Breadth-First-Search Algorithm on a 2D Grid.

    Args:
        arr (Numpy.ndarry): A 2D Array of int8s
        start (tuple): The start pixel
        end (tuple): The end pixel
    """
    start = (0, 0) if not start else start
    end = (arr.shape[0]-1, arr.shape[1]-1) if not end else end

    # get start location
    src = Node(*start)

    # make queue and add starting point
    q = queue.Queue()
    q.put(src)

    # dict to store booleans of visited locationsS
    visited = defaultdict(bool)
    visited[src.pos] = True

    while not q.empty():
        current = q.get()

        # check if complete
        if current == end:
            return mp.reconstruct_path(src, current), visited

        # get and add neighbors to queue
        for neighbor in mp.get_neighbors(arr, current, True):
            # check if visited
            if visited[neighbor]:
                continue

            q.put(Node(*neighbor, current))
            visited[neighbor] = True

    return [], []
