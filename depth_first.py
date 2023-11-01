from math import inf as inf
from node import Node


# Name depth
def depth_first(node, depth_number=0, testing=False):
    # a list sorted list of the children in the root
    children = sorted(list(node.children.keys()))
    if testing:
        print("Node type: " + str(node.type))
        print("Node children: " + str(children))
    if children:
        for child in children:
            if testing:
                print("Current child: " + str(child))
                print("Current depth: " + str(depth_number))
            current_node = node.children[child]
            current_node.depth = depth_number
            depth_number += 1
            depth_number = depth_first(current_node, depth_number, testing)
    return depth_number


# Name leaves only
def leaves_depth_first(node, depth_number=0, testing=False):
    # a list sorted list of the children in the root
    children = sorted(list(node.children.keys()))
    if testing: print("Current node is a " + str(node.type) + " with " + str(children) + " as their children")
    if children:
        for child in children:
            if testing: print("Current child " + str(child) + " is a " + str(node.children[child].type) + " type")
            current_node = node.children[child]
            if current_node.type == "leaf":
                if testing: print("Giving " + str(child) + " depth number : " + str(depth_number))
                current_node.depth = depth_number
                depth_number += 1
            depth_number = leaves_depth_first(current_node, depth_number, testing)
    return depth_number


# Update min and max internal nodes
def full_depth_first(node: Node, depth_number=0, testing=False):
    children = sorted(list(node.children.keys()))
    if node.type == "internal" or node.type == "root":
        node.depth = [inf, -inf]
        if testing:
            print("In  " + str(node.type))
            print("With children : " + str(children))
            print("Current min,max is : " + str(node.depth))
        for child in children:
            current_node = node.children[child]
            if testing: print("Going to : " + str(child))
            new_number, depth_number = full_depth_first(current_node, depth_number, testing)
            if testing:
                print("Returned : " + str(new_number))
                print("Depth is : " + str(depth_number))
                print("Current min,max is: " + str(node.depth))
            if type(new_number) is list:
                if testing:
                    print("returned a List")
                    print(str(new_number[0]) + ' < ' + str(node.depth[0]) + ' ?')
                if new_number[0] < node.depth[0]:
                    node.depth[0] = new_number[0]
                if testing: print(str(new_number[1]) + ' < ' + str(node.depth[1]) + ' ?')
                if new_number[1] > node.depth[1]:
                    node.depth[1] = new_number[1]
                if testing: print("List: New min,max is: " + str(node.depth))
            else:
                if testing:
                    print("returned a single number")
                    print(str(new_number) + ' < ' + str(node.depth[0]) + ' ?')
                if new_number < node.depth[0]:
                    node.depth[0] = new_number
                if testing: print(str(new_number) + ' > ' + str(node.depth[1]) + ' ?')
                if new_number > node.depth[1]:
                    node.depth[1] = new_number
                if testing: print("Non list: New min,max is: " + str(node.depth))
        return node.depth, depth_number
    if node.type == "leaf":
        if testing:
            print("In type " + str(node.type))
            print("Giving depth number : " + str(depth_number))
        node.depth = depth_number
        depth_number += 1
        return depth_number - 1, depth_number
    return None


# Create the array
def full_depth_first_and_array(Node,depth_to_leaf, leaf_to_depth, depth_number=0, testing=False):
    #depth_to_leaf = {}
    #leaf_to_depth = {}
    children = sorted(list(Node.children.keys()))
    if Node.type == "internal" or Node.type == "root":
        Node.depth = [inf, -inf]
        for child in children:
            current_node = Node.children[child]
            new_number, depth_number = full_depth_first_and_array(current_node, depth_to_leaf, leaf_to_depth, depth_number, testing)
            if type(new_number) is list:
                if new_number[0] < Node.depth[0]:
                    Node.depth[0] = new_number[0]
                if new_number[1] > Node.depth[1]:
                    Node.depth[1] = new_number[1]
            else:
                if new_number < Node.depth[0]:
                    Node.depth[0] = new_number
                if new_number > Node.depth[1]:
                    Node.depth[1] = new_number
        return Node.depth, depth_number
    if Node.type == "leaf":
        depth_to_leaf[depth_number] = Node.suffix
        leaf_to_depth[Node.suffix] = depth_number
        if testing:
            print("depth_to_leaf[" + str(depth_number) + "] = " + str(Node.suffix))
            print("leaf_to_depth[" + str(Node.suffix) + "] = " + str(depth_number))
        Node.depth = depth_number
        depth_number += 1
        return depth_number - 1, depth_number
    return None
