#!/usr/bin/python

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import PorterStemmer

def preprocessing(document):
	result = []
	
	stopword_list = set(stopwords.words('english'))
	stemmer = PorterStemmer()
	
	#case folding
	document = document.lower()
	
	#tokenization
	token_list = word_tokenize(document)
	
	for index, token in enumerate(token_list):
	
		#stop words removal
		if token not in stopword_list and token.isalpha():
			#stemming
			result.append(stemmer.stem(token))
		
	return result