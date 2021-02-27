from parse import *
from query import QueryProcessor
import operator


def source_retrieval(filename, threshold):
	qp = QueryParser(filename=filename)
	cp = CorpusParser(filename=filename)
	qp.parse()
	queries = qp.get_queries()
	# print(queries)
	cp.parse()
	corpus = cp.get_corpus()
	# print(corpus)
	proc = QueryProcessor(queries, corpus)
	results = proc.run()
	# print(results)
	qid = 0
	#for result in results:
	#print(result)
	result = results
	total = sum(result.values())
	sorted_y = sorted(result.items(), key=operator.itemgetter(1))
	sorted_x = []

	for element in sorted_y:
		if element[1] > float(threshold):
			sorted_x.append(element)
	
	lista = [k[1]/total for k in sorted_x]
	print("=========================")
	print(sorted_x)
	print(lista)
	print("=========================")
	# print(sum(lista))
	#print(sorted_x)
	count = 0
	for l in lista:
		if l>0.05:
			count = count +1

	sorted_x.reverse()
	if count>5:
		count = 5
	index = 0
	output = []
	for i in sorted_x[:count]:
		tmp = (i[0], index, i[1])
		output.append(i[0])
		# print('Q0\t{:>4}\t{:>2}\t{:>12}\tBM25'.format(*tmp))
		index += 1
	qid += 1
	print(output)
	return output
		#print(result.items())

		#if qid == 4:
		#	break


# if __name__ == '__main__':
# 	main()
# source_retrieval('a.txt')
