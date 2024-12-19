n1 = int(input(" Enter 1st number: "))
n2 = int(input(" Enter 2st number: "))
n3 = int(input(" Enter 3st number: "))

# max of 3
if n1 > n2 > n3 :
    print("n1")
elif n2 > n1 >n3 :
    print("n2")
elif n3> n2 > n1 :
    print("n3")
else :
    print("incorrect numbers")

    # min of 3
if n1 < n2 < n3 :
    print("n1")
elif n2 < n1 < n3 :
    print("n2")
elif n3 < n2 < n1 :
    print("n3")
else :
    print("incorrect numbers")

# среднеарифметическое
averege = (n1 + n2 +n3) / 3
print("averege")
