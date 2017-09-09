#!/usr/bin/env python3

"""context.py



Author: Curtis Belmonte
"""

import os
import sys

sys.path.insert(0,
                os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from common import (
    alphabet,
    arithmetic,
    arrays,
    calendar,
    combinatorics,
    digits,
    divisors,
    expansion,
    matrices,
    primes,
    probability,
    sequences,
    utility,
)
