import numpy as np
import typing
from node import Node


## TODO make new node function

class NaiveSuffixTree:
    """ Builds a Naive Suffix Tree
    """

    def __init__(self, sequence):
        self.sequence = sequence

    def buildTree(self):
        # Add root to tree
        Tree = Node("root", 0, children=[])

        # Build tree
        current_node = Tree
        leaf_number = 0
        len_seq = len(self.sequence)
        for i in range(len_seq):
            if current_node.children != []:
                for child in current_node.children:
                    res_idx = traverseTree(i, child.startIndex)
                    if res_idx == -1:
                        # go to Child
                        current_node = child
                        ## continue traverse and/or insert node
                    elif res_idx > 0:
                        # insert new node
                        new_internal_node = Node(name="internal", depth=(current_node.depth + 1),
                                                 start_idx=(current_node.end_idx + 1),
                                                 end_idx=(current_node.end_idx + res_idx), parent=current_node,
                                                 children=child)
                        current_node.children.remove(child)
                        current_node.children.append(new_node)
                        leaf_number += 1
                        ## Create new child note and change start index of existing child node

            elif current_node.name == "root":
                new_node = Node(leaf_number, 1, i, (len_seq - 1), parent=current_node)
                current_node.children.append(new_node)
                leaf_number += 1

    def traverseTree(self, suffix_idx, elem_idx, res=0):
        if self.sequence[suffix_idx] != self.sequence[elem_idx]:
            return res
        else:
            return traverseTree(suffix_idx + 1, elem_idx + 1, res + 1)
