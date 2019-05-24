import csv
import os

# csv_file = csv.reader(open('/Users/dujia/mswork/js/jst/datasets.csv','rU'))
# print(csv_file)
# for s in csv_file:
#     print(s)

cwd = os.getcwd()
print("Current folder is %s" % (cwd))

csvfile = open('/Users/dujia/mswork/js/jst/datasets.csv', 'r')
reader = [each for each in csv.DictReader(csvfile, delimiter='\t')]  # 这里设置分号为分隔符

for row in reader:
    print(row['S_INFO_COMPNAME'] + ' ' + row['B_INFO_CREDITRATING'] + ' ' + row['REPORT_PERIODB'])
csvfile.close()
