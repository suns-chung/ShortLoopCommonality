BioPlexPPIpool=set()

def buildBioPlexPPI (finName) :
	import csv
	import sys
	csv.field_size_limit(sys.maxsize)
	with open(finName) as csvfile:
		protppireader = csv.reader(csvfile, delimiter='\t')
		next(protppireader, None)
		for row in protppireader :
			prot1 = row[2]
			prot2 = row[3]
			
#			if len(prot1) >= 2 and len(prot2) >=2 : 
			#	print(prot1[1] + ' ' + prot2[1])
			prot1_UniID = findUniprotID(prot1)
			prot2_UniID = findUniprotID(prot2)
			if (prot1_UniID != 'NA') and (prot2_UniID != 'NA') :
				apair = frozenset([prot1_UniID,prot2_UniID])
				if len(apair) == 2 :
					BioPlexPPIpool.add(apair)
