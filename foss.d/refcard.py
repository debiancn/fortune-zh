# Copyright (C) 2018 Mo Zhou <cdluminate@gmail.com>
import re
import sys
import argparse


def colorize(msg: str):
    msg = re.sub('<replaceable>', '\x1b[0;33m', msg)
    msg = re.sub('</replaceable>', '\x1b[;m', msg)
    msg = re.sub('<literal>', '\x1b[0;36m', msg)
    msg = re.sub('</literal>', '\x1b[;m', msg)
    msg = re.sub('<optional>', '\x1b[1;33m[\x1b[;m', msg)
    msg = re.sub('</optional>', '\x1b[1;33m]\x1b[;m', msg)
    msg = re.sub('<filename>', '\x1b[1;35m', msg)
    msg = re.sub('</filename>', '\x1b[;m', msg)
    msg = re.sub('<command>', '\x1b[1;32m', msg)
    msg = re.sub('</command>', '\x1b[;m', msg)
    msg = re.sub('<ulink (.*)>(.*)</ulink>', '\\2 [\\1]', msg)
    msg = re.sub('<emphasis>', '\x1b[0;31m', msg)
    msg = re.sub('</emphasis>', '\x1b[;m', msg)
    return msg


if __name__ == '__main__':
    ag = argparse.ArgumentParser()
    ag.add_argument('src', type=str)
    ag = ag.parse_args()

    lines = open(ag.src, 'r') .readlines()
    msgid = []
    msgstr = []
    cursor = None
    for line in lines:
        if re.match('^$', line): continue
        if re.match('^#~.*', line): continue
        if re.match('^#.*', line): continue

        if re.match('^msgid.*', line):
            msgid.append('')
            cursor = msgid
            cursor[-1] += eval(line.replace('msgid', ''))
        elif re.match('^msgstr.*', line):
            msgstr.append('')
            cursor = msgstr
            cursor[-1] += eval(line.replace('msgstr', ''))
        else:
            cursor[-1] += eval(line)
    messages = list(reversed(msgstr))
    try:
        for i in range(0, len(messages), 2):
            cmd = colorize(messages[i+1])
            note = colorize(messages[i])

            #print('cmd', cmd)
            #print('note', note)

            padding = '\x1b[1;36m  │\x1b[;m'
            print(padding)
            print(padding, cmd)
            print(padding)
            print(padding, note)
            print(padding)
            print()
            print('                                                             -- Debian 参考卡片')
            print('%')
    except IndexError as e:
        pass
