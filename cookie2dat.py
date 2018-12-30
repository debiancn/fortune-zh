#!/usr/bin/python3
'''
Convert "cookie" files into "dat" files for fortune.
This script requires python3 >= 3.6
Copyright (C) 2018 Mo Zhou <cdluminate@gmail.com>
'''
from typing import *
import glob
import os


def cookie2dat(src: str) -> None:
    '''
    Read "cookie" and do preprocessing. :src: refers to source file path.
    '''
    dest = src.replace('.cookie', '.dat')
    with open(src, 'r') as fsrc, open(dest, 'w') as fdest:
        contents = fsrc.readlines()
        while contents:
            if contents[0].startswith('#'):
                contents.pop(0)
            else:
                break
        if contents:
            fdest.writelines(contents)
            print(f'Converted {src} -> {dest}')
        else:
            print(f'{src} is empty. skipped')


if __name__ == '__main__':

    cookies = glob.glob('./**/**.cookie', recursive=True)
    print(f'{__file__}: Found {len(cookies)} cookie files')
    for cookie in cookies:
        cookie2dat(cookie)
