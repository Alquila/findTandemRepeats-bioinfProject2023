# Depth first names all the leaves in their depth-first order
# and creates two dictionaries that map suffix to depth-first
# and vice versa

# string_depth gives each node its string depth

# Each function is an itteration of the implementation
# The final function is full_depth_first_and_array

from math import inf as inf
from node import Node
from collections import deque
#from stoye_gusfield_algorithm import left_rotation

# Create the array
def full_depth_first_and_array_loop(node: Node, testing=False):
    depth_number = 0
    depth_to_suffix = {}
    suffix_to_depth = {}

    # init stack
    stack = deque()
    stack.append(node)
    visited = set()

    while len(stack) > 0:
        current_node = stack.pop()
        #print(current_node)
        if current_node.type == "internal" or current_node.type == "root":
            if current_node.suffix not in visited:
                current_node.depth_first = [inf, -inf]
                stack.append(current_node)
                children = sorted(list(current_node.children.keys()), reverse=True)
                for child in children:
                    child_node = current_node.children.get(child)
                    stack.append(child_node)
                visited.add(current_node.suffix)
               #depth_number += 1
            else:
                current_node.depth_first = [inf, -inf]
                for child in current_node.children:
                    current_node_child = current_node.children[child]
                    new_depth = current_node_child.depth_first
                    if type(new_depth) is list:
                        if new_depth[0] < current_node.depth_first[0]:
                            current_node.depth_first[0] = new_depth[0]
                        if new_depth[1] > current_node.depth_first[1]:
                            current_node.depth_first[1] = new_depth[1]
                    else:
                        if new_depth < current_node.depth_first[0]:
                            current_node.depth_first[0] = new_depth
                        if new_depth > current_node.depth_first[1]:
                            current_node.depth_first[1] = new_depth
                #depth_number -= 1
        elif current_node.type == "leaf":
            # Do leaf stuff
            depth_to_suffix[depth_number] = current_node.suffix
            suffix_to_depth[current_node.suffix] = depth_number
            if testing:
                print("depth_to_leaf[" + str(depth_number) + "] = " + str(current_node.suffix))
                print("leaf_to_depth[" + str(current_node.suffix) + "] = " + str(depth_number))
            current_node.depth_first = [depth_number, depth_number]
            depth_number += 1
    return depth_to_suffix, suffix_to_depth


# Name string depth
def string_depth_loop(node, testing=False):
    # init stack
    stack = deque()
    stack.append(node)

    while len(stack) > 0:
        current_node = stack.popleft()

        if current_node.type == "internal" or current_node.type == "root":
            children = sorted(list(current_node.children.keys()), reverse=True)
            for child in children:
                child_node = current_node.children.get(child)
                stack.append(child_node)

        if current_node.type == "root":
            current_node.string_depth = 0
            continue

        current_node.string_depth = current_node.parent.string_depth + current_node.end - current_node.start + 1
        if testing:
            print("current node : " + repr(current_node.suffix))
            print("current string depth: " + str(current_node.string_depth))
    #print("done with string depth")

# --------------------------------------------------------------------------------------


def basic_stoye_gusfield_loopy(node: Node, depthfirst_to_suffix_list, sequence, testing):
    if testing: 
        print('str(node) = ' + str(node))
        print('df to suff : '+str(depthfirst_to_suffix_list))

    # init stack
    stack = deque()
    stack.append(node)
    visited = set()

    # create empty list for tandem repeats
    tandem_repeat_list = []

    while len(stack) > 0:
        current_node = stack.pop()
        if current_node.children and current_node.suffix not in visited:
            visited.add(current_node.suffix)
            children = sorted(list(current_node.children.keys()), reverse=True)
            for child in children:
                child_node = current_node.children.get(child)
                stack.append(child_node)

        # get suffix/leaf list
        suffix_list = []  # This corresponds to the LL(v) in the slides
        depthfirst_list = current_node.depth_first  # if it is an internal node or the root this is a min-max range
        if current_node.type != "leaf":
            depth_min = depthfirst_list[0]  # the minimum depth for the internal node
            depth_max = depthfirst_list[1]  # the maximum depth for the internal node
            suffix_list = depthfirst_to_suffix_list[depth_min:depth_max+1]
        else:
            continue
        
        for i in suffix_list:
            for j in suffix_list:
                if i < j and j == i + current_node.string_depth and sequence[i] != sequence[
                    i + 2 * current_node.string_depth] and current_node.string_depth > 1:
                    if testing:
                        print('here is i < j and j == i + |a| and S[i] != S[i+2*|a|]')
                        print('i : ' + str(i))
                        print('j : ' + str(j))
                    tandem_repeat = [i, current_node.string_depth]
                    if testing: print('!!!' + str(tandem_repeat))
                    tandem_repeat_list.append(tandem_repeat)
                    if testing: print('the list!!! : ' + str(tandem_repeat_list))

    #if node.children:
    #    for child in node.children.values():
    #        print("goes wrong here maybe basic")
    #        returned_tandem_repeats = basic_stoye_gusfield(child, depthfirst_to_suffix_list, sequence, testing)
    #        if returned_tandem_repeats != None and returned_tandem_repeats != []:
    #            tandem_repeat_list = tandem_repeat_list + returned_tandem_repeats

    #print("before left rotation")
    #tr_lr = left_rotation(tandem_repeat_list, sequence)

    return tandem_repeat_list


def stoye_gusfield_loopy(node: Node, depthfirst_to_suffix_list, sequence, testing):

    # init stack
    stack = deque()
    stack.append(node)
    visited = set()

    # create empty list for tandem repeats
    tandem_repeat_list = []

    while len(stack) > 0:
        current_node = stack.pop()
        if current_node.children and current_node.suffix not in visited:
            visited.add(current_node.suffix)
            children = sorted(list(current_node.children.keys()), reverse=True)
            for child in children:
                child_node = current_node.children.get(child)
                stack.append(child_node)

        # if we are in a leaf there are no tandem repeats to find and no children to call recursively
        if current_node.type == "leaf":
            if testing:
                print('I am a leaf : ' + str(current_node))
            continue

        if testing: print('str(node) = ' + str(current_node))

        # we want to get the large and small leaf list
        # our large-leaf-list placeholders
        large_leaf_list = None
        length_large_leaf_list = 0
        # Now we run through each child to get the leaf lists
        for child in current_node.children.values():
            if testing : print('current child : ' + str(child))
            # if child.type != 'leaf':
            # we use min and max of depth_first to calculate the length of the childs range
            # print('depth_first : ' + str(child.depth_first))
            child_length = (child.depth_first[1] - child.depth_first[0] + 1)
            if child_length >= length_large_leaf_list or large_leaf_list == None:
                large_leaf_list = child.depth_first
                length_large_leaf_list = child_length

        if testing: print(
            'large leaf list : ' + str(large_leaf_list) + '\nlarge leaf length : ' + str(length_large_leaf_list))

        # translate large-leaf-lists to suffix lists
        large_suffix_list = depthfirst_to_suffix_list[large_leaf_list[0]:large_leaf_list[1] + 1]
        if testing:
            print('large suffix list : ' + str(large_suffix_list))
            print(len(large_suffix_list))

        # get full suffix/leaf list
        depth_min = current_node.depth_first[0]  # the minimum depth for the internal node
        depth_max = current_node.depth_first[1]  # the maximum depth for the internal node
        full_suffix_list = depthfirst_to_suffix_list[depth_min:depth_max+1]  # This corresponds to the LL(v) in the slides

        if testing : print('full suffix list : ' + str(full_suffix_list))

        # get small suffix/leaf list
        #small_suffix_list = [x for x in full_suffix_list if x not in large_suffix_list]
        small_suffix_list = [x for x in full_suffix_list if x not in large_suffix_list]
        # for x in full_suffix_list:
        #     #print("x in full index to make small")
        #     if x not in large_suffix_list:
        #         small_suffix_list.append(x)
        if testing : print('small suffix list : ' + str(small_suffix_list))

        if current_node.string_depth > 1:
            for i in small_suffix_list:
                if i + current_node.string_depth in full_suffix_list and sequence[i] != sequence[i + 2 * current_node.string_depth]:
                    tandem_repeat_list.append([i, current_node.string_depth])
                if i - current_node.string_depth in large_suffix_list and sequence[i - current_node.string_depth] != sequence[
                    i + current_node.string_depth]:
                    tandem_repeat_list.append([i - current_node.string_depth, current_node.string_depth])
            if testing: print('tandem repeats list : ' + str(tandem_repeat_list))


    #print("before left rotation")
    #tr_lr = left_rotation(tandem_repeat_list, sequence)

    return tandem_repeat_list
