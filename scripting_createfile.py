from os import path
def createFile(dest):
    if not(path.isfile(dest)):
        f=open(dest, 'w')
        f.write("Welcome to Python scripting")
        f.close()

dest = "C:\\Users\\Davy Jones\PycharmProjects\\HelloWorld\\sample.txt"

createFile(dest)
print("File created")