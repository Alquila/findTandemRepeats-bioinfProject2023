import numpy as np
import typing

#NOTE - Potentialy make the children a dictionary, not a list {"a": None, "c": None, "t"; None, "g": None, "n": None, "$": None}
# In the fasta reader this would add some steps
# 1) Make the string in lowercase all the way
# 2) If the string is not represented by the alphabet (a, c, t, g, n) then either make an error or replace with n
# Would this be faster if we translated a,c,t,g,n,$ to 0,1,2,3,4,5? Looking up in the dictionary would look like indexing.

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
    
    def __repr__(self, level=0):
        ret = "\t"*level+repr(self.value)+"\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret


## Make class to handle node. Should be able to handle both internal nodes and leafs
# node should have a: parent, children, 