#!/usr/bin/python

from xlsxwriter import Workbook

workbook = Workbook('question.xlsx')
worksheet = workbook.add_worksheet()

id=0

try:
	file_name1 = "raw/questions"
	file_name2 = "raw/answers"
	
	file1 = open(file_name1, "r") 
	file2 = open(file_name2, "r")

	lines1 = file1.readlines() 
	lines2 = file2.readlines() 

	for line in range(len(lines1)):
		id+=1
		data1 = lines1[line].split(" ",1)
		data2 = lines2[line].split(" ",1)
		
		print data1[0]
		
		worksheet.write(id,0, data1[0].split(".",1)[0])
		worksheet.write(id,1, id)
		worksheet.write(id,2, data1[1].decode('latin1'))
		worksheet.write(id,3, data2[1].decode('latin1'))
		
except IOError:
	print "the file cannot be opened"

print id

workbook.close()