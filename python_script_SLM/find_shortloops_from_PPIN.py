import datetime
#def getPPIPDBs(uniProtIDs) :


def find_shortloops(pAdjList, length) :
	print(datetime.datetime.now())
	loop3=set()
	loop4=set()
 	
	for k,v in pAdjList.items() :
		aProtAdj = v
		adjList = list(aProtAdj.getInteractors())
		for idx in range(0,len(adjList)) :
			nProt=adjList[idx]
			if length == 3 :
				loop3Prots = (aProtAdj.getInteractors()).intersection(pAdjList[nProt].getInteractors())
				if len(loop3Prots) > 0 :
						for cProt in loop3Prots :
					#		print(nProt)
							loop3.add(frozenset([k,nProt,cProt]))
			if length == 4:
				for idx2 in range(idx+1, len(adjList)) :
					nProt2=adjList[idx2]
					nProt1_adj=pAdjList[nProt].getInteractors()
					nProt2_adj=pAdjList[nProt2].getInteractors()
					loop4Prots = nProt1_adj.intersection(nProt2_adj)
					if len(loop4Prots) > 0 :
						for cProt in loop4Prots :
							if cProt != k :
								if (tuple([k,nProt,cProt,nProt2]) not in loop4) and (tuple([nProt,cProt,nProt2,k]) not in loop4) and (tuple([cProt,nProt2,k,nProt]) not in loop4) and (tuple([nProt2,k,nProt,cProt]) not in loop4) :
									loop4.add(tuple([k,nProt,cProt,nProt2]))
									loop4.add(tuple([k,nProt2,cProt,nProt]))
	
	print(datetime.datetime.now())	
	if length == 3 :
		return loop3
	elif length == 4:
		rt_loop4 = set()
		for atuple in loop4:
			if tuple([atuple[0],atuple[3],atuple[2],atuple[1]]) not in rt_loop4 :
				rt_loop4.add(atuple)
		return rt_loop4


def writeLoopSets2File(foutname, aSet) :
    fwriter=open(foutname,'w')
    for anItem in aSet :
        fwriter.write(','.join(anItem)+'\n')
    fwriter.close()


