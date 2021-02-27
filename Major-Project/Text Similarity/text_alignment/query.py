__author__ = ''

from invdx import build_data_structures
from rank import score_BM25
import operator


class QueryProcessor:
	def __init__(self, queries, corpus):
		self.queries = queries
		# self.threshold = threshold
		self.index, self.dlt = build_data_structures(corpus)

	def run(self):
		#results = []
		#results.append(self.run_query(query))
		#for query in self.queries:
		#	results.append(self.run_query(query))
		#print(self.queries)
		results = self.run_query(self.queries)
		#print(results)
		return results
		#return results

	def run_query(self, query):
		query_result = dict()
		for term in query:
			if term in self.index:
				doc_dict = self.index[term] # retrieve index entry
				for docid, freq in doc_dict.items(): #for each document and its word frequency
					score = score_BM25(n=len(doc_dict), f=freq, qf=1, r=0, N=len(self.dlt),
									   dl=self.dlt.get_length(docid), avdl=self.dlt.get_average_length()) # calculate score
					if docid in query_result: #this document has already been scored once
						query_result[docid] += score
					else:
						query_result[docid] = score
		#print(query_result)
		return query_result
