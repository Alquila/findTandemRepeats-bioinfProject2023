from node2 import Node2, make_new_leaf, make_new_internal2


class NaiveSuffixTree2:
    """
        Builds a Naive Suffix Tree
        """

    def __init__(self, sequence):
        self.sequence = sequence

    def build_tree(self, testing=False):
        # Add root to tree
        Tree = Node2("root", suffix="root", start=-1, end=-1, children={})
        len_seq = len(self.sequence) - 1
        # Variables needed
        current_node = Tree
        Nodes = 1

        # Testing Print Statements
        if testing: print("Sequence: \n" + self.sequence + "\nSequence length: " + str(len_seq) + "\n")

        # Build Tree
        for i in range(len_seq + 1):
            letter = self.sequence[i]
            if testing: print("Starting sequence: " + str(i) + ", letter is: " + letter)
            if (current_node.type == "root") and (letter not in current_node.children):
                leaf = make_new_leaf(self.sequence, current_node, i, i, len_seq)
                Nodes += 1
                if testing:
                    print("Added new leaf to root")
                    print("Leaf's parent: " + str(leaf.parent.suffix))
                    print("Node: " + str(current_node.suffix) + "'s Children:" + str(current_node.children.keys()))
                    print("Node: " + str(leaf.suffix) + "'s Children - should be empty:" + str(leaf.children.keys()))
                    print("Amount of Nodes: " + str(Nodes))
                    print("\n")

            elif (current_node.type == "root") and (letter in current_node.children):
                current_node = current_node.children[letter]
                new_node_type, split_index, child_node, new_leaf_idx = traverse_tree2(self.sequence, current_node, i,
                                                                                      True)
                if new_node_type == "leaf":
                    parent = child_node
                    if testing: print("NEW LEAF: " + str(new_leaf_idx))
                    leaf = make_new_leaf(self.sequence, parent, new_leaf_idx, i, len_seq)
                    Nodes += 1
                    if testing:
                        print("Added new leaf to parent: " + child_node.suffix)
                        print("Leaf's parent: " + str(leaf.parent.suffix))
                        print("Node: " + str(leaf.parent.suffix) + "'s Children:" +
                              str(leaf.parent.children.keys()))
                        print("Node: " + str(leaf.parent.parent.suffix) + "'s Children:" +
                              str(leaf.parent.parent.children.keys()))
                        print("Node: " + str(leaf.suffix) + "'s Children:" + str(leaf.children.keys()))
                        print("Amount of Nodes: " + str(Nodes))
                        print("\n")

                elif new_node_type == "internal":
                    internal_node, new_leaf = make_new_internal2(self.sequence, child_node, i,
                                                                 split_index, len_seq, new_leaf_idx)
                    Nodes += 1
                    Nodes += 1
                    if testing:
                        print("Make new internal node")
                        print("Internals nodes parent: " + str(internal_node.parent.suffix))
                        print("Leafs parent: " + str(new_leaf.parent.suffix))
                        print("Node: " + str(internal_node.parent.suffix) + "'s Children:" + str(
                            internal_node.parent.children.keys()))
                        print("Node: " + str(internal_node.suffix) + "'s Children:" + str(internal_node.children.keys()))
                        print("Node: " + str(new_leaf.suffix) + "'s Children:" + str(new_leaf.children.keys()))
                        print("Amount of Nodes: " + str(Nodes))
                        print("\n")
                current_node = Tree

        if testing:
            print("Nodes made: " + str(Nodes))
            print(Tree.children.keys())

        print(repr(Tree))


def traverse_tree2(sequence, parent_node: Node2, letter_idx: int, testing=False):
    if testing: print("Traversing tree, i: " + str(letter_idx))
    parent_idx = parent_node.start
    print("Parent_start " + str(parent_idx) + ", parent_end: " + str(parent_node.end))

    # Calculate range for
    branch_len = parent_node.end - parent_idx + 1
    new_suffix_len = len(sequence) - letter_idx + 1
    it = min(branch_len, new_suffix_len)
    for _ in range(0, it):
        if testing: print("while: letter_idx(" + str(letter_idx) + ") <= parent_node.end(" + str(parent_node.end) + ")")
        seq_letter = sequence[parent_idx]
        letter = sequence[letter_idx]
        if letter == seq_letter:
            parent_idx += 1
            letter_idx += 1
        else:
            if testing: print("letter_idx: " + str(letter_idx))
            return "internal", parent_idx, parent_node, letter_idx
    next_idx = letter_idx
    if sequence[next_idx] in parent_node.children:
        new_parent = parent_node.children[sequence[next_idx]]
        return traverse_tree2(sequence, new_parent, letter_idx, True)
    else:
        if testing: print("next_idx: " + str(next_idx) + ", letter_idx: " + str(letter_idx))
        return "leaf", next_idx, parent_node, (letter_idx)



def visualise_tree(Tree: Node2, testing=False):
    if testing: print("Starting visualising tree")


