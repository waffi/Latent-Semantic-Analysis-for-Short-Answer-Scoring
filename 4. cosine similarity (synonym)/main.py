#!/usr/bin/python

from numpy import load
from numpy import zeros
from sklearn.metrics.pairwise import cosine_similarity
from model.SingularValueDecomposition import SingularValueDecomposition

#1 = question, 2 = answer key, 3 = answer, 4 = testing, 5 = corpus
source = 5
source_path = 'source/' + str(source) + '/'

#get svd
term_list = load(source_path + 'term_list.npy')
term_list = term_list.tolist()

#get svd

svd_tf_idf = SingularValueDecomposition()
svd_widf = SingularValueDecomposition()
svd_midf = SingularValueDecomposition()

svd_tf_idf.setMatrixDecomposition(load(source_path + str(source)+'.svd.tf_idf.u.npy'),load(source_path + str(source)+'.svd.tf_idf.s.npy'),load(source_path + str(source)+'.svd.tf_idf.vt.npy'))
svd_widf.setMatrixDecomposition(load(source_path + str(source)+'.svd.widf.u.npy'),load(source_path + str(source)+'.svd.widf.s.npy'),load(source_path + str(source)+'.svd.widf.vt.npy'))
svd_midf.setMatrixDecomposition(load(source_path + str(source)+'.svd.midf.u.npy'),load(source_path + str(source)+'.svd.midf.s.npy'),load(source_path + str(source)+'.svd.midf.vt.npy'))
	
#eksperiment

k_dimension = 285

svd_tf_idf.setReductionSVD(k_dimension)
svd_widf.setReductionSVD(k_dimension)
svd_midf.setReductionSVD(k_dimension)
	
m1 = zeros([len(term_list), 7])	
m2 = zeros([len(term_list), 7])	

m1[term_list.index("softwar"),0]=1
m2[term_list.index("program"),0]=1

m1[term_list.index("program"),1]=1
m2[term_list.index("applic"),1]=1

m1[term_list.index("applic"),2]=1
m2[term_list.index("softwar"),2]=1

m1[term_list.index("enhanc"),3]=1
m2[term_list.index("improv"),3]=1

m1[term_list.index("product"),4]=1
m2[term_list.index("construct"),4]=1

m1[term_list.index("function"),5]=1
m2[term_list.index("method"),5]=1

m1[term_list.index("chang"),6]=1
m2[term_list.index("manipul"),6]=1

for i in range(1, 8):
	
	v1 = m1[:,i-1:i]	
	v2 = m2[:,i-1:i]
	
	index1 = v1.transpose()[0,:].tolist().index(1)
	index2 = v2.transpose()[0,:].tolist().index(1)
	
	print term_list[index1] + " - " + term_list[index2]
	
	#score = cosine_similarity(v1.transpose(), v2.transpose()) * 5

	score_tf_idf = cosine_similarity(svd_tf_idf.createQuery(v1), svd_tf_idf.createQuery(v2))[0][0]
	score_widf = cosine_similarity(svd_widf.createQuery(v1), svd_widf.createQuery(v2))[0][0]
	score_midf = cosine_similarity(svd_midf.createQuery(v1), svd_midf.createQuery(v2))[0][0]
		
	print "   tf_idf : " + str(score_tf_idf) 
	print "   widf   : " + str(score_widf)
	print "   midf   : " + str(score_midf)		
 