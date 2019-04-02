#!/usr/bin/env python3

"""test_solns.py

Module for testing the correctness and runtime of problem solutions.
"""

__author__ = 'Curtis Belmonte'

import importlib
import operator
import sys
import time
import traceback
from argparse import ArgumentParser
from typing import Any, List, Mapping, Tuple

import common.combinatorics as comb
import common.primes as prime

# The file from which problem answers will be read
ANSWER_FILE = '../input/answers.txt'

# Threshold values used to organize slow solutions
SLOW_GROUP_SECS = [1, 10, 60]


def answers_from_file(answer_file: str) -> Mapping[str, int]:
    """Loads problem answers from a file and returns them as a dictionary."""
    answers = {}
    with open(answer_file) as input_file:
        for line in input_file:
            tokens = line.rstrip().split()
            prob_num = tokens[0]
            solution = int(tokens[1])
            answers[prob_num] = solution
    return answers


# noinspection PyProtectedMember
def reset_caches() -> None:
    """Clears the value list caches of all common modules."""
    comb._reset_factorial_cache()
    prime._reset_prime_cache()


def main(args: Any) -> None:
    answers = answers_from_file(ANSWER_FILE)

    # determine the problem numbers to be tested
    if len(args.problem_nums) == 0:
        problem_nums = sorted(answers.keys())
    elif args.skip:
        prob_num_set = set(answers.keys())
        for num in args.problem_nums:
            prob_num_set.remove('{0:03d}'.format(num))
        problem_nums = sorted(list(prob_num_set))
    else:
        problem_nums = ['{0:03d}'.format(num) for num in args.problem_nums]
    
    # initialize lists of slow solutions if enabled
    slow_lists: List[List[Tuple[str, float]]] = (
        [[], [], []] if args.list_slow else []
    )

    pass_count = 0    
    for problem_num in problem_nums:
        if problem_num not in answers:
            sys.stderr.write(
                'Problem {0}: No answer in input file\n'.format(problem_num))
            continue

        sys.stdout.write('Testing Problem {0}...'.format(problem_num))
        sys.stdout.flush()

        # import the problem module and ensure its solve function exists
        module_name = 'problem_' + problem_num
        problem = importlib.import_module(module_name)
        if not hasattr(problem, 'solve'):
            print('FAILED')
            sys.stderr.write(
                'Problem {0}: No solve function defined\n'.format(problem_num))
            continue

        # run and time the problem solution
        try:
            reset_caches()
            start = time.time()
            answer = problem.solve()  # type: ignore
            total_time = time.time() - start
        except Exception as e:
            print('FAILED')
            sys.stderr.write(
                'Problem {0}: Failed with {1}\n'.format(
                    problem_num, type(e).__name__))
            traceback.print_exc(file=sys.stderr)
            continue
        
        # check if solution matches correct answer for the problem
        if answer == answers[problem_num]:
            print('PASSED ({0:6.3f} s)'.format(total_time))
            pass_count += 1

            # add solution to slow list if necessary
            if args.list_slow:
                for i in range(-1, -len(slow_lists) - 1, -1):
                    if total_time > SLOW_GROUP_SECS[i]:
                        slow_lists[i].append((problem_num, total_time))
                        break
        else:
            print('FAILED')
            sys.stderr.write(
                'Problem {0}: Expected {1}, but got {2}\n'.format(
                    problem_num,
                    answers[problem_num],
                    answer))

    # print summary line with number of tests passed
    print('-' * 40)
    print('Solutions passed {0}/{1} tests'.format(
        pass_count,
        len(problem_nums)))

    # print lists of slow solutions if enabled
    if args.list_slow:
        slow_list_names = [
            'Slow-ish solutions (>{0} s)'.format(SLOW_GROUP_SECS[0]),
            'Slow solutions (>{0} s)'.format(SLOW_GROUP_SECS[1]),
            'Too slow solutions (>{0} s)'.format(SLOW_GROUP_SECS[2]),
        ]
        for i, slow_list in enumerate(slow_lists):
            if slow_list:
                slow_list.sort(key=operator.itemgetter(1), reverse=True)
                print('\n{0}:'.format(slow_list_names[i]))
                for prob_num, total_time in slow_list:
                    print('- Problem {0} ({1:6.3f} s)'.format(
                        prob_num,
                        total_time))


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        '-l', '--list-slow',
        action='store_true',
        help='show a summary list of slow solutions')
    parser.add_argument(
        '-s', '--skip',
        action='store_true',
        help='test all except the following problems')
    parser.add_argument(
        'problem_nums',
        metavar='prob_num',
        type=int,
        nargs='*',
        help='problem number of a solution to be tested')
    main(parser.parse_args())
