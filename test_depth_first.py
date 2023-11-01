# get functions from other files
from suffixtree import NaiveSuffixTree
from depth_first import depth_first
from depth_first import leaves_depth_first
from depth_first import full_depth_first
from depth_first import full_depth_first_and_array

# our test sequence
#test_seq = "abaabaabbba$"
test_seq = "banana$"
#test_seq = "cgtaaca$"

# Feed it to the suffix tree
treeStruct = NaiveSuffixTree(test_seq)
naiveSuffixTree = treeStruct.build_tree(False)

# Check the depth first function
#depth_first(naiveSuffixTree, testing=True)

# Check the leaf depth first function
#leaves_depth_first(naiveSuffixTree, testing=True)

# Check the full depth first function
full_depth_first(naiveSuffixTree, testing=False)
naiveSuffixTree.print_tree()

# Check the full depth first and array function
#full_depth_first_and_array(naiveSuffixTree, testing=True)