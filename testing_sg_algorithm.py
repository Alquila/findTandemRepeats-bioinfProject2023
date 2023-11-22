from suffixtree import NaiveSuffixTree
from simple_stoye_gusfield_algorithm import basic_stoye_gusfield, stoye_gusfield, left_rotation

test_seq_1 = "banana$"
test_seq_2 = "cgtaacaagg$"
test_seq_3 = "abaabaabbba$"
test_seq_4 = "heliliillihehehheel$"

# Feed it to the suffix tree
treeStruct = NaiveSuffixTree(test_seq_3)
naiveSuffixTree, depthfirst_to_suffix, _ = treeStruct.build_tree(testing=False, arrays=True)

naiveSuffixTree.print_tree_lines()

basic_tr = basic_stoye_gusfield(naiveSuffixTree, depthfirst_to_suffix, test_seq_3, False)

optimised_tr = stoye_gusfield(naiveSuffixTree, depthfirst_to_suffix, test_seq_3, False)

#print(basic_stoye_gusfield(naiveSuffixTree, depthfirst_to_suffix, test_seq_3, False))

#print(stoye_gusfield(naiveSuffixTree, depthfirst_to_suffix, test_seq_3, False))

print(left_rotation(basic_tr, test_seq_3))

print(left_rotation(optimised_tr, test_seq_3))
