weight = int(input("Weight: "))
conv_weight = input("(K)g or (L)bs: ")
if conv_weight == "K":
    print("Weight in Lbs: " + str(weight*2.20))
elif conv_weight == "k":
    print("Weight in Lbs: " + str(weight * 2.20))
if conv_weight == "L":
    print("Weight in KGs: " + str(weight / 2.20))
elif conv_weight == "l":
    print("Weight in KGs: " + str(weight / 2.20))