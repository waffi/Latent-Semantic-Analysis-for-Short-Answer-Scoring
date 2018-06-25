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
		self.precision['tf_idf'] = [float(0), float(0)]
		self.precision['widf'] = [float(0), float(0)]
		self.precision['midf'] = [float(0), float(0)]
		
		self.recall = {}
		self.recall['tf_idf'] = [float(0), float(0)]
		self.recall['widf'] = [float(0), float(0)]
		self.recall['midf'] = [float(0), float(0)]
		
		self.accuracy = {}
		self.accuracy['tf_idf'] = [float(0), float(0)]
		self.accuracy['widf'] = [float(0), float(0)]
		self.accuracy['midf'] = [float(0), float(0)]
				
		self.f_measure = {}
		self.f_measure['tf_idf'] = [float(0), float(0)]
		self.f_measure['widf'] = [float(0), float(0)]
		self.f_measure['midf'] = [float(0), float(0)]
		
	def updateContigency(self, row):
	
		if self.case == 2:
			self.updateContingencyTrueFalse(row, 4)
				
		if self.case == 3:
			self.updateContingencyTrueFalse(row, 8)
				
		if self.case == 6:
			self.updateContingencyTrueFalse(row, 12)
				
		if self.case == 11:
			self.updateContingencyTrueFalse(row, 16)
	
	def updateContingencyTrueFalse(self, row, index):
	
		#true
		if row[index] == row[index+1]:
			self.total_true['tf_idf'] += 1
			self.tp['tf_idf'], self.tn['tf_idf'] = self.updateContingencyPositiveNegative(self.tp['tf_idf'], self.tn['tf_idf'], row[index+1])
		if row[index] == row[index+2]:
			self.total_true['widf'] += 1
			self.updateContingencyPositiveNegative(self.tp['widf'], self.tn['widf'], row[index+2])
		if row[index] == row[index+3]:
			self.total_true['midf'] += 1
			self.updateContingencyPositiveNegative(self.tp['midf'], self.tn['midf'], row[index+3])
		
		#false	
		if row[index] != row[index+1]:
			self.total_false['tf_idf'] += 1
			self.updateContingencyPositiveNegative(self.fp['tf_idf'], self.fn['tf_idf'], row[index+1])
		if row[index] != row[index+2]:
			self.total_false['widf'] += 1
			self.updateContingencyPositiveNegative(self.fp['widf'], self.fn['widf'], row[index+2])	
		if row[index] != row[index+3]:
			self.total_false['midf'] += 1
			self.updateContingencyPositiveNegative(self.fp['midf'], self.fn['midf'], row[index+3])
		
	def updateContingencyPositiveNegative(self, positive,  negative, score):
				
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
			
		return positive, negative
			
	def cleanContigency(self):
		# print self.total_true['tf_idf']
		self.cleanContigencyValue(self.tp['tf_idf'])
		self.cleanContigencyValue(self.tn['tf_idf'])		
		# print self.total_false['tf_idf']
		self.cleanContigencyValue(self.fp['tf_idf'])
		self.cleanContigencyValue(self.fn['tf_idf'])

		# print self.total_true['widf']
		self.cleanContigencyValue(self.tp['widf'])
		self.cleanContigencyValue(self.tn['widf'])		
		# print self.total_false['widf']
		self.cleanContigencyValue(self.fp['widf'])
		self.cleanContigencyValue(self.fn['widf'])

		# print self.total_true['midf']
		self.cleanContigencyValue(self.tp['midf'])
		self.cleanContigencyValue(self.tn['midf'])		
		# print self.total_false['midf']
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
			
		# print array
	
	def countPerforma(self):	
		self.countPrecision()	
		self.countRecall()	
		self.countFmeasure()	
		self.countAccuracy()
	
	def countPrecision(self):	

		#micro
					
		self.precision['tf_idf'][0] = float(sum(self.tp['tf_idf']))/float(sum(self.tp['tf_idf']) + sum(self.fp['tf_idf']))
		self.precision['widf'][0] = float(sum(self.tp['widf']))/float(sum(self.tp['widf']) + sum(self.fp['widf']))
		self.precision['midf'][0] = float(sum(self.tp['midf']))/float(sum(self.tp['midf']) + sum(self.fp['midf']))
		
		#macro
		
		for i in range(0, self.case):
			try:	
				self.precision['tf_idf'][1] += float(self.tp['tf_idf'][i])/float(self.tp['tf_idf'][i] + self.fp['tf_idf'][i])		
			except ZeroDivisionError:
				pass
				
			try:
				self.precision['widf'][1] += float(self.tp['widf'][i])/float(self.tp['widf'][i] + self.fp['widf'][i])		
			except ZeroDivisionError:
				pass
				
			try:
				self.precision['midf'][1] += float(self.tp['midf'][i])/float(self.tp['midf'][i] + self.fp['midf'][i])		
			except ZeroDivisionError:
				pass
			
		self.precision['tf_idf'][1] = float(self.precision['tf_idf'][1])/float(self.case)
		self.precision['widf'][1] = float(self.precision['widf'][1])/float(self.case)
		self.precision['midf'][1] = float(self.precision['midf'][1])/float(self.case)
					
	def countRecall(self):	

		#micro				
		
		self.recall['tf_idf'][0] = float(sum(self.tp['tf_idf']))/float(sum(self.tp['tf_idf']) + sum(self.fn['tf_idf']))
		self.recall['widf'][0] = float(sum(self.tp['widf']))/float(sum(self.tp['widf']) + sum(self.fn['widf']))
		self.recall['midf'][0] = float(sum(self.tp['midf']))/float(sum(self.tp['midf']) + sum(self.fn['midf']))
		
		#macro
		
		for i in range(0, self.case):	
			try:
				self.recall['tf_idf'][1] += float(self.tp['tf_idf'][i])/float(self.tp['tf_idf'][i] + self.fn['tf_idf'][i])		
			except ZeroDivisionError:
				pass
				
			try:
				self.recall['widf'][1] += float(self.tp['widf'][i])/float(self.tp['widf'][i] + self.fn['widf'][i])		
			except ZeroDivisionError:
				pass
				
			try:
				self.recall['midf'][1] += float(self.tp['midf'][i])/float(self.tp['midf'][i] + self.fn['midf'][i])		
			except ZeroDivisionError:
				pass
		
		self.recall['tf_idf'][1] = float(self.recall['tf_idf'][1])/float(self.case)
		self.recall['widf'][1] = float(self.recall['widf'][1])/float(self.case)
		self.recall['midf'][1] = float(self.recall['midf'][1])/float(self.case)
		
	def countFmeasure(self):	

		for i in range(0,2):		
			try:					
				self.f_measure['tf_idf'][i] = float(2*self.precision['tf_idf'][i]*self.recall['tf_idf'][i])/float(self.precision['tf_idf'][i] + self.recall['tf_idf'][i])			
			except ZeroDivisionError:
				pass
				
			try:
				self.f_measure['widf'][i] = float(2*self.precision['widf'][i]*self.recall['widf'][i])/float(self.precision['widf'][i] + self.recall['widf'][i])	
			except ZeroDivisionError:
				pass
				
			try:
				self.f_measure['midf'][i] = float(2*self.precision['midf'][i]*self.recall['midf'][i])/float(self.precision['midf'][i] + self.recall['midf'][i])	
			except ZeroDivisionError:
				pass
		
	def countAccuracy(self):	

		#micro		
		
		self.accuracy['tf_idf'][0] = float(sum(self.tp['tf_idf']) + sum(self.tn['tf_idf']))/float(sum(self.tp['tf_idf']) + sum(self.fp['tf_idf']) + sum(self.fn['tf_idf']) + sum(self.tn['tf_idf']))
		self.accuracy['widf'][0] = float(sum(self.tp['widf']) + sum(self.tn['widf']))/float(sum(self.tp['widf']) + sum(self.fp['widf']) + sum(self.fn['widf']) + sum(self.tn['widf']))
		self.accuracy['midf'][0] = float(sum(self.tp['midf']) + sum(self.tn['midf']))/float(sum(self.tp['midf']) + sum(self.fp['midf']) + sum(self.fn['midf']) + sum(self.tn['midf']))
		
		#macro
		
		for i in range(0, self.case):		
			try:
				self.accuracy['tf_idf'][1] += float(self.tp['tf_idf'][i] + self.tn['tf_idf'][i])/float(self.tp['tf_idf'][i] + self.fp['tf_idf'][i] + self.fn['tf_idf'][i] + self.tn['tf_idf'][i])		
			except ZeroDivisionError:
				pass
				
			try:
				self.accuracy['widf'][1] += float(self.tp['widf'][i] + self.tn['widf'][i])/float(self.tp['widf'][i] + self.fp['widf'][i] + self.fn['widf'][i] + self.tn['widf'][i])		
			except ZeroDivisionError:
				pass
				
			try:
				self.accuracy['midf'][1] += float(self.tp['midf'][i] + self.tn['midf'][i])/float(self.tp['midf'][i] + self.fp['midf'][i] + self.fn['midf'][i] + self.tn['midf'][i])		
			except ZeroDivisionError:
				pass
		
		self.accuracy['tf_idf'][1] = float(self.accuracy['tf_idf'][1])/float(self.case)
		self.accuracy['widf'][1] = float(self.accuracy['widf'][1])/float(self.case)
		self.accuracy['midf'][1] = float(self.accuracy['midf'][1])/float(self.case)
		
	def insert(self, cursor, db):
		sql = self.insertQuery('micro', 'tf_idf')
		cursor.execute(sql)
		db.commit()
		
		sql = self.insertQuery('micro', 'widf')
		cursor.execute(sql)
		db.commit()
		
		sql = self.insertQuery('micro', 'midf')
		cursor.execute(sql)
		db.commit()
		
		sql = self.insertQuery('macro', 'tf_idf')
		cursor.execute(sql)
		db.commit()
		
		sql = self.insertQuery('macro', 'widf')
		cursor.execute(sql)
		db.commit()
		
		sql = self.insertQuery('macro', 'midf')
		cursor.execute(sql)
		db.commit()
		
	def insertQuery(self, average_type, term_weighting):
		if average_type == 'micro':
			index = 0
		if average_type == 'macro':
			index = 1
	
		sql = "INSERT INTO `performa`(`ID_SCENARIO`, `AVERAGE_TYPE`, `ROUNDING_TYPE`, `TERM_WEIGHTING`, `PRECISION`, `RECALL`, `ACCURACY`, `F_MEASURE`) VALUES (%d,'%s',%d,'%s',%f,%f,%f,%f)" %(self.id_skenario, average_type, self.case, term_weighting, self.precision[term_weighting][index], self.recall[term_weighting][index], self.accuracy[term_weighting][index], self.f_measure[term_weighting][index])
		
		return sql	