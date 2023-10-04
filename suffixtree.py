from node import Node, make_new_internal_node, make_new_leaf

class NaiveSuffixTree:
#NOTE - change name to suffixtree_naive.py?
    """
    Builds a Naive Suffix Tree
    """

    def __init__(self, sequence):
        self.sequence = sequence

    def build_tree(self):
        # Add root to tree
        Tree = Node("root", children=[])
        Nodes = []
        print(self.sequence)
        # Build tree
        current_node = Tree
        leaf_number = 0
        len_seq = len(self.sequence)

        for i in range(len_seq):
        #for i in range(0, 7):
            print("starting new sequence: " + str(i))
            if (current_node.name == "root") and (not current_node.children):
                leaf = make_new_leaf(current_node, i, len_seq, leaf_number)
                Nodes.append(leaf)
                # print("leaf put in root " + str(leaf.name))
                leaf_number += 1
            elif (current_node.name == "root") and current_node.children:
                no_match_found = True
                for child in current_node.children:
                    print("index i and index child: " + str(i), str(child.start_idx))
                    if self.sequence[i] == self.sequence[child.start_idx]:
                        # print("match found between " + str(self.sequence[i]) + " and " + str(self.sequence[child.start_idx]))
                        no_match_found = False

                        res_idx = traverse_tree(sequence=self.sequence, suffix_idx=i, child_idx=child.start_idx,
                                                child_end=child.end_idx)
                        if res_idx == -1:
                            # go to Child and continue traverse and/or insert node
                            print("go to child")
                            current_node = child
                            print(current_node.name)
                        elif res_idx > 0:
                            # insert new  internal and leaf node
                            # print("tried to make internal nodes")
                            internal_node, leaf = make_new_internal_node(current_node, child, len_seq, leaf_number,
                                                                         res_idx)
                            Nodes.append(internal_node)
                            Nodes.append(child)
                            leaf_number += 1
                            # print("leaf index of internal leaf: " + str(leaf.name))
                            current_node = Tree
                            break
                if no_match_found:
                    leaf = make_new_leaf(current_node, i, len_seq, leaf_number)
                    leaf_number += 1
                    Nodes.append(leaf)
                    print("leaf in root " + str(leaf.name))
                    current_node = Tree

        print("length of seq: " + str(len_seq))
        print("How many nodes? ")
        print(len(Nodes))
        print("how many children does tree have")
        print(len(Tree.children))

        return Tree


def traverse_tree(sequence, suffix_idx, child_idx, child_end, res=0):
    res = res
    # print("traversing")
    # print("indexes: " + str(suffix_idx), str(child_idx))
    if suffix_idx == child_end:
        # print("check if equal")
        return -1
    elif sequence[suffix_idx] != sequence[child_idx]:
        # print("check if non equal")
        # print(suffix_idx, sequence[suffix_idx], child_idx, sequence[child_idx])
        return res
    else:
        return traverse_tree(sequence, suffix_idx + 1, child_idx + 1, child_end, res + 1)







'''
            elif current_node.children:
                for child in current_node.children:
                    # print("I'm making internal node and leaf")
                    if self.sequence[i] == self.sequence[child.start_idx]:
                        res_idx = traverse_tree(sequence=self.sequence, suffix_idx=i, child_idx=child.start_idx,
                                                child_end=child.end_idx)
                        if res_idx == -1:
                            # go to Child and continue traverse and/or insert node
                            print("go to child")
                            branch_found = True
                            current_node = child
                        elif res_idx > 0:
                            # insert new  internal and leaf node
                            internal_node, leaf = make_new_internal_node(current_node, child, len_seq, leaf_number,
                                                                         res_idx)
                            Nodes.append(internal_node)
                            Nodes.append(child)
                            leaf_number += 1
                            current_node = Tree
                            branch_found = True
                            break
            elif not branch_found:
                leaf = make_new_leaf(current_node, 0, len_seq, leaf_number)
                Nodes.append(leaf)
                leaf_number += 1
'''