DIPPPIpool=set()

def buildDIPPPI (finName) :
	import csv
	import sys
	csv.field_size_limit(sys.maxsize)
	with open(finName) as csvfile:
		protppireader = csv.reader(csvfile, delimiter='\t')
		next(protppireader, None)
		for row in protppireader :
			prot1 = row[0].split('|uniprotkb:')
			prot2 = row[1].split('|uniprotkb:')
			
			if len(prot1) >= 2 and len(prot2) >=2 : 
			#	print(prot1[1] + ' ' + prot2[1])
			# Apr 2017 : Changed Uniprot Accession name
			#	prot1_UniID = findUniprotID(prot1[1])
			#	prot2_UniID = findUniprotID(prot2[1])
			#	if (prot1_UniID != 'NA') and (prot2_UniID != 'NA') :
			#		apair = frozenset([prot1_UniID,prot2_UniID])
				apair = frozenset([prot1[1], prot2[1]])
				if len(apair) == 2 :
					DIPPPIpool.add(apair)
