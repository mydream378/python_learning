from sys import argv
script,filename=argv
txt=open(filename)
print "filename %r" %(filename)
print txt.read()
txt.close()
print "Change the file name"
file_again=raw_input('>')
print "New file name %r" %(file_again)
txt_again=open(file_again)
print txt_again.read()
txt_again.close()