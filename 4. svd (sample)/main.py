#!/usr/bin/python

from numpy import save
from MySQLdb import connect
from xlsxwriter import Workbook
from model.TermDocumentMatrix import TermDocumentMatrix
from model.SingularValueDecomposition import SingularValueDecomposition

def matrixToExcel(worksheet, matrix):
	count = 0
	for row in matrix:			
		count_doc = 0
		for document in matrix[count]:
			worksheet.write(count,count_doc, document)
			
			count_doc += 1	
		count += 1

#1 = question, 2 = answer key, 3 = answer, 4 = sample
source = 4

#prepare database connection
db = connect("localhost","root","","db_asas")
cursor = db.cursor()

sql = "SELECT * FROM `term_document_matrix` tdm, `document` d WHERE tdm.ID_DOCUMENT = d.ID_DOCUMENT AND ((d.ID_SOURCE = 1 AND d.ID_REF = 1) or (d.ID_SOURCE = 2 AND d.ID_REF = 1) or (d.ID_SOURCE = 4))"
cursor.execute(sql)
term_document_matrix = cursor.fetchall()

sql = "SELECT ID_DOCUMENT d FROM document d WHERE (d.ID_SOURCE = 1 AND d.ID_REF = 1) or (d.ID_SOURCE = 2 AND d.ID_REF = 1) or (d.ID_SOURCE = 4)"
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

matrix = matrix_answer

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

#write matrix
workbook = Workbook('term weighting.xlsx')

worksheet = workbook.add_worksheet('question')
matrixToExcel(worksheet, matrix_question['tf'])
worksheet = workbook.add_worksheet('answer_key')
matrixToExcel(worksheet, matrix_answer_key['tf'])
worksheet = workbook.add_worksheet('answer')
matrixToExcel(worksheet, matrix_answer['tf'])
worksheet = workbook.add_worksheet('tf_idf')
matrixToExcel(worksheet, matrix_answer['tf_idf'])
worksheet = workbook.add_worksheet('widf')
matrixToExcel(worksheet, matrix_answer['widf'])
worksheet = workbook.add_worksheet('midf')
matrixToExcel(worksheet, matrix_answer['midf'])

workbook = Workbook('svd.xlsx')

worksheet = workbook.add_worksheet('svd_tf_idf_u')
matrixToExcel(worksheet, svd_tf_idf.U)
worksheet = workbook.add_worksheet('svd_tf_idf_s')
matrixToExcel(worksheet, svd_tf_idf.S)
worksheet = workbook.add_worksheet('svd_tf_idf_vt')
matrixToExcel(worksheet, svd_tf_idf.Vt)

worksheet = workbook.add_worksheet('svd_widf_u')
matrixToExcel(worksheet, svd_widf.U)
worksheet = workbook.add_worksheet('svd_widf_s')
matrixToExcel(worksheet, svd_widf.S)
worksheet = workbook.add_worksheet('svd_widf_vt')
matrixToExcel(worksheet, svd_widf.Vt)

worksheet = workbook.add_worksheet('svd_midf_u')
matrixToExcel(worksheet, svd_midf.U)
worksheet = workbook.add_worksheet('svd_midf_s')
matrixToExcel(worksheet, svd_midf.S)
worksheet = workbook.add_worksheet('svd_midf_vt')
matrixToExcel(worksheet, svd_midf.Vt)

workbook.close()

#disconnect from server
db.close()