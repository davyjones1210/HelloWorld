r = int(input("Enter number of rows: "))
c = int(input("Enter number of columns: "))
x=[]
val=[]
for i in range(0,r):
    for j in range(0,c):
        val.insert(j, int(input(f"Enter the {i} * {j} element of x: ")))
    x.insert(i,val)
    val = []
y=[]
for i in range(0,r):
    for j in range(0,c):
        val.insert(j, int(input(f"Enter the {i} * {j} element of y: ")))
    y.insert(i, val)
    val=[]
print(x)
print(y)
sum=[]
for i in range(0,r):
    for j in range(0,c):
        val.insert(j, x[i][j] + y[i][j])
    sum.insert(i,val)
    val=[]
print(sum)
