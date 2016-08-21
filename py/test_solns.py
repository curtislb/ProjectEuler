#!/usr/bin/env python3

"""test_solns.py

Module for testing the correctness and runtime of problem solutions.

Author: Curtis Belmonte
"""

import argparse
import importlib
import sys
import time


ANSWER_FILE = '../input/answers.txt'


def answers_from_file(answer_file):
    """Loads problem answers from a file and returns them as a dictionary."""
    answers = {}
    with open(answer_file) as f:
        for line in f:
            tokens = line.rstrip().split()
            prob_num = tokens[0]
            solution = int(tokens[1])
            answers[prob_num] = solution
    return answers


def main():
    # parse optional and positional arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--skip', action='store_true',
        help='test all except the following problems')
    parser.add_argument('problem_nums', metavar='prob_num', type=int,
        nargs='*', help='problem number of a solution to be tested')
    args = parser.parse_args()

    answers = answers_from_file(ANSWER_FILE)

    # determine the problem numbers to be tested
    if len(args.problem_nums) == 0:
        problem_nums = sorted(answers.keys())
    elif args.skip:
        problem_nums = set(answers.keys())
        for num in args.problem_nums:
            problem_nums.remove('{:03d}'.format(num))
        problem_nums = sorted(list(problem_nums))
    else:
        problem_nums = ['{:03d}'.format(num) for num in args.problem_nums]
    
    pass_count = 0
    for problem_num in problem_nums:
        if problem_num not in answers:
            sys.stderr.write('Problem {}: No answer\n'.format(problem_num))
            continue

        sys.stdout.write('Testing Problem {}...'.format(problem_num))
        sys.stdout.flush()

        # import the problem module and ensure its solve function exists
        module_name = 'problem_' + problem_num
        try:
            module = importlib.import_module(module_name)
            module.solve
        except:
            print('FAILED')
            sys.stderr.write('Problem {}: No solution\n'.format(problem_num))
            continue

        # run and time the problem solution
        try:
            start = time.time()
            answer = module.solve()
            total_time = time.time() - start
        except Exception as e:
            print('FAILED')
            sys.stderr.write('Problem {}: Exception\n'.format(problem_num))
            sys.stderr.write(str(e) + '\n')
            continue
        
        # check if solution matches correct answer for the problem
        if answer == answers[problem_num]:
            print('PASSED ({:6.3f} s)'.format(total_time))
            pass_count += 1
        else:
            print('FAILED')
            sys.stderr.write(
                'Problem {}: Answer {} != {}\n'.format(
                    problem_num,
                    answer,
                    answers[problem_num]
                )
            )

    print('-' * 40)
    print('Solutions passed {}/{} tests'.format(pass_count, len(problem_nums)))


if __name__ == '__main__':
    main()
