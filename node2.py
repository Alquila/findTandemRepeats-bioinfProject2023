class Node2:
    def __init__(self, node_type, label, start, end, depth=None, children={}, parent=None):
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


def make_new_leaf2(parent, suff_no, len_seq):
    new_leaf = Node2(node_type="leaf",
                     label=suff_no,
                     start=parent.end+1,
                     end=len_seq,
                     parent=parent)
    parent.children[]
