ENSPUniprotIDLib=dict()

def buildENSP2UniprotIDLib (finName) :
	import csv
	import sys
#	UniprotIDLib = dict()
	csv.field_size_limit(sys.maxsize)
	with open(finName) as csvfile:
		protidreader = csv.reader(csvfile, delimiter='\t')
		for row in protidreader:
			if len(row) >= 5 :
				UniprotCols=row[1].split('|')
#				print(row[2]+' '+UniprotCols[1])
				ENSPUniprotIDLib[row[2]] = UniprotCols[0]

StringPPIpool=set()

def buildStringPPI (finName) :
	import csv
	import sys
	csv.field_size_limit(sys.maxsize)
	with open(finName) as csvfile:
		protppireader = csv.reader(csvfile, delimiter=' ')
		next(protppireader, None)

		for row in protppireader :
			prot1 = row[0].split('.')
			prot2 = row[1].split('.')
			if int(row[6]) > 500 :		# Only experimental score higher than 500 (confidence > 0.5)
				prot1_UniID = ENSPUniprotIDLib.get(prot1[1],None)
				prot2_UniID = ENSPUniprotIDLib.get(prot2[1],None)
				if (prot1_UniID != None) and (prot2_UniID != None) :
					apair = frozenset([prot1_UniID,prot2_UniID])
					if len(apair) == 2 :
						StringPPIpool.add(apair)
