# -*- coding: utf-8 -*- 
str = "my name is freeman dig cai";
2
print str.split( );
3
print str.split(' ',0);
4
print str.split('e', 1);
5
print str.split(' ', 2);
['my', 'name', 'is', 'freeman', 'dig', 'cai']
['my name is freeman dig cai']
['my nam', ' is fr', '', 'man dig cai']
['my', 'name', 'is freeman dig cai']




aList = [123, 'xyz', 'zara', 'abc','opq'];


print "B List : ", aList.pop(0);

print "A List : ", aList.pop(1);

print "B List : ", aList.pop(2);

print "B List : ", aList.pop(-1)


##-------------打印index 为偶数的元素
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

a=[]
for t in range(len(change)):
    if (t%2) == 0:
        a.append(change[t])         
     
print a

