#!/usr/bin/env python
# WTFPL 2.0. See LICENSE for more info.
"""
Tiny script that iterates through a bunch of PSF files and strips the length
and fade tags. This is mainly so that I could convert my PSF files to loop
continuously in Audio Overload.
"""
from argparse import ArgumentParser
from glob import glob

def main():
    parser = ArgumentParser(description='Remove length and fade tags from '
                            'PSF files.')
    parser.add_argument('pattern', help='glob-compatible pattern of files to '
                        'parse')
    pattern = parser.parse_args().pattern

    # Yay for nasty code
    for f in glob(pattern):
        with open(f, 'r') as file:
            contents = file.read().splitlines(True)
        with open(f, 'w') as file:
            for line in contents:
                if line.startswith('length') or line.startswith('fade'):
                    line = ''
                file.write(line)



if __name__ == '__main__':
    main()
