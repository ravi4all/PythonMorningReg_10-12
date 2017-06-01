file = open("my_csv.csv",'r')
a = file.read()
split_data = a.split(",")
print(str(split_data).strip(","))

for s in split_data:
    print(s)
