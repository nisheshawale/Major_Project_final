__author__ = ''

import re
import os
import glob
import textract

class CorpusParser:

	def __init__(self, filename):
		self.filename = filename
		self.regex = re.compile('^#\s*\d+')
		self.corpus = dict()
		self.path = os.path.dirname(os.path.abspath(__file__)) + '/files/'

	def parse(self):

#		with open(self.filename) as f:
#			s = ''.join(f.readlines())
#		blobs = s.split('###')[1:]
		
		files_list = os.listdir(self.path)
		files_list.remove(self.filename)
		for x in files_list:
			for f in glob.glob(self.path+x):
				texts = textract.process(f)
				s = texts.decode('utf-8')
			
			#with open(self.path+x,"r") as f:
			#	s= f.read()
			text = s.split()#[1:]
			#print(text)
			docid = x
			#print(docid)
			self.corpus[docid] = text

	def get_corpus(self):
		return self.corpus


class QueryParser:

	def __init__(self, filename):
		self.filename = filename
		self.queries = []
		self.path = os.path.dirname(os.path.abspath(__file__)) + '/files/'

	def parse(self):
		with open(self.path + self.filename) as f:
			lines = ''.join(f.readlines())
			#print(lines)
		self.queries = [x.rstrip() for x in lines.split()]#.split('\n')
		#print(len(self.queries[0]))

	def get_queries(self):
		return self.queries


# if __name__ == '__main__':
# 	qp = QueryParser('text/queries.txt')
	#print(qp.get_queries())