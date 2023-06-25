x=[1,2,3,"Simplilearn"]
length = 0
i=0
try:
    while x[i]:
        length +=1
        i+=1
except IndexError:
    print(length)