exec(open('Protein_UniACC.py').read())
exec(open('build_PPI_AdjList.py').read())
exec(open('find_shortloops_from_PPIN.py').read())

CML_PPIN=build_PPIN_from_sif('CML_PPIN.sif')
CML_AdjList=build_ProtAdjList(CML_PPIN)
CML_Slp3=find_shortloops(CML_AdjList,3)
CML_Slp4=find_shortloops(CML_AdjList,4)

writeLoopSets2File('CML_ShortLoop3.dat',CML_Slp3)

