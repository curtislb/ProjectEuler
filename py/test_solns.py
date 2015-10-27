"""test_solns.py

Module for testing the correctness and runtime of problem solutions.

@author: Curtis Belmonte
"""

import importlib
import sys
import time


answers = {
    '001': 233168,
    '002': 4613732,
    '003': 6857,
    '004': 906609,
    '005': 232792560,
    '006': 25164150,
    '007': 104743,
    '008': 23514624000,
    '009': 31875000,
    '010': 142913828922,
    '011': 70600674,
    '012': 76576500,
    '013': 5537376230,
    '014': 837799,
    '015': 137846528820,
    '016': 1366,
    '017': 21124,
    '018': 1074,
    '019': 171,
    '020': 648,
    '021': 31626,
    '022': 871198282,
    '023': 4179871,
    '024': 2783915460,
    '025': 4782,
    '026': 983,
    '027': -59231,
    '028': 669171001,
    '029': 9183,
    '030': 443839,
    '031': 73682,
    '032': 45228,
    '033': 100,
    '034': 40730,
    '035': 55,
    '036': 872187,
    '037': 748317,
    '038': 932718654,
    '039': 840,
    '040': 210,
    '041': 7652413,
    '042': 162,
    '043': 16695334890,
    '044': 5482660,
    '045': 1533776805,
    '046': 5777,
    '047': 134043,
    '048': 9110846700,
    '049': 296962999629,
    '050': 997651,
    '051': 121313,
    '054': 376,
    '055': 249,
}


def main():
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
