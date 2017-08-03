ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:              
    next_one = more_stuff.pop() 
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There's %d items now." % len(stuff)

#  # -*- coding: utf-8 -*- 
# 使用for loop改写

#t=len(stuff)
#for t in range(len(stuff),10):
#    next_one = more_stuff.pop()
##   print "Adding: ", next_one
#    stuff.append(next_one)
#    t+=1
   
    
#print "There's %d items now." % len(stuff)


print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
print stuff.pop()
print ' '.join(stuff) # what? cool! 
 # Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。

print '#'.join(stuff[3:5]) # super stellar!
