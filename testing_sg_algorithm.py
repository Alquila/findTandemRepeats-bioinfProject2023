from suffixtree import NaiveSuffixTree
from stoye_gusfield_algorithm import basic_stoye_gusfield, stoye_gusfield, left_rotation, stupid_algorithm

test_seq_1 = "banana$"
test_seq_2 = "cgtaacaagg$"
test_seq_3 = "abaabaabbba$"
test_seq_4 = "heliliillihehehheel$"
test_seq_5 = "mississippi$"

# Feed it to the suffix tree
treeStruct = NaiveSuffixTree(test_seq_5)
naiveSuffixTree, depthfirst_to_suffix, _ = treeStruct.build_tree(testing=False, arrays=True)

naiveSuffixTree.print_tree_lines()

# basic_tr = basic_stoye_gusfield(naiveSuffixTree, depthfirst_to_suffix, test_seq_5, False)

# optimised_tr = stoye_gusfield(naiveSuffixTree, depthfirst_to_suffix, test_seq_5, False)

print(stupid_algorithm(test_seq_5))

basic_tr = (basic_stoye_gusfield(naiveSuffixTree, depthfirst_to_suffix, test_seq_5, False))

#print(stoye_gusfield(naiveSuffixTree, depthfirst_to_suffix, test_seq_5, False))

print(left_rotation(basic_tr, test_seq_5))

#print(left_rotation(optimised_tr, test_seq_5))

#print(stupid_algorithm(test_seq_5))