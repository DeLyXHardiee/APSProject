#!/bin/bash
USE_SCORING=0
. ../../_testdata_tools/gen.sh

use_solution WeWorkInTheDark.py              # Use ../submissions/accepted/js_100.cpp to generate answer files

compile generate_random.py
compile generate_explicit.py

# To generate explicit: (X, Y, N, M, Q)


# Generate answers to sample cases
sample 1
sample 2

tc  huge_grid_all_queries generate_explicit 1000 1000 100000 100000 1
tc  huge_grid_only_eaglevision generate_explicit 1000 1000 100000 100000 0
tc  small_grid_few_queries generate_explicit 1 1 1 10 1
tc  small_grid_many_queries generate_explicit 1 1 1 100000 1
tc  medium_grid_large_range generate_explicit 100 100 500 100 1
tc  medium_grid_small_range generate_explicit 100 100 500 100 1
tc  random1 generate_random
tc  random2 generate_random
tc  random3 generate_random