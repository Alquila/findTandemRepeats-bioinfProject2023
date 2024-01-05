# Finding tandem repeats in genomic data

Implementation of Suffix-Tree in O(n^2) time.

Implementation of both basic and optimised Stoye-Gusfield algorithm.
Implemented with recursion in [stoye_gusfield_algorithm](stoye_gusfield_algorithm.py) and with 
iterations in [sq_iteration](sg_iteration.py).

The [main](main.py) file contains main-functions to run all three algorithms.

To test running time run:
```
python3 test_running_time.py
```
The test sequences used are defined in the file [test_sequences](test_sequences.py).
The test will print both the amount of tandem repeats found as well as the running time.
