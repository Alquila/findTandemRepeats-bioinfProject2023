import unittest
import time, os
from main import main
from fasta_reader import read_fasta_file


def defined_test_sequences():
    test_seq = ["banana", "cgtaacaagg", "abaabaabbba", "mississippi", "heliliillihehehheel",
                read_fasta_file("ls_orchid.fasta")]

    return test_seq


def running_times():
    stupid_alg_times = []
    basic_sg_times = []
    optimised_sq_times = []

    test_sequences = defined_test_sequences()
    algorithms = ["stupid", "basic", "optimized"]

    for test_seq in test_sequences:
        i = 0
        for alg in algorithms:
            start_time = time.time_ns()
            main(alg, test_seq)
            end_time = time.time_ns()
            final_time = end_time - start_time
            match i:
                case 0:
                    stupid_alg_times.append(final_time)
                case 1:
                    basic_sg_times.append(final_time)
                case 2:
                    optimised_sq_times.append(final_time)
            i += 1

    return stupid_alg_times, basic_sg_times, optimised_sq_times


class MyTestCase(unittest.TestCase):
    def test_running_time(self):
        self.assertEqual(True, True)  # add assertion here


if __name__ == '__main__':
    unittest.main()

# time.time_ns()
