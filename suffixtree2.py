from node2 import Node2, make_new_leaf2


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
            if testing: print("Starting sequence: " + str(i))

            letter = self.sequence[i]
            if (current_node.type == "root") and (not current_node.children):
                if testing: print("Added new leaf to empty root")
                leaf = make_new_leaf2(current_node, i, len_seq, letter)
                Nodes.append(leaf)
            elif (current_node.type == "root") and (letter in current_node.children):
                new_node_type, split_index, parent_node = traverse_tree2(self.sequence, current_node, i)
                match new_node_type:
                    case "leaf": make_new_leaf2(parent_node, split_index, len_seq, self.sequence[split_index])

def traverse_tree2(sequence, parent_node: Node2, letter_idx: int, testing: False):
    if testing: print("Traversing tree")
    parent_idx = parent_node.start
    res_idx = parent_node.start
    while letter_idx <= parent_node.end:
        seq_letter = sequence[parent_idx]
        letter = sequence[letter_idx]
        if letter == seq_letter:
            parent_idx += 1
            letter_idx += 1
            res_idx += 1
        else:
            return "internal", res_idx, parent_node
    next_idx = parent_node.end + 1
    if sequence[next_idx] in parent_node.children:
        new_parent = parent_node.children[sequence[next_idx]]
        return traverse_tree2(sequence, new_parent, next_idx)
    else:
        return "leaf", next_idx, parent_node
