UniprotNameLib=dict()

class Protein :
#	UniprotAC
#	UniprotID
#	EntrezGene
#	PDB
#	PubMed
#	Ensembl_Pro
#	PrimaryName

	def __init__ (self, uac, uid, egi, pdb, ensg, enpro, entr, goids) :
		self.UniprotAC = uac
		self.UniprotID = uid
		self.EntrezGene = egi
		self.PDB = pdb
		self.Ensembl_Gen = ensg
		self.Ensembl_Pro = enpro
		self.Ensembl_Tra = entr
		self.putGOBPIDs(goids)
#		self.Interactors = set()
#		if self.UniprotAC in UniprotNameLib.keys()  : 
#			self.PrimaryName = UniprotNameLib[self.UniprotAC]
#		else :
#			self.PrimaryName = 'Unknown'
	def putGOBPIDs(self, goids) :
		self.GOBP_IDs=set()
		for aId in goids.split('; ') :
			self.GOBP_IDs.add(aId)
		
	def getEntrezID(self) :
		return self.EntrezGene
	def getUniprotAC(self) :
		return self.UniprotAC
	def getUniprotID(self) :
		return self.UniprotID
	def getEnsemblGenID(self) :
		return self.Ensembl_Gen
	def getEnsemblTraID(self) :
		return self.Ensembl_Tra
	def getEnsemblProtID(self) :
		return self.Ensembl_Pro
	def getPDB(self) :
		return self.PDB
	def getGOIDs(self) :
		return self.GOBP_IDs
	def printStr(self) :
#		return self.UniprotAC+'\t'+self.UniprotID+'\t'+self.EntrezGene+'\t'+self.PDB+'\t'+self.Ensembl_Pro+'\t'+self.PrimaryName
		return self.UniprotAC+'\t'+self.UniprotID+'\t'+self.EntrezGene+'\t'+self.PDB+'\t'+self.Ensembl_Gen+'\t'+self.Ensembl_Pro+'\t'+self.Ensembl_Tra
#	def addProtInteractor(self, anewprot) :
#		self.Interactor.add(anewprot)


UniprotIDLib=dict()
EntrezUniprotIDLib=dict()
ENSTUniprotIDLib=dict()
ENSGUniprotIDLib=dict()
ENSPUniprotIDLib=dict()
missingUniprotNames=dict()

def buildUniprotNameLib (finName) :
	import csv
	import sys
	csv.field_size_limit(sys.maxsize)
	with open(finName) as csvfile:
		protidreader = csv.reader(csvfile, delimiter='\t')
		for row in protidreader:
			if row[2] != '' : 
				UniprotNameLib[row[0]] = row[1]
			else :
				UniprotNameLib[row[0]] = row[1]

def buildUniprotIDLib (finName) :
	import csv
	import sys
#	UniprotIDLib = dict()
	csv.field_size_limit(sys.maxsize)
	with open(finName) as csvfile:
		protidreader = csv.reader(csvfile, delimiter='\t')
		for row in protidreader:
			aProt = Protein(row[0], row[1], row[2], row[5], row[18], row[20], row[19], row[6])
#			print(aProt.printStr())
			UniprotNameLib[aProt.getUniprotAC()] = aProt.getUniprotID()
			UniprotIDLib[aProt.getUniprotAC()] = aProt
			buildEntrezUniprotIDLib(aProt.getEntrezID(), aProt.getUniprotAC(), aProt.getUniprotID())
			buildENSTUniprotLib(aProt.getEnsemblTraID(), aProt.getUniprotAC(), aProt.getUniprotID())
			buildENSGUniprotLib(aProt.getEnsemblGenID(), aProt.getUniprotAC(), aProt.getUniprotID())	
			buildENSPUniprotLib(aProt.getEnsemblProtID(), aProt.getUniprotAC(), aProt.getUniprotID())	
#			EntrezUniprotIDLib[aProt.getUniprotID()] = aProt.getEntrezID()

def addMissingUniprotNameLib (finName) :
	import csv
	import sys
#	csv.field_size_limit(sys.maxsize)
	with open(finName) as csvfile:
		protidreader = csv.reader(csvfile, delimiter='\t')
	#	next(protidreader)
		for row in protidreader:
			if row[2] != '' and row[1] != row[2] : 
				missingUniprotNames[row[1]] = row[2]

#Convert all below functions to use Uniprot Accession Number as key
 
def buildENSGUniprotLib (ENSG_IDs, aUniAC, aUniID) :
	for aid in ENSG_IDs.split(';') :
		aENSG=aid.strip()
		if len(aENSG) > 0:
			if aENSG not in ENSGUniprotIDLib.keys() :
				ENSGUniprotIDLib[aENSG]=aUniAC
			else :
				if not aUniID.startswith(aUniAC) :
						ENSGUniprotIDLib[aENSG]=aUniAC


def buildENSTUniprotLib (ENST_IDs, aUniAC, aUniID) :
	for aid in ENST_IDs.split(';') :
		aENST=aid.strip()
		if len(aENST) > 0:
			if aENST not in ENSTUniprotIDLib.keys() :
				ENSTUniprotIDLib[aENST]=aUniAC
			else :
				if not aUniID.startswith(aUniAC) :
						ENSTUniprotIDLib[aENST]=aUniAC
def buildENSPUniprotLib (ENSP_IDs, aUniAC, aUniID) :
	for aid in ENSP_IDs.split(';') :
		aENSP=aid.strip()
		if len(aENSP) > 0:
			if aENSP not in ENSPUniprotIDLib.keys() :
				ENSPUniprotIDLib[aENSP]=aUniAC
			else :
				if not aUniID.startswith(aUniAC) :
						ENSPUniprotIDLib[aENSP]=aUniAC

def getUniprotENSP(ensp) :
	if ensp in ENSPUniprotIDLib.keys() :
		return ENSPUniprotIDLib[ensp]
	else :
		return 'NA'


def getUniprotENST(enst) :
	if enst in ENSTUniprotIDLib.keys() :
		return ENSTUniprotIDLib[enst]
	else :
		return 'NA'

def getUniprotENSG(ensg) :
	if ensg in ENSGUniprotIDLib.keys() :
		return ENSGUniprotIDLib[ensg]
	else :
		return 'NA'
			
def findUniprotID (uacc) :
	if uacc in UniprotIDLib.keys() :
		return UniprotIDLib[uacc].getUniprotID()
	else :
		return 'NA'

def confirmUniprotID (uid) :
	if not uid.endswith('_HUMAN') :
		uid_cols=uid.split('-')
#		print(uid_cols[0])
		return findUniprotID(uid_cols[0].upper())
	else :
		if uid in UniprotNameLib.values() :
			return uid
		else :
			return 'NA'

def buildEntrezUniprotIDLib(aEgid, aUniAC, aUniID) :
	if aEgid not in EntrezUniprotIDLib.keys() :
		EntrezUniprotIDLib[aEgid] = aUniAC
	else :
#		print('Same Entrez ID : '+EntrezUniprotIDLib[aEgid]+' '+aUniID)

		if not aUniID.startswith(aUniAC) :
			EntrezUniprotIDLib[aEgid] = aUniAC

def getUniprotIDEntrez(egi) :
	if egi in EntrezUniprotIDLib.keys() :
		return EntrezUniprotIDLib[egi]
	else : 
		return 'NA'


