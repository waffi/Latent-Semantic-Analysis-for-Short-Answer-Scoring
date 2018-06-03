#!/usr/bin/python

from MySQLdb import connect
from collections import Counter
from preprocessing import preprocessing

#1 = question, 2 = answer key, 3 = answer, 4 = sample
source = 1

#prepare database connection
db = connect("localhost","root","","db_asas" )
cursor = db.cursor()

#list document
if source == 1 or source == 2:
	sql = "SELECT * FROM question" 
if source == 3:
	sql = "SELECT * FROM answer" 
if source == 4:
	sql = "SELECT * FROM answer WHERE ID_QUESTION = 1" 
cursor.execute(sql)
document_list = cursor.fetchall()

for document in document_list:

	#fetched result
	id = document[0]
	if source == 1 or source == 3 or source == 4:
		text = document[2]
	if source == 2:
		text = document[3]
	print "id = %d text = %s" %(id, text)
	
	#insert document
	sql = "INSERT INTO `document`(`ID_SOURCE`, `ID_REF`) VALUES (%d, %d)" %(source, id)
	cursor.execute(sql)
	db.commit()
	
	id_document = cursor.lastrowid
	
	#result preprocessing + count term
	term_list = preprocessing(text)
	term_list = Counter(term_list)
	#print term_list
	
	#insert term document matrix
	for term in term_list:
		sql = "INSERT INTO `term_document_matrix`(`ID_DOCUMENT`, `TERM`, `TF`) VALUES (%d, '%s', %d)" %(id_document, term, term_list[term])
		cursor.execute(sql)
		db.commit()
	
#disconnect from server
db.close()