#!/usr/bin/python

from math import pow, isnan
from MySQLdb import connect
from xlsxwriter import Workbook
from scipy.stats import pearsonr
from model.Skenario import Skenario
from model.Performa import Performa

def worksheetWrite(worksheet, count, row):
	worksheet.write(count,0, row[0])
	worksheet.write(count,1, row[1])
	worksheet.write(count,2, row[2])
	worksheet.write(count,3, row[3])
	
	worksheet.write(count,4, row[4])	
	worksheet.write(count,5, row[5])
	worksheet.write(count,6, row[6])
	worksheet.write(count,7, row[7])
	
	worksheet.write(count,8, row[8])
	worksheet.write(count,9, row[9])	
	worksheet.write(count,10, row[10])
	worksheet.write(count,11, row[11])
	
	worksheet.write(count,12, row[12])
	worksheet.write(count,13, row[13])
	worksheet.write(count,14, row[14])	
	worksheet.write(count,15, row[15])
	
	worksheet.write(count,16, row[16])
	worksheet.write(count,17, row[17])
	worksheet.write(count,18, row[18])	
	worksheet.write(count,19, row[19])

#main

#prepare database connection
db = connect("localhost","root","","db_asas" )
cursor = db.cursor()

for i in range(?, ?):
	id_skenario = i
	skenario = Skenario(id_skenario)

	workbook = Workbook('skenario/skenario_' + str(id_skenario) + '.xlsx')
	worksheet = workbook.add_worksheet()

	sql = skenario.getQuery()
	cursor.execute(sql)
	score_list = cursor.fetchall()

	#init mae
	mae_tf_idf = 0
	mae_widf = 0
	mae_midf = 0

	#init korelasi
	x = []
	y_tf_idf = []
	y_widf = []
	y_midf = []

	#init akurasi
	performa_2 = Performa(id_skenario, 2)
	performa_3 = Performa(id_skenario, 3)
	performa_6 = Performa(id_skenario, 6)
	performa_11 = Performa(id_skenario, 11)

	count = 0
	for row in score_list:
		
		worksheetWrite(worksheet, count, row)
		
		#prepare mae
		mae_tf_idf += abs(row[0]-row[1])
		mae_widf += abs(row[0]-row[2])
		mae_midf += abs(row[0]-row[3])
		
		#prepare korelasi
		x.append(row[0])
		y_tf_idf.append(row[1])
		y_widf.append(row[2])
		y_midf.append(row[3])
		
		#prepare performa
		performa_2.checkRelevantScore(row)
		performa_3.checkRelevantScore(row)
		performa_6.checkRelevantScore(row)
		performa_11.checkRelevantScore(row)
		
		count += 1
		
	performa_2.cleanContigency()
	performa_3.cleanContigency()
	performa_6.cleanContigency()
	performa_11.cleanContigency()
	
	#count mae
	mae_tf_idf = mae_tf_idf/count
	mae_widf = mae_widf/count
	mae_midf = mae_midf/count

	#count korelasi
	korelasi_tf_idf = pearsonr(x, y_tf_idf)[0]
	korelasi_widf = pearsonr(x, y_widf)[0]
	korelasi_midf = pearsonr(x, y_midf)[0]

	#count performa
	performa_2.countPerforma()
	performa_3.countPerforma()
	performa_6.countPerforma()
	performa_11.countPerforma()
		
	#insert mae
	sql = "INSERT INTO `mae`(`ID_SCENARIO`, `TF_IDF`, `WIDF`, `MIDF`) VALUES (%d,%f,%f,%f)" %(id_skenario, mae_tf_idf, mae_widf, mae_midf)
	cursor.execute(sql)
	db.commit()
	
	if isnan(korelasi_tf_idf):
		korelasi_tf_idf = 0
	if isnan(korelasi_widf):
		korelasi_widf = 0
	if isnan(korelasi_midf):
		korelasi_midf = 0
	
	#insert pearson
	sql = "INSERT INTO `pearson`(`ID_SCENARIO`, `TF_IDF`, `WIDF`, `MIDF`) VALUES (%d,%f,%f,%f)" %(id_skenario, korelasi_tf_idf, korelasi_widf, korelasi_midf)
	cursor.execute(sql)
	db.commit()
	
	#insert performa
	performa_2.insert(cursor, db)
	performa_3.insert(cursor, db)
	performa_6.insert(cursor, db)
	performa_11.insert(cursor, db)
		
#disconnect from server
db.close()

workbook.close()