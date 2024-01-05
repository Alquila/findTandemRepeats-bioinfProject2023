import unittest
import time, os
from main import main, main_time
from test_sequences import defined_test_sequences
from fasta_reader import read_fasta_file
import matplotlib.pyplot as plt


def defined_test_sequences_small():
    test_seq = ["banana", "cgtaacaagg", "abaabaabbba", "mississippi", "heliliillihehehheel"]

    return test_seq


def test_loopdy_loop():
    algorithms = ["naive", "basic", "optimized"]
    tr_list = []

    for alg in algorithms:
        print("\n")
        tr, final_time = main_time(alg, "banana")
        tr_list.append(tr)



def running_times():
    naive_alg_times = []
    basic_sg_times = []
    optimised_sq_times = []

    test_sequences = defined_test_sequences()
    algorithms = ["naive", "basic", "optimized"]

    for test_seq in test_sequences:
        for alg in algorithms:
            i = 0
            start_time = time.time_ns()
            main(alg, test_seq)
            end_time = time.time_ns()
            final_time = end_time - start_time
            match i:
                case 0:
                    naive_alg_times.append(final_time)
                case 1:
                    basic_sg_times.append(final_time)
                case 2:
                    optimised_sq_times.append(final_time)
            i += 1

    return naive_alg_times, basic_sg_times, optimised_sq_times


def running_times_wo_tree():
    naive_alg_times = []
    basic_sg_times = []
    optimised_sq_times = []

    test_sequences = defined_test_sequences()
    algorithms = ["naive", "basic", "optimized"]
    #algorithms = ["naive", "optimized"]
    #algorithms = ["optimized"]

    tr_list = []

    for test_seq in test_sequences:
        i = 0
        for alg in algorithms:
            tr, final_time = main_time(alg, test_seq)
            tr_list.append(tr)
            match i:
                case 0:
                    naive_alg_times.append(final_time)
                case 1:
                    basic_sg_times.append(final_time)
                case 2:
                    optimised_sq_times.append(final_time)
            i += 1
    #assert tr_list[0] == tr_list[1] == tr_list[2]
    return naive_alg_times, basic_sg_times, optimised_sq_times


def test_running_time():
    slow_times, basic_times, optimised_times = running_times_wo_tree()
    count = []
    no_of_test_seq = len(slow_times)
    for i in range(no_of_test_seq):
        no = i + 1
        count.append(no)
    print(count)
    print("Slow times: " + str(slow_times))
    print("Basic SG-times: " + str(basic_times))
    print("Optimized times: " + str(optimised_times))
    # PLOT Naive
    plt.title('Running time')
    plt.xlabel('Test sequences')
    plt.ylabel('Time (ns)')
    #plt.xscale('log')
    plt.yscale('log')
    plt.scatter(count, slow_times, c='red')
    plt.scatter(count, basic_times, c='gold')
    plt.scatter(count, optimised_times, c='green')
    plt.savefig('figures/running_time', bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    test_running_time()