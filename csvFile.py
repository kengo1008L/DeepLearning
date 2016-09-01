#coding:utf-8
import csv   #csvモジュールをインポートする

f = open('saito.csv', 'rb')

dataReader = csv.reader(f)
listData = []
for row in dataReader:
	if row[2] != "" and row[2] != 'NULL':
   		listData.append(row[2].split(','))
print listData



f = open('writeData.csv', 'ab')
wf = csv.writer(f)
wf.writerows(listData)
f.close()

# f = open('writeData2.csv', 'ab')
# wf = csv.writer(f)
# wf.writerows([num1,num2])
# f.close()



