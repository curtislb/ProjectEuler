"""test_solns.py

Module for testing the correctness and runtime of problem solutions.

@author: Curtis Belmonte
"""

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
    answers = answers_from_file(ANSWER_FILE)

    # determine the problem numbers to be tested
    if len(sys.argv) == 1:
        problem_nums = sorted(answers.keys())
    else:
        problem_nums = ['{0:03d}'.format(int(arg, 10)) for arg in sys.argv[1:]]

    for problem_num in problem_nums:
        sys.stdout.write('Testing Problem {0}...'.format(problem_num))
        sys.stdout.flush()

        # import the problem module and ensure its main function exists
        module_name = 'problem_' + problem_num
        try:
            module = importlib.import_module(module_name)
            module.main
        except:
            print('FAILED')
            sys.stderr.write('Problem {0}: No solution\n'.format(problem_num))
            continue

        # run and time the problem solution
        try:
            start = time.time()
            answer = module.main()
            total_time = time.time() - start
        except Exception as e:
            print('FAILED')
            sys.stderr.write('Problem {0}: Exception\n'.format(problem_num))
            sys.stderr.write(str(e) + '\n')
            continue
        
        # check if solution matches correct answer for the problem
        if answer == answers[problem_num]:
            print('PASSED ({0:.3f} s)'.format(total_time))
        else:
            print('FAILED')
            sys.stderr.write(
                'Problem {0}: Answer {1} != {2}\n'.format(
                    problem_num,
                    answer,
                    answers[problem_num]
                )
            )


if __name__ == '__main__':
    main()
