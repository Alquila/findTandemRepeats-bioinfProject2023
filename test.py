
# get functions from other files
from suffixtree import NaiveSuffixTree
from fasta_reader import read_fasta_file, add_dollar_sign

# Read in the fasta file
test_seq = read_fasta_file("ls_orchid.fasta")
test_dollar_seq = add_dollar_sign(test_seq)

# Feed it to the suffix tree
treeStruct = NaiveSuffixTree(test_dollar_seq)
naiveSuffixTree = treeStruct.buildTree()

# Check out the suffix tree
