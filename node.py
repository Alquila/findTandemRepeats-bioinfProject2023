import numpy as np
import typing

class Node():
    def __init__(self, name, depth = 0, start_idx = 0, end_idx = None,
                 parent = None, children = None):
        self.name = name
        self.depth = depth
        self.parent = parent
        self.children = children
        self.start_idx = start_idx
        self.end_idx = end_idx

    def __str__(self):
        return f"{self.name}({self.depth})"


## Make class to handle node. Should be able to handle both internal nodes and leafs
# node should have a: parent, children, 