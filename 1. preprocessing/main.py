#!/usr/bin/python

from MySQLdb import connect
from xml.dom import minidom
from collections import Counter
from preprocessing import preprocessing

#1 = question, 2 = answer key, 3 = answer, 4 = testing, 5 = corpus
source = ?

#prepare database connection
db = connect("localhost","root","","db_asas" )
cursor = db.cursor()

#list document [getDocumentList(sourceID)]
if source == 1 or source == 2:
	sql = "SELECT * FROM question" 
if source == 3:
	sql = "SELECT * FROM answer" 
if source == 4:
	sql = "SELECT * FROM answer WHERE ID_QUESTION = 1" 
if source == 5:	
	sql = "SELECT * FROM corpus WHERE DOMAIN = 'applied science' OR DOMAIN = 'natural sciences'" 
cursor.execute(sql)
document_list = cursor.fetchall()

for document in document_list:

	#fetched result [getDocumentText(document)]
	id = document[0]
	if source == 1 or source == 3 or source == 4:
		text = document[2]
	if source == 2:
		text = document[3]
	if source == 5:
		text = ''
		
		print document[1]
		mydoc = minidom.parse(document[1])
		words = mydoc.getElementsByTagName("w")
		for word in words:
			try:
				w = word.firstChild.data
				w = w.strip().encode('utf-8').decode('latin1')
				w = str(w)
				text += w + ' '
			except (UnicodeEncodeError, AttributeError) as error:
				pass
		
	print "id = %d text = %s" %(id, text)
	
	#insert document [insertDocument(sourceID, documentID)]
	sql = "INSERT INTO `document`(`ID_SOURCE`, `ID_REF`) VALUES (%d, %d)" %(source, id)
	cursor.execute(sql)
	db.commit()
	
	#new document id
	id_document = cursor.lastrowid
	
	#result [preprocessing(text)] + count term [countEachTerm(termList)]
	term_list = preprocessing(text)
	term_list = Counter(term_list)
	#print term_list
	
	#insert term document matrix [insertTermDocumentMatrix(newDocumentID, term, count)]
	for term in term_list:
		sql = "INSERT INTO `term_document_matrix`(`ID_DOCUMENT`, `TERM`, `TF`) VALUES (%d, '%s', %d)" %(id_document, term, term_list[term])
		cursor.execute(sql)
		db.commit()

#disconnect from server
db.close()