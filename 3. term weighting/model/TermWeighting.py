#!/usr/bin/python

from math import log10

class TermWeighting:

	def setTotalDocument(self, total_document):
		self.total_document = total_document
		
	def setCountDocumentDictionary(self, term_list):
		self.count_document_dictionary = {}
		for row in term_list:
			term = row[0]
			contained_document = row[1]
			self.count_document_dictionary[term] = contained_document

	def setSumTfDictionary(self, sum_tf_list):
		self.sum_tf_dictionary = {}
		for row in sum_tf_list:
			term = row[0]
			sum_tf = row[1]
			self.sum_tf_dictionary[term] = sum_tf
		
	def get_idf(self, term):
		return log10(float(self.total_document) / float(self.count_document_dictionary[term]))
		
	def get_tf_idf(self, term, tf):
		return float(tf) * self.get_idf(term)
		
	def get_widf(self, term, tf):
		return float(tf) / float(self.sum_tf_dictionary[term])
		
	def get_midf(self, term, tf):
		return float(tf) * float(self.count_document_dictionary[term]) / float(self.sum_tf_dictionary[term])