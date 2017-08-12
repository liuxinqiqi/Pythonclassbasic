import csv

#writer = csv.writer(open('csvfile1.xls','wb'))
reader = csv.reader(open('csvfile1.xls','rb'))

#writer.writerow(['a','b','c'])

for line in reader:
    print line
