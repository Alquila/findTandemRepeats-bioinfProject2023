from node import Node
from suffixtree import NaiveSuffixTree

test_string = "catata$"

test_tree = NaiveSuffixTree(test_string).buildTree()

print(test_tree)