#!/bin/bash
USE_SCORING=0
. ../../_testdata_tools/gen.sh

use_solution TvaerThySum.py              # Use ../submissions/accepted/js_100.cpp to generate answer files

compile generate_random.py
compile generate_explicit.py

# Generate answers to sample cases
sample 1
sample 2


tc  random1 generate_random
tc  random2 generate_random
tc  random3 generate_random
tc  edge1 generate_explicit 0
tc  edge2 generate_explicit 1
tc  edge3 generate_explicit 99
tc  edge4 generate_explicit 999
tc  edge-huge1 generate_explicit 9999
tc  edge-huge2 generate_explicit 99999999999999999
