# Name depth
def depth_first(Node, depth_number = 0, testing=False):
    # a list sorted list of the children in the root
    children = sorted(list(Node.children.keys()))
    if testing: print("Node type: " + str(Node.type))
    if testing: print("Node children: " + str(children))
    if children:
        for child in children:
            if testing: print("Current child: " + str(child))
            current_node = Node.children[child]
            if testing: print("Current depth: " + str(depth_number))
            current_node.depth = depth_number
            depth_number += 1
            depth_number = depth_first(current_node, depth_number, testing)
    return depth_number

# Name leaves only
def leaves_depth_first(Node, depth_number = 0, testing=False):
    # a list sorted list of the children in the root
    children = sorted(list(Node.children.keys()))
    if testing: print("Node type: " + str(Node.type))
    if testing: print("Node children: " + str(children))
    if children:
        for child in children:
            if testing: print("Current child: " + str(child))
            current_node = Node.children[child]
            if testing: print("Current depth: " + str(depth_number))
            if current_node.type == "leaf":
                current_node.depth = depth_number
                depth_number += 1
            depth_number = depth_first(current_node, depth_number, testing)
    return depth_number


# Update min and max internal nodes



# Create the array



