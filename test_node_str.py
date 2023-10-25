from suffixtree import NaiveSuffixTree

test_string = "banana&"
test_string = "cgtaaca$"

treeStruct = NaiveSuffixTree(test_string)
naiveSuffixTree = treeStruct.build_tree(False)

print("__str()__: \n", str(naiveSuffixTree))

print("other_name(): \n")
naiveSuffixTree.other_name()
