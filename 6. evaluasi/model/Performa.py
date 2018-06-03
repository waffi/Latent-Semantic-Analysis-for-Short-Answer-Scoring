#!/usr/bin/python

class Performa:
		
	def __init__(self, id_skenario, case):
		self.id_skenario = id_skenario
		self.case = case
				
		self.tp = {}
		self.tp['tf_idf'] = [0] * 11
		self.tp['widf'] = [0] * 11
		self.tp['midf'] = [0] * 11
		
		self.fp = {}
		self.fp['tf_idf'] = [0] * 11
		self.fp['widf'] = [0] * 11
		self.fp['midf'] = [0] * 11
		
		self.tn = {}
		self.tn['tf_idf'] = [0] * 11
		self.tn['widf'] = [0] * 11
		self.tn['midf'] = [0] * 11
		
		self.fn = {}
		self.fn['tf_idf'] = [0] * 11
		self.fn['widf'] = [0] * 11
		self.fn['midf'] = [0] * 11
		
		self.total_true = {}
		self.total_true['tf_idf'] = 0
		self.total_true['widf'] = 0
		self.total_true['midf'] = 0
		
		self.total_false = {}
		self.total_false['tf_idf'] = 0
		self.total_false['widf'] = 0
		self.total_false['midf'] = 0
		
		self.precision = {}
		self.precision['tf_idf'] = float(0)
		self.precision['widf'] = float(0)
		self.precision['midf'] = float(0)
		
		self.recall = {}
		self.recall['tf_idf'] = float(0)
		self.recall['widf'] = float(0)
		self.recall['midf'] = float(0)
		
		self.accuracy = {}
		self.accuracy['tf_idf'] = float(0)
		self.accuracy['widf'] = float(0)
		self.accuracy['midf'] = float(0)
				
		self.f_measure = {}
		self.f_measure['tf_idf'] = float(0)
		self.f_measure['widf'] = float(0)
		self.f_measure['midf'] = float(0)
		
	def checkRelevantScore(self, row):
	
		if self.case == 2:
			self.updateTotalTrueFalse(row, 4)
				
		if self.case == 3:
			self.updateTotalTrueFalse(row, 8)
				
		if self.case == 6:
			self.updateTotalTrueFalse(row, 12)
				
		if self.case == 11:
			self.updateTotalTrueFalse(row, 16)
	
	def updateTotalTrueFalse(self, row, index):
	
		#true
		if row[index] == row[index+1]:
			self.total_true['tf_idf'] += 1
			self.updateContingency(self.tp['tf_idf'], self.tn['tf_idf'], row[index+1])
		if row[index] == row[index+2]:
			self.total_true['widf'] += 1
			self.updateContingency(self.tp['widf'], self.tn['widf'], row[index+2])
		if row[index] == row[index+3]:
			self.total_true['midf'] += 1
			self.updateContingency(self.tp['midf'], self.tn['midf'], row[index+3])
		
		#false	
		if row[index] != row[index+1]:
			self.total_false['tf_idf'] += 1
			self.updateContingency(self.fp['tf_idf'], self.fn['tf_idf'], row[index+1])			
		if row[index] != row[index+2]:
			self.total_false['widf'] += 1
			self.updateContingency(self.fp['widf'], self.fn['widf'], row[index+2])			
		if row[index] != row[index+3]:
			self.total_false['midf'] += 1
			self.updateContingency(self.fp['midf'], self.fn['midf'], row[index+3])
		
	def updateContingency(self, positive,  negative, score):
				
		#positive
		if score == 0:#case 6, 3, 2
			positive[0] += 1
		if score == 0.5:
			positive[1] += 1
		if score == 1:#case 6
			positive[2] += 1
		if score == 1.5:
			positive[3] += 1
		if score == 2:#case 6
			positive[4] += 1
		if score == 2.5:#case 3
			positive[5] += 1
		if score == 3:#case 6
			positive[6] += 1
		if score == 3.5:
			positive[7] += 1
		if score == 4:#case 6
			positive[8] += 1
		if score == 4.5:
			positive[9] += 1
		if score == 5:#case 6, 3, 2
			positive[10] += 1
			
		#negative
		if score != 0:#case 6, 3, 2
			negative[0] += 1
		if score != 0.5:
			negative[1] += 1
		if score != 1:#case 6
			negative[2] += 1
		if score != 1.5:
			negative[3] += 1
		if score != 2:#case 6
			negative[4] += 1
		if score != 2.5:#case 3
			negative[5] += 1
		if score != 3:#case 6
			negative[6] += 1
		if score != 3.5:
			negative[7] += 1
		if score != 4:#case 6
			negative[8] += 1
		if score != 4.5:
			negative[9] += 1
		if score != 5:#case 6, 3, 2
			negative[10] += 1
			
	def cleanContigency(self):
	
		print self.total_true['tf_idf']
		self.cleanContigencyValue(self.tp['tf_idf'])
		self.cleanContigencyValue(self.tn['tf_idf'])		
		print self.total_false['tf_idf']
		self.cleanContigencyValue(self.fp['tf_idf'])
		self.cleanContigencyValue(self.fn['tf_idf'])

		print self.total_true['widf']
		self.cleanContigencyValue(self.tp['widf'])
		self.cleanContigencyValue(self.tn['widf'])		
		print self.total_false['widf']
		self.cleanContigencyValue(self.fp['widf'])
		self.cleanContigencyValue(self.fn['widf'])

		print self.total_true['midf']
		self.cleanContigencyValue(self.tp['midf'])
		self.cleanContigencyValue(self.tn['midf'])		
		print self.total_false['midf']
		self.cleanContigencyValue(self.fp['midf'])
		self.cleanContigencyValue(self.fn['midf'])			
	
	def cleanContigencyValue(self, array):	
		if self.case == 2:
			del array[9]
			del array[8]
			del array[7]
			del array[6]
			del array[5]
			del array[4]
			del array[3]
			del array[2]
			del array[1]	
		if self.case == 3:
			del array[9]
			del array[8]
			del array[7]
			del array[6]
			del array[4]
			del array[3]
			del array[2]
			del array[1]	
		if self.case == 6:	
			del array[9]
			del array[7]
			del array[5]
			del array[3]
			del array[1]
			
		print array
	
	def countPerforma(self):	
		self.countPrecision()	
		self.countRecall()	
		self.countFmeasure()	
		self.countAccuracy()
	
	def countPrecision(self):	

		print 'precision'
					
		self.precision['tf_idf'] = float(sum(self.tp['tf_idf']))/float(sum(self.tp['tf_idf']) + sum(self.fp['tf_idf']))
		self.precision['widf'] = float(sum(self.tp['widf']))/float(sum(self.tp['widf']) + sum(self.fp['widf']))
		self.precision['midf'] = float(sum(self.tp['midf']))/float(sum(self.tp['midf']) + sum(self.fp['midf']))
		
		# print self.precision['tf_idf']
		# print self.precision['widf']
		# print self.precision['midf']
		
	def countRecall(self):	

		print 'recall'
					
		self.recall['tf_idf'] = float(sum(self.tp['tf_idf']))/float(sum(self.tp['tf_idf']) + sum(self.fn['tf_idf']))
		self.recall['widf'] = float(sum(self.tp['widf']))/float(sum(self.tp['widf']) + sum(self.fn['widf']))
		self.recall['midf'] = float(sum(self.tp['midf']))/float(sum(self.tp['midf']) + sum(self.fn['midf']))
		
		# print self.recall['tf_idf']
		# print self.recall['widf']
		# print self.recall['midf']
		
	def countFmeasure(self):	

		print 'f_measure'
					
		self.f_measure['tf_idf'] = float(2*self.precision['tf_idf']*self.recall['tf_idf'])/float(self.precision['tf_idf'] + self.recall['tf_idf'])
		self.f_measure['widf'] = float(2*self.precision['widf']*self.recall['widf'])/float(self.precision['widf'] + self.recall['widf'])
		self.f_measure['midf'] = float(2*self.precision['midf']*self.recall['midf'])/float(self.precision['midf'] + self.recall['midf'])
		
		print self.f_measure['tf_idf']
		print self.f_measure['widf']
		print self.f_measure['midf']
		
	def countAccuracy(self):	

		print 'accuracy'
			
		# self.accuracy['tf_idf'] = float(self.total_true['tf_idf'])/float(self.total_true['tf_idf']+self.total_false['tf_idf'])*100
		# self.accuracy['widf'] = float(self.total_true['widf'])/(self.total_true['widf']+self.total_false['widf'])*100
		# self.accuracy['midf'] = float(self.total_true['midf'])/(self.total_true['midf']+self.total_false['midf'])*100
		
		# print self.accuracy['tf_idf']
		# print self.accuracy['widf']
		# print self.accuracy['midf']
		
		self.accuracy['tf_idf'] = float(sum(self.tp['tf_idf']) + sum(self.tn['tf_idf']))/float(sum(self.tp['tf_idf']) + sum(self.fp['tf_idf']) + sum(self.fn['tf_idf']) + sum(self.tn['tf_idf']))*100
		self.accuracy['widf'] = float(sum(self.tp['widf']) + sum(self.tn['widf']))/float(sum(self.tp['widf']) + sum(self.fp['widf']) + sum(self.fn['widf']) + sum(self.tn['widf']))*100
		self.accuracy['midf'] = float(sum(self.tp['midf']) + sum(self.tn['midf']))/float(sum(self.tp['midf']) + sum(self.fp['midf']) + sum(self.fn['midf']) + sum(self.tn['midf']))*100
		
		print self.accuracy['tf_idf']
		print self.accuracy['widf']
		print self.accuracy['midf']
		
	def insert(self, cursor, db):
		sql = self.insertQuery('tf_idf')
		cursor.execute(sql)
		db.commit()
		
		sql = self.insertQuery('widf')
		cursor.execute(sql)
		db.commit()
		
		sql = self.insertQuery('midf')
		cursor.execute(sql)
		db.commit()
		
	def insertQuery(self, term_weighting):
		sql = "INSERT INTO `performa`(`ID_SCENARIO`, `ROUNDING_TYPE`, `TERM_WEIGHTING`, `PRECISION`, `RECALL`, `ACCURACY`, `F_MEASURE`) VALUES (%d,%d,'%s',%f,%f,%f,%f)" %(self.id_skenario, self.case, term_weighting, self.precision[term_weighting], self.recall[term_weighting], self.accuracy[term_weighting], self.f_measure[term_weighting])
		
		return sql
	