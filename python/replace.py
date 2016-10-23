#!usr/bin/env python3
# -*- coding: utf-8 -*-

#
# 遍历程序所在文件夹下所有目录,替换文件中的字符串.
#

import os

def replace_file_str(file, cur, replace):
    lines = []
    with open(file, 'rt') as f:
        [lines.append(line.replace(cur, replace)) for line in f]
    with open(file, 'wt') as f:
        f.writelines(lines)
    print(file + ' process succeed!')


def replace_dir_str(dir, cur = '', replace=''):
    for name in os.listdir(dir):
        name = os.path.join(dir, name)
        if os.path.isdir(name):
            replace_dir_str(name, cur, replace)
        elif os.path.isfile(name):
            replace_file_str(name, cur, replace)


if __name__ == '__main__':
    dir = os.getcwd()
    cur = ''
    replace = ''

    while not cur:
        cur = input('old str:').strip()
    print(cur)
    while not replace:
        replace = input('new str:').strip()

    print(replace)

    for name in os.listdir(dir):
        # 忽略当前目录下的隐藏文件夹和所有文件
        if os.path.isdir(os.path.join(dir, name)) and not name.startswith('.'):
            replace_dir_str(name, cur, replace)

