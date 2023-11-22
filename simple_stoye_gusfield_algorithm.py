from suffixtree import NaiveSuffixTree
from node import Node

def basic_stoye_gusfield(node: Node, depthfirst_to_suffix, sequence, testing):
    if testing: print('str(node) = ' + str(node))

    # create empty list for tandem repeats
    tandem_repeat_list = []

    # get suffix/leaf list
    suffix_list = [] # This corresponds to the LL(v) in the slides
    depthfirst_list = node.depth_first # if it is an internal node or the root this is a min-max range
    if node.type != "leaf":
        depth_min = depthfirst_list[0] # the minimum depth for the internal node
        depth_max = depthfirst_list[1] # the maximum depth for the internal node
        for index in range(depth_min, depth_max+1):
            suffix_list.append(depthfirst_to_suffix[index])
    else:
        return
    
    for i in suffix_list:
        for j in suffix_list:
            if i < j and j == i + node.string_depth and sequence[i] != sequence[i + 2 * node.string_depth] and node.string_depth > 1:
                if testing:
                    print('here is i < j and j == i + |a| and S[i] != S[i+2*|a|]')
                    print('i : ' + str(i))
                    print('j : ' + str(j))
                tandem_repeat = [i, node.string_depth]
                if testing: print('!!!' + str(tandem_repeat))
                tandem_repeat_list.append(tandem_repeat)
                if testing: print('the list!!! : ' + str(tandem_repeat_list))

    if node.children:
        for child in node.children.values():
            returned_tandem_repeats = basic_stoye_gusfield(child, depthfirst_to_suffix, sequence, testing)
            if returned_tandem_repeats != None and returned_tandem_repeats != []:
                tandem_repeat_list = tandem_repeat_list + returned_tandem_repeats

    return tandem_repeat_list





def stoye_gusfield(node: Node, depthfirst_to_suffix, sequence, testing):

    # if we are in a leaf there are no tandem repeats to find and no children to call recursively
    if node.type == "leaf":
        if testing: print('I am a leaf : ' + str(node))
        return
    
    if testing: print('str(node) = ' + str(node))

    # create empty list for tandem repeats
    tandem_repeat_list = []

    # we want to get the large and small leaf list
    # our large-leaf-list placeholders
    large_leaf_list = None
    length_large_leaf_list = 0
    # Now we run through each child to get the leaf lists
    for child in node.children.values():
        # if child.type != 'leaf':
        # we use min and max of depth_first to calculate the length of the childs range
        #print('depth_first : ' + str(child.depth_first))
        child_length = (child.depth_first[1] - child.depth_first[0] + 1)
        if child_length >= length_large_leaf_list or large_leaf_list == None:
            large_leaf_list = child.depth_first
            length_large_leaf_list = child_length

    if testing: print('large leaf list : ' + str(large_leaf_list) + '\nlarge leaf length : ' + str(length_large_leaf_list))

    # translate large-leaf-lists to suffix lists
    large_suffix_list = []
    for index in range(large_leaf_list[0], large_leaf_list[1]+1):
        large_suffix_list.append(depthfirst_to_suffix[index])
    if testing: print('large suffix list : ' + str(large_suffix_list))

    # get full suffix/leaf list
    full_suffix_list = [] # This corresponds to the LL(v) in the slides
    depth_min = node.depth_first[0] # the minimum depth for the internal node
    depth_max = node.depth_first[1] # the maximum depth for the internal node
    for index in range(depth_min, depth_max+1):
        full_suffix_list.append(depthfirst_to_suffix[index])
    
    # get small suffix/leaf list
    small_suffix_list = [x for x in full_suffix_list if x not in large_suffix_list]

    if node.string_depth > 1:
        for i in small_suffix_list:
            if i + node.string_depth in full_suffix_list and sequence[i] != sequence[i+2*node.string_depth]:
                tandem_repeat_list.append([i, node.string_depth])
            if i - node.string_depth in large_suffix_list and sequence[i-node.string_depth] != sequence[i+node.string_depth]:
                tandem_repeat_list.append([i-node.string_depth, node.string_depth])
        if testing: print('tandem repeats list : ' + str(tandem_repeat_list))

    if node.children:
        for child in node.children.values():
            returned_tandem_repeats = stoye_gusfield(child, depthfirst_to_suffix, sequence, testing)
            if returned_tandem_repeats != None and returned_tandem_repeats != []:
                tandem_repeat_list = tandem_repeat_list + returned_tandem_repeats

    return tandem_repeat_list


def left_rotation(tandem_repeats, sequence):
    rotated_tr = []
    for tr in tandem_repeats:
        i = tr[0] - 1
        j = i  + 2 * tr[1]
        while sequence[i] == sequence[j]:
            rotated_tr.append([i, tr[1]])
            i-=1
            j-=1
    return tandem_repeats + rotated_tr

