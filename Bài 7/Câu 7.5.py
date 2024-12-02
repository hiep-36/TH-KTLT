print("Le Hoa Hiep")
print("235752021610073")
def file_append_and_display(fname):
    with open(fname, "a") as myfile:
        myfile.write("Python Exercises\n")
        myfile.write("Java Exercises\n")
    with open(fname, "r") as myfile:
        print(myfile.read())  
file_append_and_display('abc.txt')
