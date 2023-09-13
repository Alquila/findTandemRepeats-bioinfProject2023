import numpy as np
import typing

class Node():
    def __init__(self, name, depth = 0, startInd = None, endInd = None, 
                 parent = None, children = None):
        self.name = name
        self.depth = depth
        self.parent = parent
        self.children = children
        self.startInd = startInd
        self.endInd = endInd

    def __str__(self):
        return f"{self.name}({self.depth})"



## Make class to handle node. Should be able to handle both internal nodes and leafs
# node should have a: parent, children, 