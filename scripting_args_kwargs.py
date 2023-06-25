def func1(*args, **kwargs):
    for i in kwargs.items():
        print(i)

#func1(10,20,30,80,40,26,'asfdfgf')
func1(a=10,b=20,c=30)