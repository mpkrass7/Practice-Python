#Ask the user for a number.
#Depending on whether the number is even or odd,
#print out an appropriate message to the user.
#Hint: how does an even / odd number react differently when divided by 2?
#Extra 1: If number is a multiple of 4, print another message
#Extra 2: Ask the user for two numbers, one to check (num) and one to divide by (check)
#if check divides evenly by num, tell that to user. Otherwise print something else

#def check_int(x):
#    if x != int(x):
#        print "The number is not an integer"
#        given_number = int(raw_input("Please type an integer as a base number: "))
#    else:
#        print "The number is an integer"
#Function added for extra 1

def even_odd():
    while True:
        try:
            given_number = int(raw_input("Please type an integer as a base number: "))
            break
        except ValueError:
            print ("Not a valid number. Try again")

    print given_number

    #check_int(given_number)

    if (given_number % 2) != 0:
        print "The number is odd"
    elif (given_number % 4) == 0:
        print "The number is a multiple of four"
    elif (given_number % 2) == 0:
        print "The number is even"
    second_number = float(raw_input("Please provide an integer as a divisor "))

    #check_int(second_number)

    if (given_number % second_number) != 0:
        print "The numbers do not divide evenly"
    else:
        print "The numbers divide evenly"
even_odd()
#function created for extra two
