#!/usr/bin/env python3
"""
Author : Justin Byers <justin.byers64@gmail.com>
Date   : 2021-01-10
Purpose: Print words that are given
"""

import argparse


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Print words that are given',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='str',
                        help='The given word')

    return parser.parse_args()


def main():
    """
    Determine which article to use based on the given word \
    to print the full sentence with correct grammar.
    """

    args = get_args()

    if args.word.lower().startswith(('a','e','i','o','u')):
        article = 'an'
    else:
        article = 'a'

    return f'Ahoy, Captain, {article} {args.word} off the larboard bow!'


if __name__ == '__main__':
    print(main())
