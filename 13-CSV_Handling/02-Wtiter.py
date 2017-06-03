import csv

data = ['FirstName,LastName'.split(","),
        'Sachin,Tendulkar'.split(","),
        'Virat,Kohli'.split(","),
        'MS,Dhoni'.split(","),
        'John,Cena'.split(","),
        'Mike,Tyson'.split(",")]

path = 'names.csv'

with open(path,'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')

    for line in data:
        csv_writer.writerow(line)
