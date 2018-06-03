#!/usr/bin/python

from numpy import zeros
from TermDocument import TermDocument

class TermDocumentMatrix:

	def __init__(self, term_document_matrix, documemt_list):
		self.term_document_matrix = term_document_matrix
		self.documemt_list = documemt_list

	def createTermDictionary(self):
		self.term_dictionary = {}
		for row in self.term_document_matrix:
			
			td = TermDocument(row)
			
			if td.term in self.term_dictionary:
				self.term_dictionary[td.term].append(td)	
			else:
				self.term_dictionary[td.term] = []
				self.term_dictionary[td.term].append(td)
		
	def createTermList(self):
		self.term_list = [term for term in self.term_dictionary.keys()] 
		self.term_list.sort()
		
	def createDocumentList(self):		
		self.documemt_list = [document[0] for document in self.documemt_list]
		self.documemt_list.sort()
		
	def createMatrix(self):	
		self.matrix = {}
		self.matrix['tf'] = zeros([len(self.term_list), len(self.documemt_list)])
		self.matrix['idf'] = zeros([len(self.term_list), len(self.documemt_list)])
		self.matrix['tf_idf'] = zeros([len(self.term_list), len(self.documemt_list)])
		self.matrix['widf'] = zeros([len(self.term_list), len(self.documemt_list)])
		self.matrix['midf'] = zeros([len(self.term_list), len(self.documemt_list)])

		for idx1, term in enumerate(self.term_list):
			for idx2, document in enumerate(self.documemt_list):
				for td in self.term_dictionary[term]:
					if td.id_document == document:
						self.matrix['tf'][idx1, idx2] = td.tf
						self.matrix['idf'][idx1, idx2] = td.idf
						self.matrix['tf_idf'][idx1, idx2] = td.tf_idf
						self.matrix['widf'][idx1, idx2] = td.widf
						self.matrix['midf'][idx1, idx2] = td.midf
		
	def getMatrixQuestion(self):
		matrix = {}
		matrix['tf'] =  self.matrix['tf'][:,0:1]
		matrix['idf'] =  self.matrix['idf'][:,0:1]
		matrix['tf_idf'] =  self.matrix['tf_idf'][:,0:1]
		matrix['widf'] =  self.matrix['widf'][:,0:1]
		matrix['midf'] =  self.matrix['midf'][:,0:1]
		
		return matrix
	
	def getMatrixAnswerKey(self):
		matrix = {}
		matrix['tf'] =  self.matrix['tf'][:,1:2]
		matrix['idf'] =  self.matrix['idf'][:,1:2]
		matrix['tf_idf'] =  self.matrix['tf_idf'][:,1:2]
		matrix['widf'] =  self.matrix['widf'][:,1:2]
		matrix['midf'] =  self.matrix['midf'][:,1:2]
		
		return matrix
		
	def getMatrixAnswer(self):
		matrix = {}
		matrix['tf'] =  self.matrix['tf'][:,2:31]
		matrix['idf'] =  self.matrix['idf'][:,2:31]
		matrix['tf_idf'] =  self.matrix['tf_idf'][:,2:31]
		matrix['widf'] =  self.matrix['widf'][:,2:31]
		matrix['midf'] =  self.matrix['midf'][:,2:31]
		
		return matrix