#!/usr/bin/python

from MySQLdb import connect
from model.TermDocument import TermDocument
from model.TermWeighting import TermWeighting

#1 = question, 2 = answer key, 3 = answer, 4 = testing, 5 = corpus
source = ?

#prepare database connection
db = connect("localhost","root","","db_asas" )
cursor = db.cursor()

tw = TermWeighting()

#get total document [getTotalDocument(sourceID)]
sql = "SELECT COUNT(*) FROM document d WHERE d.ID_SOURCE = %d" %(source)
cursor.execute(sql)
total_document = cursor.fetchone()[0]

#[setTotalDocument(totalDocument)]
tw.setTotalDocument(total_document)
print 'total_document: ' + str(total_document)

#get count documents each terms [getCountDocumentEachTerm(sourceID)]
sql = "SELECT term, COUNT(*) FROM term_document_matrix m, document d WHERE m.ID_DOCUMENT = d.ID_DOCUMENT AND d.ID_SOURCE = %d GROUP BY m.TERM" %(source)
cursor.execute(sql)
term_list = cursor.fetchall()
		
#[setCountDocumentDictionary(termList)]
tw.setCountDocumentDictionary(term_list)
#print tw.count_document_dictionary['approach']
	
#get sum term frequency each term [getSumTermFrequencyEachTerm(sourceID)]
sql = "SELECT term, sum(tf) FROM term_document_matrix m, document d WHERE m.ID_DOCUMENT = d.ID_DOCUMENT AND d.ID_SOURCE = %d GROUP BY m.TERM" %(source)
cursor.execute(sql)
sum_tf_list = cursor.fetchall()
		
#[setSumTermFrequencyDictionary(sumTfList)]
tw.setSumTfDictionary(sum_tf_list)
#print tw.sum_tf_dictionary['approach']
	
#get term document matrix [getTermDocumentMatrix(sourceID)]
sql = "SELECT * FROM term_document_matrix m, document d WHERE m.ID_DOCUMENT = d.ID_DOCUMENT AND d.ID_SOURCE = %d" %(source)
cursor.execute(sql)
term_document_matrix = cursor.fetchall()

#count term weighting
for row in term_document_matrix:

	td = TermDocument(row)
	
	td.idf = tw.get_idf(td.term)
	td.tf_idf = tw.get_tf_idf(td.term, td.tf)
	td.widf = tw.get_widf(td.term, td.tf)
	td.midf = tw.get_midf(td.term, td.tf)
	
	print str(td.id_document) + " - " + str(td.id_term)
	print td.term + " : " + str(td.tf_idf) + "-" + str(td.widf) + "-" + str(td.midf)
	
	sql = "UPDATE `term_document_matrix` SET `IDF`=%f, `TF_IDF`=%f, `WIDF`=%f, `MIDF`=%f WHERE ID_TERM = %d" %(td.idf, td.tf_idf, td.widf, td.midf, td.id_term)
	cursor.execute(sql)
	db.commit()
	
#disconnect from server
db.close()