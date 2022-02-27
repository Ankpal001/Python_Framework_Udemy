import os
import csv
os.getcwd()
data = open('BBGW_OPENET_20220202_000107.csv', encoding='utf-8')
csv_data = csv.reader(data)
data_lines = list(csv_data)
#print(data_lines)
print(data_lines[1])
for line in data_lines[0:5]:
    print(line)
data = open('practice_write.csv',mode ='w',newline='')
file_written = csv.writer(data,delimiter = '|')
file_written.writerow(['a','b','c','d'])



print(os.getcwd())
f = open('practicefile.txt','w+')
f.write('How r u')
f.close()

print(os.listdir())
