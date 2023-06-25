from threading import *
def show():
    print("This is a child thread")
t=Thread(target= show())
t.start()
print("This is the parent thread")
#t.stop()