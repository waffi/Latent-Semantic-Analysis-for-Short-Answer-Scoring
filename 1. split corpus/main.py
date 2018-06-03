#!/usr/bin/python

from MySQLdb import connect
from xml.dom import minidom
from string import ascii_uppercase
						
def searchFile(identifier):

	for child_identifier in range(0, 10):
		new_identifier = identifier + str(child_identifier)		
		
		if len(new_identifier) == 3:
			getDomain(new_identifier)
		else:
			searchFile(new_identifier)
			
	for child_identifier in ascii_uppercase:
		new_identifier = identifier + child_identifier
		
		if len(new_identifier) == 3:
			getDomain(new_identifier)
		else:
			searchFile(new_identifier)
			
def getDomain(file):
	global insert_status
	
	file = file[:1] + '/' + file[:2] + '/' + file[:3] + '.xml'
	print file
	
	if file == progress:
		insert_status = bool(1)
		
	if insert_status:
		try:				
			mydoc = minidom.parse(file)
			title = mydoc.getElementsByTagName('titleStmt')[0].getElementsByTagName('title')[0].firstChild.data
			title = title.strip().encode('utf-8').decode('latin1')
			
			try:			
				find_text = 'domain: '
				domain = title[title.index(find_text)+len(find_text):-1]
				
			except ValueError:
				domain = 'undefined'
			
			#insert domain info
			sql = "INSERT INTO `corpus`(`FILE`, `TITLE`, `DOMAIN`) VALUES (\"%s\", \"%s\", \"%s\")" %(file, title, domain)
			cursor.execute(sql)
			db.commit()
			
		except IOError:
			print "no such file or directory: " + file

#main program
			
#progress insert corpus	
progress = "A/A0/A00.xml"
insert_status = bool(0) 	
	
#prepare database connection
db = connect("localhost","root","","db_asas" )
cursor = db.cursor()

for folder in ascii_uppercase:
	searchFile(folder)

#disconnect from server
db.close()