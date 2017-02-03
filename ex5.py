import random

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
b2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c= []
d= []

def list_maker():
    count = 0
    first = []
    second = []
    common_items = []

    firstAppendCount = random.randint(5, 20)
    secondAppendCount = random.randint(5, 20)

    while len(first) < firstAppendCount:
        first.append(int(random.random()*100))
    while len(second) < secondAppendCount:
        second.append(int(random.random()*100))

    print first
    print second

    for item in first:
        if item in second:
            count += 1
            print item, "is in both lists"
            common_items.append(item)
            second.remove(item)
    if len(common_items) > 1:
        print count, "numbers are in both lists"
        print common_items
    elif len(common_items) == 1:
        print count, "number is in both lists"
    else:
        print "The two lists do not share any numbers"
list_maker()


'''for number in a:
    x = number
    for number2 in b:
        if number2 == x:
            print "%d is in both lists" % number
            c.append(x)
            print "Removing %d from second list" % number
            b.remove(x)
print c

for item in a:
    y = item
    if y in b2:z
        print y, "is in both lists"
        d.append(y)
        b2.remove(y)
print d'''
