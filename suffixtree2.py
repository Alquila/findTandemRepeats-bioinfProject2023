from node2 import Node2


class NaiveSuffixTree2:
    """
        Builds a Naive Suffix Tree
        """

    def __init__(self, sequence):
        self.sequence = sequence

    def build_tree(self, testing=False):
        # Add root to tree
        Tree = Node2("root", -1, -1, -1)
        len_seq = len(self.sequence)

        # Variables needed
        current_node = Tree
        Nodes = []

        # Testing Print Statements
        if testing: print("Sequence: \n" + self.sequence + "\nSequence length: " + str(len_seq))

        # Build Tree
        for i in range(len_seq):
            if testing: print("Starting new sequence: " + str(i))

            if (current_node.type == "root") and (not current_node.children):
                leaf = make_new_leaf2()
                Nodes.append(leaf)