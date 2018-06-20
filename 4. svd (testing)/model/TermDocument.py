#!/usr/bin/python

class TermDocument:

    def __init__(self, array):
		
		self.id_term = array[0]
		self.id_document = array[1]
		self.term = array[2]
		self.tf = array[3]
		self.idf = array[4]
		self.tf_idf = array[5]
		self.widf = array[6]
		self.midf = array[7]