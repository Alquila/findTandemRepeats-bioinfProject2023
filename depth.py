# Gives each node its' depth

from math import inf as inf
from node import Node


# Name depth
def depth(node, depth_number=0, testing=False):
    if testing:
        print("current depth : " + str(depth_number))
        print("current node : " + str(node.type))
        print("current nodes children : " + str(node.children.keys()))
    node.depth = depth_number
    depth_number += 1
    if node.children:
        for child in node.children:
            current_node = node.children[child]
            depth(current_node, depth_number, testing)
    return None