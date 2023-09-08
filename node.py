import numpy as np
import typing
from abc import ABC #Abstract Base Classes

class Node:
    def __init__(self, name, startInd, endInd, depth = 0, parent = None):
        self.name = name
        self.startInd = startInd
        self.endInd = endInd
        self.parent = parent
        self.depth = depth

    def __str__(self):
        return f"{self.name}({self.depth})"
    
    def myfunc(self):
        print("Hello my name is " + self.name)

## Make class to handle node. Should be able to handle both internal nodes and leafs
# node should have a: parent, children, 