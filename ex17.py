# -*- coding: utf-8 -*- 

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

## 先打开（open）----读取（read）--

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)

## exists。这个命令将文件名字符串作为参数，如果文件存在的话，它将返回 True，否则将返回 False。

## 我使用了一个叫 cat 的东西，这个古老的命令的用处是将两个文件“连接(con*cat*enate)”到一起，
## 不过实际上它最大的用途是打印文件内容到屏幕上。你可以通过 man cat 命令了解到更多信息。 
## eg.   cat test.text
print "Ready, hit RETURN to continue, CTRL-C to abort."

raw_input("are you ready?")

out_file = open(to_file, 'w')

## It's really just a string with a character in it for the kind of mode for the file. 
##If you use 'w' then you're saying "open this file in 'write' mode",
 ## thus the 'w' character. There's also 'r' for "read", 'a' for append, and modifiers on these.

 ## 需要先“打开” out_file 文件夹———才可以-进行编辑操作---"写入write”
 
out_file.write(indata)    

### 将 in_file 读入的indata， 写入到， out_file 中

## 整个流程-->in_file--> open & read--> indata 过渡 --> out_file--> open & write 

print "Alright, all done."

out_file.close()  ## 删除后 不影响运行结果

in_file.close()
