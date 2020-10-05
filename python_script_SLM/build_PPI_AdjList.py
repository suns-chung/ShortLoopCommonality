
#def getPPIPDBs(uniProtIDs) :

class Prot_Interactors() :
	def __init__ (self, uid, interactor) :
		self.UniprotID = uid
	#	self.UniprotAC = UniprotID2Name[uid]
		self.interactors = set()
		self.addInteractor(interactor)

	def addInteractor(self, interactor) :
		self.interactors.add(interactor)
	
	def getInteractors(self) :
		return self.interactors

UniprotID2Name=dict(zip(UniprotNameLib.values(), UniprotNameLib.keys()))
	
#ProtAdjList=dict()

def build_PPIN_from_sif (finName) :
    import csv
    import sys
    csv.field_size_limit(sys.maxsize)
    ppiPool=set()
    with open(finName) as csvfile:
        protppireader = csv.reader(csvfile,delimiter='\t')
        for row in protppireader :
            if len(row) == 3:
                prot1_UniID = row[0]
                prot2_UniID = row[2]
                apair = frozenset([prot1_UniID,prot2_UniID])
                if len(apair) == 2:
                    ppiPool.add(apair)
        return ppiPool

def build_ProtAdjList(aPPIN) :
	ProtAdjList=dict()
	for aset in aPPIN :
		alist = list(aset)
		if alist[0] not in ProtAdjList.keys() :
			aProt_Ints = Prot_Interactors(alist[0], alist[1])
			ProtAdjList[alist[0]]=aProt_Ints
		else :
			ProtAdjList[alist[0]].addInteractor(alist[1])

		if alist[1] not in ProtAdjList.keys() :
			aProt_Ints = Prot_Interactors(alist[1], alist[0])
			ProtAdjList[alist[1]]=aProt_Ints
		else :
			ProtAdjList[alist[1]].addInteractor(alist[0])
	return ProtAdjList
