#task 1
file=open('sample.txt','r')
reading_file=file.read()
print("reading file content:\n",reading_file)
file.close()

try:
    file=open('not.txt','r')
    reading_file=file.read()
    print("reading file content:\n",reading_file)
    file.close()
except :
    print("ERROR: the file 'not.txt' was not found")












# task 2
a= input("Enter text to write to the file: ")
file=open('output.txt', 'w')
writing_file = file.write(a + '\n')
print(writing_file)
file.close()

b=input("Enter additional text to append: ")
file1=open('output.txt', 'a')
appending_file = file1.write(b + '\n')
print(appending_file)
file1.close()


file2=open('output.txt', 'r')
reading_file = file2.read()
print("Final content of output.txt:\n", reading_file)
