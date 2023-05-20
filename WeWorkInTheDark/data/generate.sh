#!/bin/bash
USE_SCORING=0
. ../../_testdata_tools/gen.sh

use_solution WeWorkInTheDark.py              # Use ../submissions/accepted/js_100.cpp to generate answer files

compile generate_random.py
compile generate_explicit.py

# Generate answers to sample cases
sample 1


tc  random1 generate_random
tc  random2 generate_random
tc  random3 generate_random
