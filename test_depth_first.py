# get functions from other files
from suffixtree2 import NaiveSuffixTree2
from depth_first import depth_first
from depth_first import leaves_depth_first

# our test sequence
test_seq = "banana$"

# Feed it to the suffix tree
treeStruct = NaiveSuffixTree2(test_seq)
naiveSuffixTree = treeStruct.build_tree(False)

# Check the depth first function
#depth_first(naiveSuffixTree, testing=True)

# Check the leaf depth first function
leaves_depth_first(naiveSuffixTree, testing=True)