import gc
import random

#input file: short loops (length=3) comma delimited file format
#e.g. prot1,prot2,prot3

def process_loop2adjset(fname) :
	import csv
	import sys
	csv.field_size_limit(sys.maxsize)
	loopDic = dict()
	with open(fname) as csvfile:
		loopreader = csv.reader(csvfile, delimiter=',')
		for row in loopreader :
			prot1=row[0]
			prot2=row[1]
			prot3=row[2]
			if prot1 not in loopDic :
				loopDic[prot1]=set()
			loopDic[prot1].add(frozenset([prot2,prot3]))

			if prot2 not in loopDic :
				loopDic[prot2]=set()
			loopDic[prot2].add(frozenset([prot1,prot3]))
	
			if prot3 not in loopDic :
				loopDic[prot3]=set()
			loopDic[prot3].add(frozenset([prot1,prot2]))
		
	return loopDic				

def process_loop2pairs(fname) :
	import csv
	import sys
	csv.field_size_limit(sys.maxsize)
	loopPairs=set()
	with open(fname) as csvfile :
		loopreader = csv.reader(csvfile,delimiter=',')
		for row in loopreader :
			prot1 = row[0]
			prot2 = row[1]
			prot3 = row[2]

			loopPairs.add(frozenset([prot1,prot2]))
			loopPairs.add(frozenset([prot3,prot2]))
			loopPairs.add(frozenset([prot1,prot3]))
	return loopPairs

def write_loopPairs2file(loopPairs, fname) :
	fout=open(fname,'w')

	for apair in loopPairs :
		apairList=list(apair)
		fout.write(apairList[0]+'\t'+apairList[1]+'\n')
	fout.close()


def comp2sets(aDic,loopPairs,akey,bkey,cutoff):
	tmpPairSet=set()
	iSet=aDic[akey]
	jSet=aDic[bkey]
	if len(iSet) > 3 and len(jSet) > 3:
		ijPair=frozenset([akey, bkey])
		if ijPair not in loopPairs and ijPair not in tmpPairSet:
			if len(iSet.intersection(jSet)) > max(min(len(iSet),len(jSet))*float(cutoff),3) :
				return str(iSet.intersection(jSet))

def find_ShortLoopCommonality(aDic,loopPairs,loopHomName,cutoff) :
	keyList= list(aDic.keys())
	fout=open(loopHomName,'w')
	
	for idx in range(0,len(keyList)) :
		print(idx)
		for jdx in range(idx+1,len(keyList)) :
			rt_str=comp2sets(aDic,loopPairs,keyList[idx],keyList[jdx],cutoff)
			if rt_str is not None and len(rt_str) > 0:
				fout.write(keyList[idx]+', '+keyList[jdx]+' : '+rt_str+'\n')

	fout.close()

def find_randSLC(aDic,loopPairs,rand_size,cutoff) :
	keyList= list(aDic.keys())
	random.shuffle(keyList)
	comm_cnt=0
	
	for idx in range(0,rand_size) :
		print(idx)
		for jdx in range(idx+1,len(keyList)) :
				rt_str=comp2sets(aDic,loopPairs,keyList[idx],keyList[jdx],cutoff)
			if rt_str is not None and len(rt_str) > 0:
				comm_cnt=comm_cnt+1

	return comm_cnt


