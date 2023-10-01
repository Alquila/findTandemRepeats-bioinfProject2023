class Node2:
    def __init__(self, node_type: str, label, start: int, end: int, children: dict, depth=None, parent=None):
        self.type = node_type
        self.label = label
        self.start = start
        self.end = end
        self.depth = depth
        self.children = children
        self.parent = parent

        def __str__(self):
            return f"{self.name}({self.depth})"

        def print_path(self):
            return f"({self.start},{self.end})"


def make_new_leaf(seq, parent: Node2, start_idx: int, suff_no: int, len_seq: int):
    # Takes parent
    new_leaf = Node2(node_type="leaf",
                     label=suff_no,
                     start=start_idx,
                     end=len_seq,
                     parent=parent,
                     children={})
    parent.children[seq[start_idx]] = new_leaf
    return new_leaf


def make_new_internal2(seq, child, suff_no: int, split_idx: int, len_seq: int, new_leaf_idx: int):
    # Takes child
    new_internal_node = Node2(node_type="internal",
                              label="i" + str(suff_no),
                              start=child.start,
                              end=split_idx - 1,
                              parent=child.parent,
                              children={})

    child_letter = seq[child.start]  # used to save new internal node
    split_letter = seq[split_idx]
    child.start = split_idx
    new_internal_node.children[split_letter] = child
    child.parent.children[child_letter] = new_internal_node  # child's new parent to new_internal_node

    leaf = make_new_leaf(seq, new_internal_node, new_leaf_idx, suff_no, len_seq)

    return new_internal_node, leaf
