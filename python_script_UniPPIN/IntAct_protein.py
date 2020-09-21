import xml.etree.ElementTree as ET
protIDmap=dict()
def readFileList() :
	import glob
	xmlfiles = glob.glob('../datasets/IntAct/species/*[0-9].xml')
#	protIDmap=dict()
	# Protein ID
	for afile in xmlfiles :
		print(afile)
		buildProtPsimi(afile,protIDmap)
		buildPPIPsimi(afile)
#		for k,v in protIDmap.iteritems() :
#			print(k,v)

def buildProtPsimi (finName,protIDmap) :
	ns = {'psimins':'http://psi.hupo.org/mi/mif'}
	tree = ET.parse(finName) 
	root = tree.getroot()
	for interactor in root.findall('.//psimins:interactor',ns):
		intid = interactor.get('id')
		names = interactor.find('psimins:names',ns)
	#	print(intid)	
		label = names.find('psimins:shortLabel',ns).text
	# UniprotID validation
		protIDmap[intid]=confirmUniprotID(label.upper())
	#	print(label) 
	
IntActPPIpool=set()

# Moved to Protein.py
#def findUniprotID (uacc) :
#	if uacc in UniprotIDLib.keys() :
#		return UniprotIDLib[uacc].getUniprotID()
#	else :
#		return 'NA'

#def confirmUniprotID (uid) :
#	if not uid.endswith('_HUMAN') :
#		uid_cols=uid.split('-')
#		print(uid_cols[0])
#		return findUniprotID(uid_cols[0].upper())
#	else :
#		if uid in UniprotNameLib.values() :
#			return uid
#		else :
#			return 'NA'
	
def buildPPIPsimi (finName) :
#	import xml.etree.ElementTree as ET
	ns = {'psimins':'http://psi.hupo.org/mi/mif'}
	tree = ET.parse(finName) 
	root = tree.getroot()
	for interactor in root.findall('.//psimins:interactor',ns):
		names = interactor.find('psimins:names',ns)
#		print(names.tag)	
		label = names.find('psimins:shortLabel',ns).text
#		print(label) 
	for interaction in root.findall('.//psimins:interaction',ns):
		names = interaction.find('psimins:names',ns)
		label = names.find('psimins:shortLabel',ns).text
#		print(label)
#		for child in interaction :
#			print(child.tag)
		ppi_pair=[]
		for participants in interaction.findall('.//psimins:participant',ns):
			protname=participants.find('psimins:names',ns)
			if protname is not None :
				protlabel=protname.find('psimins:shortLabel',ns).text
#				print(label)
				interactorRef=participants.find('psimins:interactorRef',ns).text
				tuid = protIDmap[interactorRef]
#				if not tuid.endswith('_HUMAN') : 
#					tuid_cols=tuid.split('-')
#					uid=findUniprotID(tuid_cols[0].upper())
				#	if uid.endswith('_HUMAN') :
#					print(tuid+'   '+uid)
				ppi_pair.append(tuid)
				#	else :
				#		ppi_pair.append(tuid)
#				else :
#					uid=confirmUniprotID(tuid.upper())
#					print(tuid+'   '+uid)
#					ppi_pair.append(uid)
		if len(ppi_pair) >= 2 :
			if ppi_pair[0].endswith('_HUMAN') :
				for i in range(1,len(ppi_pair)) :
#					if frozenset(ppi_pair[0],ppi_pair[i]) not in IntActPPIpool :
					# Ignore Self-loop
					if ppi_pair[i].endswith('_HUMAN') :
						apair = frozenset([ppi_pair[0],ppi_pair[i]])
						if len(apair) == 2 :
							IntActPPIpool.add(apair)
#		for label in names.find('psimins:shortLabel',ns) :
#			print(label)


