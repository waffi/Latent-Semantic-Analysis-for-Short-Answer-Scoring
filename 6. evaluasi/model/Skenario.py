#!/usr/bin/python

class Skenario:

	def __init__(self, id_skenario):
		
		self.id_skenario = id_skenario
		
	def getQuery(self):
		sql = ""
		
		sql += "SELECT SCORE_HUMAN, SCORE_TF_IDF, SCORE_WIDF, SCORE_MIDF"		
		sql += self.getQueryCase(2)
		sql += self.getQueryCase(3)
		sql += self.getQueryCase(6)
		sql += self.getQueryCase(11)
		sql += " FROM `score_system` s, `answer` a WHERE s.ID_ANSWER = a.ID_ANSWER AND s.ID_SCENARIO = %d" %(self.id_skenario)
		
		return sql
	
	def getQueryCase(self, case):
		sql = ""
	
		sql += self.getQueryRound(case, 'SCORE_HUMAN')
		sql += self.getQueryRound(case, 'SCORE_TF_IDF')
		sql += self.getQueryRound(case, 'SCORE_WIDF')
		sql += self.getQueryRound(case, 'SCORE_MIDF')
		
		return sql
		
	def getQueryRound(self, case, column):
		sql = ""
		
		if case == 2:
			sql = ", (CASE WHEN " + column + " < 2.5 THEN 0 WHEN " + column + " >= 2.5 THEN 5 END) AS " + column + "_2"
			
		if case == 3:
			sql = ", (CASE WHEN " + column + " < 1.6 THEN 0 WHEN " + column + " >= 1.6 AND " + column + " < 3.3 THEN 2.5 WHEN " + column + " >= 3.3 THEN 5 END) AS " + column + "_3"
			
		if case == 6:
			sql = ", (CASE WHEN " + column + " < 0.5 THEN 0 WHEN " + column + " >= 0.5 AND " + column + " < 1.5 THEN 1 WHEN " + column + " >= 1.5 AND " + column + " < 2.5 THEN 2 WHEN " + column + " >= 2.5 AND " + column + " < 3.5 THEN 3 WHEN " + column + " >= 3.5 AND " + column + " < 4.5 THEN 4 WHEN " + column + " >= 4.5 THEN 5 END) AS " + column + "_5"
			
		if case == 11:
			sql = ", (CASE WHEN " + column + " < 0.25 THEN 0 WHEN " + column + " >= 0.25 AND " + column + " < 0.75 THEN 0.5 WHEN " + column + " >= 0.75 AND " + column + " < 1.25 THEN 1 WHEN " + column + " >= 1.25 AND " + column + " < 1.75 THEN 1.5 WHEN " + column + " >= 1.75 AND " + column + " < 2.25 THEN 2 WHEN " + column + " >= 2.25 AND " + column + " < 2.75 THEN 2.5 WHEN " + column + " >= 2.75 AND " + column + " < 3.25 THEN 3 WHEN " + column + " >= 3.25 AND " + column + " < 3.75 THEN 3.5 WHEN " + column + " >= 3.75 AND " + column + " < 4.25 THEN 4 WHEN " + column + " >= 4.25 AND " + column + " < 4.75 THEN 4.5 WHEN " + column + " >= 4.75 THEN 5 END) AS " + column + "_10"
			
		return sql