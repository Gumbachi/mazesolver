import unittest
from pathfinding.bfs import breadth_first_search
from pathfinding.mapping import get_neighbors, reconstruct_path
from pathfinding.node import Node
import numpy as np


class Tests(unittest.TestCase):

    def test_get_neighbors(self):
        array = np.array([
            [[0, 0, 0], [255, 255, 255], [0, 0, 0]],
            [[255, 255, 255], [255, 255, 255], [0, 0, 0]],
            [[0, 0, 0], [255, 255, 255], [255, 255, 255]]
        ])

        expected = [(0, 1), (1, 0), (2, 1), (2, 2)]
        actual = get_neighbors(array, Node(1, 1))

        self.assertCountEqual(expected, actual)

    def test_reconstruct_path(self):

        start = Node(0, 0)
        n1 = Node(0, 1, start)
        n2 = Node(1, 1, n1)
        n3 = Node(2, 1, n2)
        end = Node(2, 2, n3)

        expected = [start, n1, n2, n3, end]

        actual = reconstruct_path(start, end)
        self.assertListEqual(expected, actual)

    def test_bfs(self):
        array = np.array([
            [[255, 255, 255], [255, 255, 255], [0, 0, 0]],
            [[0, 0, 0], [255, 255, 255], [0, 0, 0]],
            [[0, 0, 0], [255, 255, 255], [255, 255, 255]]
        ])

        expected = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 2)]
        actual, _ = breadth_first_search(array)

        self.assertListEqual(expected, actual)

    def test_dfs(self):
        """TODO test Depth-First-Search."""
        assert True == False
