import requests
#import json

def runCommand(cmd):
	durations = requests.get(cmd).json()['durations']
	
	output = [[x[i] for x in durations] for i in range(len(durations[0]))]
	
	resultFile = open('results.txt', 'w')
	for line in output:
		for i,val in enumerate(line):
			resultFile.write(str(float(val)/60))	# convert seconds to minutes
			if i+1 < len(line):
				resultFile.write('\t ')
		resultFile.write('\n')
		
	print(len(output))
	
	
def buildCommand(sources, dests):
	coords = []
	coords.extend(sources)
	coords.extend(dests)
	coords = swapLatLongAndTrim(coords)

	curlcmd = 'http://router.project-osrm.org/table/v1/driving/'
	for coord in coords:
			curlcmd += coord
			if coord != coords[-1]:
				curlcmd += ';'
	
	curlcmd += '?'
	curlcmd += 'sources='
	for i,pt in enumerate(sources):
		curlcmd += str(i)
		if i+1 < len(sources):
			curlcmd += ';'
	
	curlcmd += '&'
	curlcmd += 'destinations='
	for i, pt in enumerate(dests):
		curlcmd += str(i+len(sources))
		if i+1 < len(dests):
			curlcmd += ';'
	
	'''
	curlcmd += '?'
	curlcmd += 'annotations=distance,duration'
	'''
	return curlcmd

def swapLatLongAndTrim(coords):
	lats = []
	longs = []
	for coord in coords:
		latlong = coord.split(',')
		lats.append(latlong[0][:-7])
		longs.append(latlong[1][:-7])
	
	swapped = []
	for i,lat in enumerate(lats):
		swappedCoord = longs[i]
		swappedCoord += ','+lat

		swapped.append(swappedCoord)
	return swapped

def getSources():
	file = open("C:\\Users\\Kerry\\coding\\driveTimes\\coords")
	sourcesLine = file.readline()
	cells = sourcesLine.split('\t')
	
	sources = []
	for cell in cells:
		cell = cell.replace(' ', "")
		cell = cell.replace('\n', "")
		if len(cell) == 0:
			continue
		else:
			#we have a coordinate, probably
			sources.append(cell)
	return sources
			
def getDestinations():
	file = open("C:\\Users\\Kerry\\coding\\driveTimes\\coords")
	line = file.readline()
	line = file.readline()
	line = file.readline()

	dests = []	
	while line:
		line = file.readline()
		if not line:
			break

		dest = line.strip()
		dest = dest.replace('\n','')
		dest = dest.replace(' ','')

		if len(dest) ==0:
			continue
		else:
			dests.append(dest)
	return dests
	
if __name__ == '__main__':
	sources = getSources()
	dests = getDestinations()

	#print(sources)
	#print(dests)
	
	cmd = buildCommand(sources,dests)
	#print(cmd)
	runCommand(cmd)