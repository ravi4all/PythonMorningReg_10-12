file = open("demo_1.txt",'r')

##a = file.read()
##print(a)

b = file.readlines()
for x in b:
    print(x.strip("\n"))
