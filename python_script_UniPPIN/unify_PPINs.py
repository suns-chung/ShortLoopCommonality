exec(open('generate_PPINs.py').read())
exec(open('compare_PPINs.py').read())
#
Uni_PPINs=getUnion((BPMSPPIpool, BioGRIDPPIpool, BioPlexPPIpool, DIPPPIpool, HPRDPPIpool, HeinMSPPIpool, IntActPPIpool, MetazoaPPIpool, StringPPIpool, Y2HPPIpool))
#Uni_PPINs=getUnion((BPMSPPIpool, BioPlexPPIpool)) #, DIPPPIpool, HPRDPPIpool, HeinMSPPIpool, MetazoaPPIpool, StringPPIpool, Y2HPPIpool))


UniACC_PPINs=set()
#Unmapped=set()
Deleted=set()

for appi in Uni_PPINs :
	prot1_ACC=None
	prot2_ACC=None
	if list(appi)[0] in UniprotNameLib.values() : 
		prot1_ACC = getUniIDfromName(list(appi)[0])
	elif list(appi)[0] in missingUniprotNames.keys() :
		prot1_ACC = getUniIDfromName(missingUniprotNames[list(appi)[0]])
	
	if list(appi)[1] in UniprotNameLib.values() : 
		prot2_ACC = getUniIDfromName(list(appi)[1])
	elif list(appi)[1] in missingUniprotNames.keys() :
		prot2_ACC = getUniIDfromName(missingUniprotNames[list(appi)[1]])
	
	if len(set([prot1_ACC,prot2_ACC])) == 2 :
		UniACC_PPINs.add(frozenset([prot1_ACC,prot2_ACC]))
	else :
		Deleted.add(appi)	

writePPINtoSIF('UniPPIN_ACC.sif',UniACC_PPINs)
