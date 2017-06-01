##file = open("demo.txt",'r')
##a = file.read()
##print(a)


file_writer = open("demo_1.txt",'w')
str = file_writer.write("Hello python with file handling")
file_writer.close()


file_reader = open("demo_1.txt",'r')
a = file_reader.read()
print(a)

file_reader.close()
