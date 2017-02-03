# Determines when a user will be 100 hundred
import time

def determiner():
    def inner(X):
        message1 = name + ", you will be 100 years old in " + str((int(year) - age + X))
        print message1
        repeat = raw_input("How many times would you like to see the previous message? ")
        print (("\n" + message1) * int(repeat))
    print "Did you turn %d this year? (y/n) " % age
    answer = raw_input()
    if answer == "y":
        inner(100)
    elif answer == "n":
        inner(99)
    else:
        print "Please type 'y' or 'n' "
        determiner()

name = raw_input("What is your name? ")
print name
print "Your name is %s. Ok, how old are you? " % name
age = int(raw_input())
year = time.strftime("%Y")
determiner()
