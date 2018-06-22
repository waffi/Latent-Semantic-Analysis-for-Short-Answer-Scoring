#!/usr/bin/python


from nltk.corpus import stopwords

stopword_list = set(stopwords.words('english'))
for stopword in stopword_list:
	print stopword