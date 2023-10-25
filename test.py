# get functions from other files
from suffixtree2 import NaiveSuffixTree2
from fasta_reader import read_fasta_file, add_dollar_sign, seq_one

# Read in the fasta file
test_seq = read_fasta_file("ls_orchid.fasta")
test_dollar_seq = add_dollar_sign(test_seq)

actual_test_seq = add_dollar_sign(seq_one[0:7])

actual_test_seq = "abaabaabbba$"

# Feed it to the suffix tree
#treeStruct = NaiveSuffixTree(actual_test_seq)
#naiveSuffixTree = treeStruct.build_tree()


treeStruct = NaiveSuffixTree2(actual_test_seq)
naiveSuffixTree = treeStruct.build_tree(False)


#banana = add_dollar_sign("banana")
#treeStruct = NaiveSuffixTree2(banana)
#naiveSuffixTree = treeStruct.build_tree(True)

# Check out the suffix tree
