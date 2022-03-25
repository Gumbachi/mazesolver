"""This module holds functions relative to the Astar algorithm"""

import numpy as np
from pathfinding.node import AstarNode as Node
import queue
from heapq import heappush, heappop
import pathfinding.mapping as mp
from decorators import timer
from math import sqrt


@timer
def astar(arr, start=None, end=None):
    """A* Search Algorithm on a 2D Matrix of ints.

    Args:
        arr (Numpy.ndarry): A 2D Array of int8s
        start (tuple): location to start at
        end (end): location to end at
    """

    # default start and end
    if not start:
        start = (0, 0)
    if not end:
        end = (arr.shape[0]-1, arr.shape[1]-1)

    # get start location
    src = Node(*start)
    goal = Node(*end)

    src.hscore = src.distance_to(goal)

    # make queue and add starting point
    heap = []
    visited = set()
    heappush(heap, src)

    while heap:
        current = heappop(heap)
        visited.add(current.pos)

        if current == goal:
            return (mp.reconstruct_path(src, current), visited)

        # get and add neighbors to queue
        for neighbor in mp.get_neighbors(arr, current, True):
            # Check if node exists and if not create one
            nb = Node.nodes.get(neighbor)
            if not nb:
                neighbor = Node(*neighbor)
            else:
                neighbor = nb

            # checkd if neighbor in visited
            if neighbor.pos in visited:
                continue

            new_gscore = current.gscore + current.distance_to(neighbor)

            # Check if new path is better
            if new_gscore < neighbor.gscore or neighbor not in heap:
                neighbor.gscore = new_gscore
                neighbor.hscore = neighbor.distance_to(goal)
                neighbor.parent = current

                if neighbor not in heap:
                    heappush(heap, neighbor)
    return [], []
