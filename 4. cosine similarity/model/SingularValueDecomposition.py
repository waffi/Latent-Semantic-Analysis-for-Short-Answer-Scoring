#!/usr/bin/python

from numpy import identity, dot
from scipy.linalg import svd, inv

class SingularValueDecomposition:

	def generateSVD(self, matrix):
		self.U, self.S, self.Vt = svd(matrix)
		self.S = self.S * identity(len(self.S))
	
	def setMatrixDecomposition(self, U, S, Vt):
		self.U = U
		self.S = S
		self.Vt = Vt
	
	def setReductionSVD(self, k):
		self.Uk = self.U[:,0:k]
		self.Sk = self.S[0:k,0:k]
		self.Vtk = self.Vt[0:k,]
		
	def createQuery(self, v):
		return inv(self.Sk).dot(self.Uk.transpose()).dot(v).transpose()
	