Y2HPPIpool=set()

VidalEntrezUnmapped=set()

def buildY2HPPI (finName) :
	import csv
	import sys
	csv.field_size_limit(sys.maxsize)
	with open(finName) as csvfile:
		protppireader = csv.reader(csvfile, delimiter='\t')
		next(protppireader, None)
		for row in protppireader :
			if len(row) == 4 :
				prot1_UniID = getUniprotIDEntrez(row[0])
				prot2_UniID = getUniprotIDEntrez(row[2])
			
				if (prot1_UniID != 'NA') and (prot2_UniID != 'NA') :
					apair = frozenset([prot1_UniID,prot2_UniID])
					if len(apair) == 2 :
						Y2HPPIpool.add(apair)
				else :
					if (prot1_UniID == 'NA'):
						VidalEntrezUnmapped.add(row[0])
					if (prot2_UniID == 'NA'):
						VidalEntrezUnmapped.add(row[2])
