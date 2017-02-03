#tells whether an input string is a palindrome

palin_check = raw_input("Type something you think may be a Palindrome ")
print palin_check
s = []
count = 0
for character in palin_check:
    count += 1
    #print "letter", count, ":", character
    s.insert(0,character)
reverse = ''.join(s)
print reverse
if reverse == palin_check:
    print "\'" + palin_check + "\' is a palindrome"
else:
    print "\'" + palin_check + "\' is not a palindrome"
