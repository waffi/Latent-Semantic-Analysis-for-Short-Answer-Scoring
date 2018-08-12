#!/usr/bin/python

from collections import Counter
from openpyxl import load_workbook
from numpy import load, save, zeros
from preprocessing import preprocessing
from sklearn.metrics.pairwise import cosine_similarity
from model.TermDocumentMatrix import TermDocumentMatrix
from model.SingularValueDecomposition import SingularValueDecomposition

#1 = question, 2 = answer key, 3 = answer, 4 = testing, 5 = corpus
source = 5
source_path = 'source/' + str(source) + '/'

term_list = load(source_path + 'term_list.npy')
term_list = term_list.tolist()

workbook = load_workbook("sequence.xlsx")
worksheet = workbook.active

for i in range(?, ?):

	text1 = worksheet['A'+str(i)].value
	text2 = worksheet['B'+str(i)].value

	term_list1 = preprocessing(text1)
	term_list2 = preprocessing(text2)
	term_list1 = Counter(term_list1)
	term_list2 = Counter(term_list2)

	#create SVD
	svd_tf_idf = SingularValueDecomposition()
	svd_widf = SingularValueDecomposition()
	svd_midf = SingularValueDecomposition()

	svd_tf_idf.setMatrixDecomposition(load(source_path + str(source)+'.svd.tf_idf.u.npy'),load(source_path + str(source)+'.svd.tf_idf.s.npy'),load(source_path + str(source)+'.svd.tf_idf.vt.npy'))
	svd_widf.setMatrixDecomposition(load(source_path + str(source)+'.svd.widf.u.npy'),load(source_path + str(source)+'.svd.widf.s.npy'),load(source_path + str(source)+'.svd.widf.vt.npy'))
	svd_midf.setMatrixDecomposition(load(source_path + str(source)+'.svd.midf.u.npy'),load(source_path + str(source)+'.svd.midf.s.npy'),load(source_path + str(source)+'.svd.midf.vt.npy'))

	k_dimension = 285
	svd_tf_idf.setReductionSVD(k_dimension)
	svd_widf.setReductionSVD(k_dimension)
	svd_midf.setReductionSVD(k_dimension)

	#create vecor
	vector = zeros([len(term_list), 2])
	for idx, term in enumerate(term_list):
		vector[idx][0] = term_list1[term]
		vector[idx][1] = term_list2[term]

	v1 = vector[:,0:1]	
	v2 = vector[:,1:2]
			
	score = cosine_similarity(v1.transpose(), v2.transpose())[0][0]		
	score_tf_idf = cosine_similarity(svd_tf_idf.createQuery(v1), svd_tf_idf.createQuery(v2))[0][0]
	score_widf = cosine_similarity(svd_widf.createQuery(v1), svd_widf.createQuery(v2))[0][0]
	score_midf = cosine_similarity(svd_midf.createQuery(v1), svd_midf.createQuery(v2))[0][0]

	print "text1 : " + text1
	print "text2 : " + text2
	print "   tf_idf : " + str(score_tf_idf) 
	print "   widf   : " + str(score_widf)
	print "   midf   : " + str(score_midf)
	
	worksheet['C'+str(i)] = score_tf_idf
	worksheet['D'+str(i)] = score_widf
	worksheet['E'+str(i)] = score_midf

workbook.save('result.xlsx')
