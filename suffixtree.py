import numpy as np
import typing
from node import Node


#NOTE - change name to suffixtree_naive.py?

class NaiveSuffixTree():
    """
    Builds a Naive Suffix Tree
    """

    def __init__(self, sequence):
        self.sequence = sequence

    def buildTree(self):
        # Add root to tree
        Tree = Node("root", children=[])

        # Build tree
        current_node = Tree
        leaf_number = 0
        len_seq = len(self.sequence)
        for i in range(len_seq):
            if current_node.children != []:
                for child in current_node.children:
                    res_idx = traverseTree(i, child.startIndex, child.end_idx)
                    if res_idx == -1:
                        # go to Child
                        current_node = child
                        ## continue traverse and/or insert node
                    elif res_idx > 0:
                        # insert new node
                        new_internal_node = Node(name="internal",
                                                 start_idx=(current_node.end_idx + 1),
                                                 end_idx=(current_node.end_idx + res_idx),
                                                 parent=current_node,
                                                 children=child)
                        current_node.children.remove(child)
                        current_node.children.append(new_internal_node)
                        child.start_idx = new_internal_node.end_idx + 1
                        child.parent = new_internal_node
                        # Insert new leaf node
                        new_leaf_node = Node(name = leaf_number,
                                             start_idx = new_internal_node.end_idx + 1,
                                             end_idx = len_seq,
                                             parent = new_internal_node)
                        leaf_number += 1
                        new_internal_node.children.append(new_leaf_node)

            elif current_node.name == "root":
                new_node = Node(leaf_number, i, (len_seq - 1), parent=current_node)
                current_node.children.append(new_node)
                leaf_number += 1

    def traverseTree(self, suffix_idx, elem_idx, elem_end, res=0):
        if suffix_idx == elem_end:
            return -1
        elif self.sequence[suffix_idx] != self.sequence[elem_idx]:
            return res
        else:
            return traverseTree(suffix_idx + 1, elem_idx + 1, res + 1, elem_end)
