

print "Type the filename again:"


file_again = raw_input(">ab ")     ## actually the two lines can be simplified to ##   txt_again =  raw_input(">ab ")

txt_again = open(file_again)
print txt_again.read()
print txt_again.close()