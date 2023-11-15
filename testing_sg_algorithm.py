from suffixtree import NaiveSuffixTree
from simple_stoye_gusfield_algorithm import basic_stoye_gusfield

test_seq = "abccbccanan$"

# Feed it to the suffix tree
treeStruct = NaiveSuffixTree(test_seq)
naiveSuffixTree, depthfirst_to_suffix, _ = treeStruct.build_tree(testing=False, arrays=True)

naiveSuffixTree.print_tree_lines()

print(basic_stoye_gusfield(naiveSuffixTree, depthfirst_to_suffix, test_seq, True))
