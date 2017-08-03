
# -*- coding: utf-8 -*- 

# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %s, arg2: %s" % (arg1, arg2)  
    
## 比较print_two 使用[%S]和 print_two_again 使用[%r],printout 

##  print_two--->        arg1: Zed, arg2: Shaw
## print_two_again--->   arg1: 'Zed', arg2: 'Shaw'

# ok, that *args is actually pointless, we can just do this
def print_two_again (arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2) 
    
    ##  ?? the printout result--> arg1: 'Zed', arg2: 'Shaw', why with a single quote??


# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one takes no arguments
def print_none():
    print "I got nothin'."


print_two("Zed","Shaw")  ##  double-quotes are needed, coz it indicates the arg is a [string], not a variable.
print_two_again("Zed","Shaw")
print_one("First!")
print_none()

##  每个【:】的重要性