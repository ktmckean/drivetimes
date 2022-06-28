if __name__ == '__main__':
	lines = []
	for line in open('curlResults.txt'):
		line = line.strip()
		fromSrc = line.split(',')
		lines.append(fromSrc)
		
	print(lines)
	'''
	output = [[],[],[],[]]
	for i,col in enumerate(lines[0]):
		for j,line in enumerate(lines):
			output[j].append(line[i])
	'''
	output = [[x[i] for x in lines] for i in range(4, len(lines[0]))]
	
	resultFile = open('results.txt', 'w')
	for line in output:
		for i,val in enumerate(line):
			resultFile.write(str(float(val)/60))
			if i+1 < len(line):
				resultFile.write('\t ')
		resultFile.write('\n')
		