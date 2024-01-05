from suffixtree import NaiveSuffixTree
from stoye_gusfield_algorithm import basic_stoye_gusfield, stoye_gusfield, naive_algorithm, left_rotation
from sg_iteration import basic_stoye_gusfield_loopy, stoye_gusfield_loopy
from dict_to_list import dict_to_list
import time

def add_dollar_sign(sequence):
    '''
    This function adds a $ to a string and returns the new string
    '''

    dollar_seq = sequence + "$"
    return dollar_seq


def execute_naive_algorithm(seq: str):
    print("Tandem Repeats found using the N^2 algorithm: " + str(naive_algorithm(seq)))


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


def main_time(algorithm: str, sequence: str):
    sequence = add_dollar_sign(sequence)

    match algorithm:
        case "stupid":
            start_time = time.time_ns()
            TR = naive_algorithm(sequence)
            end_time = time.time_ns()
            #print("Tandem Repeats found using the N^3 algorithm: " + str(TR))
            print("Number of Tandem Repeats found using the N^3 algorithm: " + str(len(TR)))
            final_time = end_time - start_time
            print("Naive implementation with final time: " + str(final_time))
            return TR, final_time
        case "basic":
            tree_struct = NaiveSuffixTree(sequence)
            suffixtree, depthfirst_to_suffix, _ = tree_struct.build_tree(False, True)
            start_time = time.time_ns()
            tandem_repeats = basic_stoye_gusfield(suffixtree, depthfirst_to_suffix, sequence, False)
            #tandem_repeats = basic_stoye_gusfield_loopy(suffixtree, depthfirst_to_suffix_list, sequence, False)
            end_time = time.time_ns()
            tr_lr = left_rotation(tandem_repeats, sequence)
            #print("Tandem Repeats found using the basic Stoye-Gusfield algorithm: " + str(tandem_repeats))
            print("Number of Tandem Repeats found using the basic Stoye-Gusfield algorithm: " + str(len(tr_lr)))
            final_time = end_time - start_time
            print("Basic Stoye-Gusfield with final time: " + str(final_time))
            return tr_lr, final_time
        case "optimized":
            tree_struct = NaiveSuffixTree(sequence)
            suffixtree, depthfirst_to_suffix, _ = tree_struct.build_tree(False, True)
            #suffixtree.print_tree()
            depthfirst_to_suffix_list = dict_to_list(depthfirst_to_suffix)
            start_time = time.time_ns()
            #tandem_repeats = stoye_gusfield(suffixtree, depthfirst_to_suffix, sequence, False)
            tandem_repeats = stoye_gusfield_loopy(suffixtree, depthfirst_to_suffix_list, sequence, False)
            end_time = time.time_ns()
            tr_lr = left_rotation(tandem_repeats, sequence)
            print("Number of Tandem Repeats found using the optimized Stoye-Gusfield algorithm: " + str(len(tr_lr)))
            #print("Tandem Repeats found using the optimized Stoye-Gusfield algorithm: " + str(tandem_repeats))
            final_time = end_time - start_time
            print("Optimised Stoye-Gusfield with final time: " + str(final_time))
            return tr_lr, final_time


def main(algorithm: str, sequence: str):
    sequence = add_dollar_sign(sequence)

    match algorithm:
        case "naive":
            execute_naive_algorithm(sequence)
        case "basic":
            execute_basic_stoyegusfield(sequence)
        case "optimized":
            execute_optimized_stoyegusfield(sequence)

