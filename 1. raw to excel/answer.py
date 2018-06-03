#!/usr/bin/python

from xlsxwriter import Workbook

workbook = Workbook('answer.xlsx')
worksheet = workbook.add_worksheet()

id=0

for assessment in range(12):
	for question in range(10):
		try:
			file_name1 = "raw/" + str(assessment+1) + "." + str(question+1)
			file_name2 = "scores/" + str(assessment+1) + "." + str(question+1) + "/ave"
			
			file1 = open(file_name1, "r") 
			file2 = open(file_name2, "r")

			lines1 = file1.readlines() 
			lines2 = file2.readlines() 

			for line in range(len(lines1)):
				id+=1
				data = lines1[line].split(" ",1)
				
				print data[0]
				print data[1]
				
				worksheet.write(id,0, assessment+1)
				worksheet.write(id,1, question+1)
				worksheet.write(id,2, id)
				worksheet.write(id,3, data[1].decode('latin1'))
				worksheet.write(id,4, lines2[line])
				
		except IOError:
			print "the file cannot be opened"

print id

workbook.close()