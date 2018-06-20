#!/usr/bin/python

from numpy import load
from MySQLdb import connect
from sklearn.metrics.pairwise import cosine_similarity
from model.SingularValueDecomposition import SingularValueDecomposition

#prepare database connection
db = connect("localhost","root","","db_asas" )
cursor = db.cursor()

#get answer boudary
sql = "SELECT MAX(ID_ANSWER), ID_QUESTION FROM `answer` GROUP BY ID_QUESTION"
cursor.execute(sql)
answer_boudary = cursor.fetchall()

print answer_boudary

#1 = question, 2 = answer key, 3 = answer, 4 = testing, 5 = corpus
source = ?
source_path = 'source/' + str(source) + '/'

#get svd
term_list = load(source_path + 'term_list.npy')
matrix_answer = load(source_path + 'matrix.answer.npy')
matrix_answer_key = load(source_path + 'matrix.answer_key.npy')
print term_list.shape
print matrix_answer.shape
print matrix_answer_key.shape

#get svd

svd_tf_idf = SingularValueDecomposition()
svd_widf = SingularValueDecomposition()
svd_midf = SingularValueDecomposition()

svd_tf_idf.setMatrixDecomposition(load(source_path + str(source)+'.svd.tf_idf.u.npy'),load(source_path + str(source)+'.svd.tf_idf.s.npy'),load(source_path + str(source)+'.svd.tf_idf.vt.npy'))
svd_widf.setMatrixDecomposition(load(source_path + str(source)+'.svd.widf.u.npy'),load(source_path + str(source)+'.svd.widf.s.npy'),load(source_path + str(source)+'.svd.widf.vt.npy'))
svd_midf.setMatrixDecomposition(load(source_path + str(source)+'.svd.midf.u.npy'),load(source_path + str(source)+'.svd.midf.s.npy'),load(source_path + str(source)+'.svd.midf.vt.npy'))

#eksperiment
for i in range(?, ?):
	id_skenario = i
	k_dimension = ?

	svd_tf_idf.getReductionSVD(k_dimension)
	svd_widf.getReductionSVD(k_dimension)
	svd_midf.getReductionSVD(k_dimension)

	sql = "INSERT INTO `scenario`(`ID_SCENARIO`,`ID_SOURCE`, `K_DIMENSION`) VALUES (%d,%d,%d)" %(id_skenario, source, k_dimension)
	cursor.execute(sql)
	db.commit()
		
	id_answer = 1
	id_question = 1
	for answer in matrix_answer.transpose():

		v1 = matrix_answer[:,id_answer-1:id_answer]	
		v2 = matrix_answer_key[:,id_question-1:id_question]	
		
		#score = cosine_similarity(v1.transpose(), v2.transpose()) * 5
		
		score_tf_idf = cosine_similarity(svd_tf_idf.createQuery(v1), svd_tf_idf.createQuery(v2)) * 5
		score_widf = cosine_similarity(svd_widf.createQuery(v1), svd_widf.createQuery(v2)) * 5
		score_midf = cosine_similarity(svd_midf.createQuery(v1), svd_midf.createQuery(v2)) * 5
		
		print str(id_answer) + "-" + str(id_question)
		print str(score_tf_idf) + " | " + str(score_widf) + " | " + str(score_midf)
		
		sql = "INSERT INTO `score_system`(`ID_SCENARIO`, `ID_ANSWER`, `SCORE_TF_IDF`, `SCORE_WIDF`, `SCORE_MIDF`) VALUES (%d,%d,%f,%f,%f)" %(id_skenario, id_answer, score_tf_idf, score_widf, score_midf)
		cursor.execute(sql)
		db.commit()
		
		if id_answer == answer_boudary[id_question-1][0]:
			id_question += 1
			
		id_answer += 1
 
#disconnect from server
db.close()