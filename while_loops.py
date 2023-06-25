val = int(input("Enter a multiple of 7: "))
while (val%7 != 0):
    print("%d is a not multiple of 7" % val)
    val = int(input("Enter a multiple of 7: "))
else:
    print("%d is a multiple of 7" %val)