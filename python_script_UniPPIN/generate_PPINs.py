exec(open('Protein_UniACC.py').read())
buildUniprotIDLib('../datasets/HUMAN_9606_idmapping_selected.tab')
buildUniprotNameLib('../datasets/HUMAN_9606_idmapping_selected.tab')


#IntAct 
exec(open('IntAct_protein.py').read())
readFileList()
#output : IntActPPIpool

#StringDB
exec(open('StringDB_protein.py').read())
buildENSP2UniprotIDLib('../datasets/String-DB/v10/9606_reviewed_uniprot_2_string.04_2015.tsv')
buildStringPPI('../datasets/String-DB/v10/9606.protein.links.detailed.v10.txt')
#output : StringPPIpool

#DIP
exec(open('DIP_protein.py').read())
buildDIPPPI('../datasets/DIP/Hsapi20160731.txt')
#output : DIPPPIpool

#BioGRID
exec(open('BioGRID_protein.py').read())
buildBioGRIDPPI('../datasets/BioGRID/BIOGRID-ORGANISM-Homo_sapiens-3.4.144.mitab.txt')
#output : BioGRIDPPIpool

#HPRD
exec(open('HPRD_protein.py').read())
findHPRDUniprot('../datasets/hprd/FLAT_FILES_072010/HPRD_ID_MAPPINGS.txt')
buildHPRDPPI('../datasets/hprd/FLAT_FILES_072010/BINARY_PROTEIN_PROTEIN_INTERACTIONS.txt')
#output : HPRDPPIpool

#Cell BPMS by Marcotte&Emilli
exec(open('Cell_BPMS_protein.py').read())
buildChangedUniIDs('../datasets/UniprotIDmapping/Uniprot_BPMS_Obsolete.tab','../datasets/UniprotIDmapping/Uniprot_BPMS_Changed.tab')
buildBPMSPPI('../datasets/hspn/hspnppi.sif')
#output : BPMSPPIpool

#Cell Y2H 2014 by Vidal
exec(open('Cell_Y2H_vidal_protein.py').read())
buildY2HPPI('../datasets/vidal14/HI-II-14.tsv')
#output : Y2HPPIpool

#Cell BioPlex 2015 by Gygi
exec(open('BioPlex_protein.py').read())
buildBioPlexPPI('../datasets/BioPlex/BioPlex_interactionList_v4.tsv')
#output : BioPlexPPIpool

#Cell 3D MS Weak Interaction 2015 by Mann
exec(open('HeinMS_protein.py').read())
buildHeinMSPPI('../datasets/HeinMS/BIOGRID-PUBLICATION-188719-3.4.137.mitab.txt')
#output : HeinMSPPIpool

#Nature Metazaoa by Marcortte&Emilli
exec(open('Metazoan_protein.py').read())
buildMetazoaPPI('../datasets/Metazoan/Hsapiens_projected_PPI_metazoan_conserved_map.txt')
#output : MetazoaPPIpool


