import numpy as np
import typing
from node import Node


class NaiveSuffixTree():
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
                for j in current_node.children:
                    traverseTree()
            elif current_node.name == "root":
                new_node = Node(leaf_number, 1, i, (len_seq - 1), parent=current_node)
                current_node.children.append(new_node);
                leaf_number += 1;

    def traverseTree(self, suffix_idx, node_idx, res):
        if self.sequence[suffix_idx] != self.sequence[node_idx]:
            return res
        else:
            return traverseTree(suffix_idx + 1, node_idx + 1, res + 1)
