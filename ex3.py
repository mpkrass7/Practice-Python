#Appends numbers from list a to list b if they are less than five

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []

for number in a:
    if number < 5:
        print number
        b.append(number)
print b

#function that appends numbers from list A to list B if they are less than the input integer

def list_lower():
    try:
        given_number = int(raw_input("Please provide an integer with a maximum of two digits> "))
        for number in a:
            if number < int(given_number):
                print number
                b.append(number)
        print b
    except ValueError:
        print "That is not an integer"
        list_lower()
list_lower()
