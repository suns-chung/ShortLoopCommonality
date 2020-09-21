BPMSPPIpool=set()
changedUniIDs=dict()

def buildChangedUniIDs (obsName,chfName) :
	import csv
	import sys
	csv.field_size_limit(sys.maxsize)
	with open(obsName) as csvfile :
		protIDmapreader = csv.reader(csvfile, delimiter='\t')
		for row in protIDmapreader :
			changedUniIDs[row[1]]='OBSOLETE'
	with open(chfName) as csvfile :
		protIDmapreader = csv.reader(csvfile, delimiter='\t')
		for row in protIDmapreader :
			changedUniIDs[row[1]]=row[2]

def buildBPMSPPI (finName) :
	import csv
	import sys
	csv.field_size_limit(sys.maxsize)
	with open(finName) as csvfile:
		protppireader = csv.reader(csvfile, delimiter='\t')
		next(protppireader, None)
		for row in protppireader :
			if len(row) == 3 :
				prot1 = row[0].split(':')
				prot2 = row[2].split(':')
				if prot1[0] in changedUniIDs.keys() :
					prot1_UniID = changedUniIDs[prot1[0]]
				else :
					prot1_UniID = prot1[0]
				if prot2[0] in changedUniIDs.keys() :
					prot2_UniID = changedUniIDs[prot2[0]]
				else :
					prot2_UniID = prot2[0]

				if (prot1_UniID != 'OBSOLETE') and (prot2_UniID != 'OBSOLETE') :
					apair = frozenset([prot1_UniID,prot2_UniID])
					if len(apair) == 2 :
						BPMSPPIpool.add(apair)
