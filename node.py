class Node:
    def __init__(self, node_type: str, suffix, start: int, end: int, children: dict, depth_first=None, depth=None, parent=None):
        self.type = node_type
        self.suffix = suffix
        self.start = start
        self.end = end
        self.depth_first = depth_first
        self.depth = depth
        self.children = children
        self.parent = parent

    def __str__(self):
        return f"{self.suffix}: {self.depth_first}"

    def print_tree(self, level=0):
        print('\t' * level + repr(self.suffix) + ": " + repr(self.depth_first))
        for child in self.children.values():
            child.print_tree(level + 1)

    def print_tree_lines(self, level=0, last=False, header=''):
        distance = '\t' * level
        elbow = "   └── "
        pipe = "   │  "
        tee = "   ├── "
        repr_suffix = repr(self.suffix) + ": " + repr(self.depth_first)
        print(repr_suffix) if self.type == "root" else print(header + (elbow if last else tee) + repr_suffix)
        for i, child in enumerate(self.children.values()):
            child.print_tree_lines(level + 1, last=(i == len(self.children) - 1),
                                   header=header + (distance if last else pipe))

    def print_path(self):
        return f"({self.start},{self.end})"


def make_new_leaf(seq, parent: Node, start_idx: int, suff_no: int, len_seq: int):
    new_leaf = Node(node_type="leaf",
                    suffix=suff_no,
                    start=start_idx,
                    end=len_seq,
                    parent=parent,
                    children={})
    parent.children[seq[start_idx]] = new_leaf
    return new_leaf


def make_new_internal_node(seq, path, suffix_no: int, split_idx: int, len_seq: int, new_leaf_idx: int):
    new_internal_node = Node(node_type="internal",
                             suffix="i" + str(suffix_no),
                             start=path.start,
                             end=split_idx - 1,
                             parent=path.parent,
                             children={})

    # Set letters from path and new split
    child_letter = seq[path.start]
    split_letter = seq[split_idx]

    # Add path to new internal nodes children
    path.start = split_idx
    new_internal_node.children[split_letter] = path

    # Set paths new parent to new_internal_node
    path.parent.children[child_letter] = new_internal_node
    path.parent = new_internal_node

    # Make new leaf
    leaf = make_new_leaf(seq, new_internal_node, new_leaf_idx, suffix_no, len_seq)
    return new_internal_node, leaf
