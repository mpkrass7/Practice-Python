#Takes a user input number and returns all of it's divisors. Froze computer after typing in a number ~581000000

def int_checker():
    while True:
        try:
            a = int(raw_input("Input an integer to find its divisors> "))
        except ValueError:
            print "That is not an integer"
        else:
            return a

def divisors():
    divisor = int_checker()
    x = range(1, divisor+1)
    y = []
    for number in x:
        if divisor % number == 0:
            y.append(number)
    print y
divisors()
