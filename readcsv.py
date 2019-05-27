import csv
import os
import sys
import json



# csv_file = csv.reader(open('/Users/dujia/mswork/js/jst/datasets.csv','rU'))
# print(csv_file)
# for s in csv_file:
#     print(s)

# dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
#
# while True:
#     line = sys.stdin.readline()
#     line = line.replace('\n', '')
#     if dict.keys().__contains__(line):
#         print(dict[line])
#     else: break

cwd = os.getcwd()
print("Current folder is %s" % (cwd))

csvfile = open(cwd + '/datasets.csv', 'r')

reader = [each for each in csv.DictReader(csvfile, delimiter='\t')]  # 这里设置分号为分隔符
# j = json.dumps(reader)
#
file_handle = open('/Users/dujia/PycharmProjects/mskjjs/result.txt', mode='w')
# file_handle.write(j)

# print(j)

# row = reader[0]
# print(row)
# print(row['ANN_DT'])

for row in reader:
    print(row['S_INFO_COMPNAME'] + ' ' + row['B_INFO_CREDITRATING'] + ' '
          + row['REPORT_PERIODB'] + ' ' + row['TOT_LIAB'] + ' ' + row['TOT_CUR_ASSETS'])
    file_handle.writelines(row['S_INFO_COMPNAME'] + ' ' + row['B_INFO_CREDITRATING'] + '\n')
csvfile.close()
