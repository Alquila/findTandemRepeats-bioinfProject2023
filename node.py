class Node:
    def __init__(self, name, depth=0, start_idx=0, end_idx=0,
                 parent=None, children=None):
        self.name = name
        self.depth = depth
        self.parent = parent
        self.children = children
        self.start_idx = start_idx
        self.end_idx = end_idx

        def __str__(self):
            return f"{self.name}({self.depth})"


def make_new_leaf(parent, index_fix, len_seq, leaf_number):
    new_leaf_node = Node(name=leaf_number,
                         start_idx=parent.end_idx + index_fix,
                         end_idx=len_seq,
                         parent=parent)
    parent.children.append(new_leaf_node)
    # print("I make new leaf")
    return new_leaf_node


def make_new_internal_node(parent, child_node, length, leaf_number, res_index):
    if parent.name != "root":
        internal_node = Node(name="internal",
                             start_idx=(parent.end_idx + 1),
                             end_idx=(parent.end_idx + res_index),
                             parent=parent,
                             children={})
    else:
        internal_node = Node(name="internal",
                             start_idx=child_node.start_idx,
                             end_idx=(child_node.start_idx + res_index),
                             parent=parent,
                             children={})

    # Make class to handle node. Should be able to handle both internal nodes and leafs
    # node should have a: parent, children,
    parent.children.remove(child_node)
    parent.children.append(internal_node)
    internal_node.children.append(child_node)
    child_node.start_idx = internal_node.end_idx + 1
    child_node.parent = internal_node
    leaf = make_new_leaf(internal_node, 1, length, leaf_number)
    return internal_node, leaf
