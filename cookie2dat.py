#!/usr/bin/python3
'''
Convert "cookie" files into "dat" files for fortune.
This script requires python3 >= 3.6
Copyright (C) 2018 Mo Zhou <cdluminate@gmail.com>
'''
from typing import *
import glob
import os


def delComment(lines: List[str], result: List[str], state: bool = False) -> List[str]:
    '''
    delete comments from the given list. Note, it only deletes the
    first consecutive lines which starts with # . Any line starts with #
    after that won't be changed.
    '''
    if not lines:
        return result
    else:
        if not state:
            if lines[0].startswith('#'):
                return delComment(lines[1:], result, False)
            else:
                return delComment(lines[1:], result + [lines[0]], True)
        else:
            return delComment(lines[1:], result + [lines[0]], True)


def cookie2dat(src: str) -> None:
    '''
    Read "cookie" and do preprocessing. :src: refers to source file path.
    '''
    dest = src.replace('.cookie', '.dat')
    with open(src, 'r') as fsrc, open(dest, 'w') as fdest:
        fdest.writelines(delComment(fsrc.readlines(), [], False))
    print(f'{__file__}: Converted {src} -> {dest}')


if __name__ == '__main__':

    cookies = glob.glob('./**/**.cookie', recursive=True)
    print(f'{__file__}: Found {len(cookies)} cookie files')
    for cookie in cookies:
        cookie2dat(cookie)
