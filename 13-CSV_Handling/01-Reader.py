import csv

path = 'names.csv'

#csv_file = open(path,'r')

with open(path,'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for row in csv_reader:
        print(row[0],row[1])
