from node import Node, make_new_leaf, make_new_internal_node
from depth import full_depth_first_and_array, string_depth
from loopdy_loop import full_depth_first_and_array_loop, string_depth_loop


class NaiveSuffixTree:
    """
        Builds a Naive Suffix Tree
        """

    def __init__(self, sequence):
        self.sequence = sequence

    def build_tree(self, testing=False, arrays=False):
        # Add root to tree
        Tree = Node("root", suffix="root", start=-1, end=-1, children={})
        len_seq = len(self.sequence) - 1

        # Variables needed
        current_node = Tree
        Nodes = 1
        #print("making Tree")
        # Testing Print Statements
        if testing: print("Sequence: \n" + self.sequence + "\nSequence length: " + str(len_seq) + "\n")

        # Build Tree
        for i in range(len_seq + 1):
            if testing:
                print("\n")
                Tree.print_tree()
                print("\n")
            letter = self.sequence[i]

            if testing: print("Starting sequence: " + str(i) + ", letter is: " + letter)

            if (current_node.type == "root") and (letter not in current_node.children):
                if testing: print("len_seq: " + str(len_seq))
                leaf = make_new_leaf(self.sequence, current_node, i, i, len_seq)
                Nodes += 1
                if testing:
                    print("Added new leaf to root")
                    print("Leaf's parent: " + str(leaf.parent.type))
                    print("Node: " + str(current_node.suffix) + "'s Children:" + str(current_node.children.keys()))
                    print("Node: " + str(leaf.suffix) + "'s Children - should be empty:" + str(leaf.children.keys()))
                    print("Amount of Nodes: " + str(Nodes))
                    print("leafs end: " + str(leaf.end))
                    print("\n")

            elif (current_node.type == "root") and (letter in current_node.children):
                current_node = current_node.children[letter]
                if testing: print("current node: ", str(current_node))
                new_node_type, split_index, path_node, new_leaf_idx = traverse_tree(self.sequence, current_node, i,
                                                                                    testing)
                if new_node_type == "leaf":
                    parent = path_node
                    if testing: print("NEW LEAF: " + str(new_leaf_idx))
                    leaf = make_new_leaf(self.sequence, parent, new_leaf_idx, i, len_seq)
                    Nodes += 1
                    if testing:
                        print("Added new leaf to parent: " + path_node.suffix)
                        print("Leaf's parent: " + str(leaf.parent.type))
                        print("Node: " + str(leaf.parent.type) + "'s Children:" +
                              str(leaf.parent.children.keys()))
                        print("Node: " + str(leaf.parent.parent.type) + "'s Children:" +
                              str(leaf.parent.parent.children.keys()))
                        print("Node: " + str(leaf.suffix) + "'s Children:" + str(leaf.children.keys()))
                        print("Amount of Nodes: " + str(Nodes))
                        print("\n")

                elif new_node_type == "internal":
                    internal_node, new_leaf = make_new_internal_node(self.sequence, path_node, i,
                                                                     split_index, len_seq, new_leaf_idx)
                    Nodes += 1
                    Nodes += 1
                    if testing:
                        print("Make new internal node")
                        print("Internals nodes parent: " + str(internal_node.parent.type))
                        print("Leafs parent: " + str(new_leaf.parent.type))
                        print("Node: " + str(internal_node.parent.type) + "'s Children:" + str(
                            internal_node.parent.children.keys()))
                        print("Node: " + str(internal_node.suffix) + "'s Children:" + str(internal_node.children.keys()))
                        print("Node: " + str(new_leaf.suffix) + "'s Children:" + str(new_leaf.children.keys()))
                        print("Amount of Nodes: " + str(Nodes))
                        print("\n")
                current_node = Tree

        if testing:
            print("Nodes made: " + str(Nodes))
            print(Tree.children.keys())

        if arrays:
            #_, _, depthfirst_to_suffix, suffix_to_depthfirst = full_depth_first_and_array(Tree, depth_to_suffix={}, suffix_to_depth={}, depth_number=0, testing=testing)
            depthfirst_to_suffix, suffix_to_depthfirst = full_depth_first_and_array_loop(Tree, testing=testing)

            if testing:
                print("\n")
                Tree.print_tree_lines()
                print("\n")

        if testing:
            print("Depth-first to suffix: ")
            print(depthfirst_to_suffix)
            print("Suffix to depth-first: ")
            print(suffix_to_depthfirst)
            print("\n")

        #string_depth(Tree, testing)
        string_depth_loop(Tree, testing)

        if arrays:
            #print("tree done in array")
            return Tree, depthfirst_to_suffix, suffix_to_depthfirst

        return Tree


def traverse_tree(sequence, path_node: Node, letter_idx: int, testing=False):
    if testing: print("Traversing tree, i: " + str(letter_idx))
    path_idx = path_node.start
    if testing:
        print("Path node: " + str(path_node))
        print("Path_start " + str(path_idx) + ", parent_end: " + str(path_node.end))

    # Calculate range for
    branch_len = path_node.end - path_idx + 1
    new_suffix_len = len(sequence) - letter_idx + 1
    it = min(branch_len, new_suffix_len)
    if testing: print("it: min(branch_len, new_suffix_len): " + str(it))
    for _ in range(0, it):
        seq_letter = sequence[path_idx]
        letter = sequence[letter_idx]
        if testing: print("seq_letter: " + seq_letter + ", letter: " + letter)
        if letter == seq_letter:
            path_idx += 1
            letter_idx += 1
        else:
            if testing:
                print("path_idx: ", str(path_idx))
                print("path_node: ", str(path_node))
                print("letter_idx: " + str(letter_idx))
            return "internal", path_idx, path_node, letter_idx
    next_idx = letter_idx
    if sequence[next_idx] in path_node.children:
        new_parent = path_node.children[sequence[next_idx]]
        return traverse_tree(sequence, new_parent, letter_idx, testing)
    else:
        if testing: print("next_idx: " + str(next_idx) + ", letter_idx: " + str(letter_idx))
        return "leaf", next_idx, path_node, letter_idx
