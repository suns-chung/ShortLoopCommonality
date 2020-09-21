MetazoaPPIpool=set()

def buildMetazoaPPI (finName) :
	import csv
	import sys
	csv.field_size_limit(sys.maxsize)
	with open(finName) as csvfile:
		protppireader = csv.reader(csvfile, delimiter='\t')
		next(protppireader, None)

		for row in protppireader :
			if len(row) > 2 :
				prot1 = row[0].split('||')
				prot2 = row[1].split('||')
				for isoProt1 in prot1 :
					isoProt1_UniID = getUniprotENSG(isoProt1)
					for isoProt2 in prot2 :
						isoProt2_UniID = getUniprotENSG(isoProt2)
						if (isoProt1_UniID is not 'NA') & (isoProt2_UniID is not 'NA') :
							apair = frozenset([isoProt1_UniID,isoProt2_UniID])
							if len(apair) == 2 :
								MetazoaPPIpool.add(apair)  
