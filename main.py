from suffixtree import NaiveSuffixTree
from stoye_gusfield_algorithm import basic_stoye_gusfield, stoye_gusfield, stupid_algorithm


def add_dollar_sign(sequence):
    '''
    This function adds a $ to a string and returns the new string
    '''

    dollar_seq = sequence + "$"
    return dollar_seq


def execute_stupid_algorithm(seq: str):
    print("Tandem Repeats found using the N^2 algorithm: " + str(stupid_algorithm(seq)))


def execute_basic_stoyegusfield(seq: str):
    tree_struct = NaiveSuffixTree(seq)
    suffixtree, depthfirst_to_suffix, _ = tree_struct.build_tree(False, True)
    tandem_repeats = basic_stoye_gusfield(suffixtree, depthfirst_to_suffix, seq, False)
    print("Tandem Repeats found using the basic Stoye-Gusfield algorithm: " + str(tandem_repeats))


def execute_optimized_stoyegusfield(seq: str):
    tree_struct = NaiveSuffixTree(seq)
    suffixtree, depthfirst_to_suffix, _ = tree_struct.build_tree(False, True)
    tandem_repeats = stoye_gusfield(suffixtree, depthfirst_to_suffix, seq, False)
    print("Tandem Repeats found using the optimized Stoye-Gusfield algorithm: " + str(tandem_repeats))


def main(algorithm: str, sequence: str):
    sequence = add_dollar_sign(sequence)

    match algorithm:
        case "stupid":
            execute_stupid_algorithm(sequence)
        case "basic":
            execute_basic_stoyegusfield(sequence)
        case "optimized":
            execute_optimized_stoyegusfield(sequence)


