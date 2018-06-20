#!/usr/bin/python

from numpy import save
from MySQLdb import connect
from model.TermDocumentMatrix import TermDocumentMatrix
from model.SingularValueDecomposition import SingularValueDecomposition

#1 = question, 2 = answer key, 3 = answer, 4 = testing, 5 = corpus
source = ?

#prepare database connection
db = connect("localhost","root","","db_asas")
cursor = db.cursor()

sql = "SELECT * FROM `term_document_matrix` tdm, `document` d WHERE tdm.ID_DOCUMENT = d.ID_DOCUMENT"
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
matrix_corpus = tdm.getMatrixCorpus()

print matrix_question['tf'].shape
print matrix_answer_key['tf'].shape
print matrix_answer['tf'].shape
print matrix_corpus['tf'].shape

if(source == 1):
	matrix = matrix_question
if(source == 2):
	matrix = matrix_answer_key
if(source == 3):
	matrix = matrix_answer
if(source == 5):
	matrix = matrix_corpus
	
#create SVD
svd_tf_idf = SingularValueDecomposition()
svd_widf = SingularValueDecomposition()
svd_midf = SingularValueDecomposition()

svd_tf_idf.generateSVD(matrix['tf_idf'])
svd_widf.generateSVD(matrix['widf'])
svd_midf.generateSVD(matrix['midf'])

save('result/'+str(source)+'.svd.tf_idf.u.npy',svd_tf_idf.U)
save('result/'+str(source)+'.svd.tf_idf.s.npy',svd_tf_idf.S)
save('result/'+str(source)+'.svd.tf_idf.vt.npy',svd_tf_idf.Vt)

save('result/'+str(source)+'.svd.widf.u.npy',svd_widf.U)
save('result/'+str(source)+'.svd.widf.s.npy',svd_widf.S)
save('result/'+str(source)+'.svd.widf.vt.npy',svd_widf.Vt)

save('result/'+str(source)+'.svd.midf.u.npy',svd_midf.U)
save('result/'+str(source)+'.svd.midf.s.npy',svd_midf.S)
save('result/'+str(source)+'.svd.midf.vt.npy',svd_midf.Vt)

save('result/'+'matrix.question.npy',matrix_question['tf'])
save('result/'+'matrix.answer_key.npy',matrix_answer_key['tf'])
save('result/'+'matrix.answer.npy',matrix_answer['tf'])

save('result/'+'term_list.npy',tdm.term_list)

#disconnect from server
db.close()