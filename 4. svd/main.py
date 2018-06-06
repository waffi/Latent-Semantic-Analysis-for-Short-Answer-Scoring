#!/usr/bin/python

from numpy import save
from MySQLdb import connect
from model.TermDocumentMatrix import TermDocumentMatrix
from model.SingularValueDecomposition import SingularValueDecomposition

#1 = question, 2 = answer key, 3 = answer
source = ?

#prepare database connection
db = connect("localhost","root","","db_asas")
cursor = db.cursor()

sql = "SELECT * FROM term_document_matrix"
cursor.execute(sql)
term_document_matrix = cursor.fetchall()

sql = "SELECT ID_DOCUMENT FROM document"
cursor.execute(sql)
documemt_list = cursor.fetchall()

tdm = TermDocumentMatrix(term_document_matrix, documemt_list)

#create document list containing term
tdm.createTermDictionary()
print tdm.term_dictionary['address'][0].term
		
#create term list
tdm.createTermList()
print tdm.term_list

#create document list
tdm.createDocumentList()
print tdm.documemt_list

#create matrix
tdm.createMatrix()	
matrix_question = tdm.getMatrixQuestion()
matrix_answer_key = tdm.getMatrixAnswerKey()
matrix_answer = tdm.getMatrixAnswer()

if(source == 1):
	matrix = matrix_question
if(source == 2):
	matrix = matrix_answer_key
if(source == 3):
	matrix = matrix_answer
	
#create SVD
svd_tf_idf = SingularValueDecomposition()
svd_widf = SingularValueDecomposition()
svd_midf = SingularValueDecomposition()

svd_tf_idf.generateSVD(matrix['tf_idf'])
svd_widf.generateSVD(matrix['widf'])
svd_midf.generateSVD(matrix['midf'])

save(str(source)+'.svd.tf_idf.u.npy',svd_tf_idf.U)
save(str(source)+'.svd.tf_idf.s.npy',svd_tf_idf.S)
save(str(source)+'.svd.tf_idf.vt.npy',svd_tf_idf.Vt)

save(str(source)+'.svd.widf.u.npy',svd_widf.U)
save(str(source)+'.svd.widf.s.npy',svd_widf.S)
save(str(source)+'.svd.widf.vt.npy',svd_widf.Vt)

save(str(source)+'.svd.midf.u.npy',svd_midf.U)
save(str(source)+'.svd.midf.s.npy',svd_midf.S)
save(str(source)+'.svd.midf.vt.npy',svd_midf.Vt)

save('matrix.question.npy',matrix_question['tf'])
save('matrix.answer_key.npy',matrix_answer_key['tf'])
save('matrix.answer.npy',matrix_answer['tf'])

save('term_list.npy',tdm.term_list)

#disconnect from server
db.close()