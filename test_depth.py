# get functions from other files
from suffixtree import NaiveSuffixTree
from depth import depth

# our test sequence
#test_seq = "abaabaabbba$"
#test_seq = "banana$"
test_seq = "cgtaaca$"

# Feed it to the suffix tree
treeStruct = NaiveSuffixTree(test_seq)
naiveSuffixTree = treeStruct.build_tree(False)

# Check the depth first function
depth(naiveSuffixTree, depth_number=0, testing=False)
naiveSuffixTree.print_tree_lines()