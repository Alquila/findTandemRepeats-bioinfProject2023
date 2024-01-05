from suffixtree import NaiveSuffixTree

test_string = "banana&"
test_string = "cgtaaca$"

treeStruct = NaiveSuffixTree(test_string)
naiveSuffixTree = treeStruct.build_tree(False)

print("__str()__: \n", str(naiveSuffixTree))

naiveSuffixTree.print_tree()
