from pathlib import Path
class Node:
    def __init__(self, node_type: str, suffix, start: int, end: int, children: dict, depth=None, parent=None):
        self.type = node_type
        self.suffix = suffix
        self.start = start
        self.end = end
        self.depth = depth
        self.children = children
        self.parent = parent

    def __str__(self):
        return f"{self.type}({self.suffix})"

    #def __repr__(self, level=0):
    #    ret = "\t"*level+repr(self.suffix)+"\n"
    #    for child in self.children:
    #        ret += child.__repr__(level+1)
    #    return ret

    def other_name(self, level=0):
        print('\t' * level + repr(self.suffix))
        for child in self.children.values():
            child.other_name(level + 1)

    def print_path(self):
        return f"({self.start},{self.end})"

    #def print_tree(self, p: Path, last=True, header=''):
    #    elbow = "└──"
    #    pipe = "│  "
    #    tee = "├──"
    #    blank = "   "
    #    print(header + (elbow if last else tee) + p.name)
    #    if p.is_dir():
    #        children = list(p.iterdir())
    #        for i, c in enumerate(children):
    #            print_tree(c, header=header + (blank if last else pipe), last=i == len(children) - 1)
    #
    #print_tree(Path("./MNE-001-2014-bids-cache"))


def make_new_leaf(seq, parent: Node, start_idx: int, suff_no: int, len_seq: int):
    # Takes parent
    new_leaf = Node(node_type="leaf",
                    suffix=suff_no,
                    start=start_idx,
                    end=len_seq,
                    parent=parent,
                    children={})
    parent.children[seq[start_idx]] = new_leaf
    return new_leaf


def make_new_internal2(seq, child, suff_no: int, split_idx: int, len_seq: int, new_leaf_idx: int):
    # Takes child
    print("In make new internal node \n")
    print("path_node ", str(child))
    print("path_node_parent: ", str(child.parent))
    new_internal_node = Node(node_type="internal",
                             suffix="i" + str(suff_no),
                             start=child.start,
                             end=split_idx - 1,
                             parent=child.parent,
                             children={})

    child_letter = seq[child.start]  # used to save new internal node
    split_letter = seq[split_idx]
    child.start = split_idx
    #if child.parent.type == "root":
    new_internal_node.children[split_letter] = child
    #else:
    #    children = child.parent.children.copy()
    #    new_internal_node.children = children

    child.parent.children[child_letter] = new_internal_node  # child's new parent to new_internal_node
    child.parent = new_internal_node
    leaf = make_new_leaf(seq, new_internal_node, new_leaf_idx, suff_no, len_seq)
    print("new leaf in internal node + parent: " + str(leaf) + ", " + str(leaf.parent))
    return new_internal_node, leaf
