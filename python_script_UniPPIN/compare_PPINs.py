
#def getPPIPDBs(uniProtIDs) :

def getUniIDfromName(uniName) :
	return list(UniprotNameLib.keys())[list(UniprotNameLib.values()).index(uniName)]

def get1stNeighbourSubPPIN(aPPIN, uniProtIDs) :
	subPPIN = set()
#	print(uniProtIDs)
	for aset in aPPIN :
		alist = list(aset)
		#print(alist) 
		if (alist[0] in uniProtIDs) or (alist[1] in uniProtIDs) :
			subPPIN.add(aset)
	return subPPIN	

def getSubPPIN(aPPIN, uniProtIDs) :
	subPPIN = set()
#	print(uniProtIDs)
	for aset in aPPIN :
		alist = list(aset)
		#print(alist) 
		if (alist[0] in uniProtIDs) and (alist[1] in uniProtIDs) :
			subPPIN.add(aset)
	return subPPIN	


def getIntersection(PPINlists) :
	aset = PPINlists[0]
	for each in PPINlists :
		aset=aset.intersection(each)
	return aset

def getNumberPPIs(PPINlists) :
	for each in PPINlists :
		print('# of proteins : '+str(getNumProts(each)))
		print('# of interactions : '+str(len(each)))

def getNumProts(aPPIN) :
	prots=set()
	for aset in aPPIN :
		alist = list(aset)
		prots.add(alist[0])
		prots.add(alist[1])
	return len(prots)

def getUnion(PPINlists) :
	aset = PPINlists[0]
	for each in PPINlists :
		aset=aset.union(each)
	return aset

def writePPINtoSIF(foutname, aPPIN) :
	fwriter=open(foutname,'w')
	for aset in aPPIN :
		alist = list(aset)
		fwriter.write(alist[0]+'\tppi\t'+alist[1]+'\n')
	fwriter.close()
