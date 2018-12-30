'''
https://www.debian.org/doc/manuals/debian-reference/debian-reference.en.txt
'''
__URL__ = 'https://www.debian.org/doc/manuals/debian-reference/debian-reference.zh-cn.txt'
import re
import os
from subprocess import call

White   = lambda x: '\x1b[37;1m' + x + '\x1b[;m'
Green   = lambda x: '\x1b[32;1m' + x + '\x1b[;m'
Red     = lambda x: '\x1b[31;1m' + x + '\x1b[;m'
Cyan    = lambda x: '\x1b[36;1m' + x + '\x1b[;m'
Yellow  = lambda x: '\x1b[33;1m' + x + '\x1b[;m'
yellow  = lambda x: '\x1b[33;0m' + x + '\x1b[;m'

def colorize(line):
    if re.match('^\s*\$.*', line):
        return Green(line)
    elif re.match('^\s*#.*', line):
        return Cyan(line)
    else:
        line = re.sub('注意', '\x1b[33;1m注意\x1b[m', line)
        line = re.sub('小心', '\x1b[33;1m小心\x1b[m', line)
        line = re.sub('提示', '\x1b[36;1m提示\x1b[m', line)
        line = re.sub('警告', '\x1b[31;1m警告\x1b[m', line)
        line = re.sub('^(\s*)([\d\.]*)', Yellow('\\1\\2'), line)
        return line


if __name__ == '__main__':

    if not os.path.exists('debian-reference.zh-cn.txt'):
        call(['wget', __URL__, '-O', 'debian-reference.zh-cn.txt'])

    lines = open('debian-reference.zh-cn.txt', 'r').readlines()
    for i, line in enumerate(lines):
        line = line.rstrip()
        if re.match(r'^\S+.*', line) and i > 0:
            print('  --                        Osamu Aoki (青木修), Debian 参考手册（版本 2.73）')
            print('%')
            print(White(line))
        else:
            line = colorize(line)
            print(line)
