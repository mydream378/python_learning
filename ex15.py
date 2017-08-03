# -*- coding: utf-8 -*- 

from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:" ## 试试中文
file_again = raw_input(">ab ")     ## actually the two lines can be simplified to ##   txt_again =  raw_input(">ab ")

txt_again = open(file_again)

print txt_again.read()