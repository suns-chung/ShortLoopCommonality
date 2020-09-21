BioGRIDPPIpool=set()
BioGRIDEntrezpool=set()

def buildBioGRIDPPI (finName) :
	import csv
	import sys
	csv.field_size_limit(sys.maxsize)
	with open(finName) as csvfile:
		protppireader = csv.reader(csvfile, delimiter='\t')
		next(protppireader, None)
		for row in protppireader :
			if row[0].startswith('entrez gene/locuslink:') and row[1].startswith('entrez gene/locuslink:'):
				prot1 = row[0].split(':')
				prot2 = row[1].split(':')
			else :
				print(row[0]+' '+row[1])
			
					
			if len(prot1) >= 2 and len(prot2) >=2 : 
			#	print(prot1[1] + ' ' + prot2[1])
					
				prot1_UniID = getUniprotIDEntrez(prot1[1].strip())
				prot2_UniID = getUniprotIDEntrez(prot2[1].strip())

				if (prot1_UniID != 'NA') and (prot2_UniID != 'NA') :
					apair = frozenset([prot1_UniID,prot2_UniID])
					if len(apair) == 2 :
						BioGRIDPPIpool.add(apair)
				else :
					apair = frozenset([prot1[1],prot2[1]])
					if len(apair) == 2 :
						BioGRIDEntrezpool.add(apair)
			
