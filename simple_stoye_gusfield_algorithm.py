from suffixtree import NaiveSuffixTree
from node import Node

test_seq = "abaabaabbba$"

# Feed it to the suffix tree
treeStruct = NaiveSuffixTree(test_seq)
naiveSuffixTree, depthfirst_to_suffix, _ = treeStruct.build_tree(testing=False, arrays=True)

naiveSuffixTree.print_tree_lines()


def stoye_gusfield(node: Node, depthfirst_to_suffix, sequence, testing):
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
                tandem_repeat = (i, node.string_depth, 2)
                if testing: print('!!!' + str(tandem_repeat))
                tandem_repeat_list.append(tandem_repeat)

    if node.children:
        for child in node.children.values():
            returned_tandem_repeats = stoye_gusfield(child, depthfirst_to_suffix, sequence, testing)
            if returned_tandem_repeats != None and returned_tandem_repeats != []:
                tandem_repeat_list.append(returned_tandem_repeats)

    return tandem_repeat_list

print(stoye_gusfield(naiveSuffixTree, depthfirst_to_suffix, test_seq, True))
