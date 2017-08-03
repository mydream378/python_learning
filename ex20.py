# -*- coding: utf-8 -*- 

from sys import argv

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)
## 任何文件操作 都需要 先打开

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

# rewind(current_file)  ##通过使用 seek() 【方法用于移动文件读取指针到指定位置。】 使得指针回归 --> 定位
## seek(0) 和readline() 往往同时使用。 而且 readline每执行一次，往下扫描一行。

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)