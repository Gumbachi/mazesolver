"""Module with Nodes that are used for the algorithms."""


class Node:
    """Node base class with basic functions"""

    def __init__(self, row, col, parent=None):
        """inits a node containing position and parent."""
        self.row = row
        self.col = col
        self.parent = parent

    @property
    def pos(self):
        """Return the position tuple."""
        return (self.row, self.col)

    def __repr__(self):
        """Debug printing"""
        return f"{(self.row, self.col)}"

    def __eq__(self, other):
        """Comparing two nodes together."""
        if isinstance(other, tuple):
            return self.row == other[0] and self.col == other[1]
        return self.row == other.row and self.col == other.col

    def distance_to(self, node):
        """Calculate the distance from the goal using diagonal distance."""
        dx = abs(self.col - node.col)
        dy = abs(self.row - node.row)
        return 10 * (dx + dy) - 6 * min(dx, dy)


class AstarNode(Node):
    """Node designed to be used by the A* pathfinding algo."""

    nodes = {}

    def __init__(self, row, col, parent=None):
        """inits position values and adds to a storage dictionary"""
        super().__init__(row, col, parent)
        self.gscore = 0
        self.hscore = 0
        self.nodes[self.pos] = self

    @property
    def fscore(self):
        """Calculate fscore."""
        return self.gscore + self.hscore

    def __lt__(self, other):
        """Compare f scores and h scores."""
        if self.fscore == other.fscore:
            return self.hscore < other.hscore
        return self.fscore < other.fscore
