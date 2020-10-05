# Scripts for generating short loops (length=3 and 4) and short loop commonality from short loops (length=3)

## To find short loops in a PPIN

**Input file: A tab-delimited file**
```
protein1[tab]ppi[tab]protein2
...
```

###### Pythons scripts ######
```
Protein_UniACC.py # to define protein data structures and functions 

build_PPI_AdjList.py # to load a PPIN (i.e. input file) 

find_shortloops_from_PPIN.py # to calculate short loops from a PPIN
```

**Output: A comma delimited short loop sets**
```
protein1,protein2,protein3
...
```

**Example:**

*run_PPIN_ShortLoop_example.py*

- Input : CML_PPIN.sif

- Output : CML_ShortLoop3.dat


## To find short loop commonality from short loops (length=3)

**Input file: A comma delimited file**
```
protein1,protein2,protein3
...
```

###### Pythons scripts ######
```
find_shortloopcommonality.py # parameters with output file name and percentage of common short loops
```

**Output: commonality protein pairs and their common interaction partners**
```
protein1, protein2 : set([frozenset([protein3, protein4]), frozenset([protein5, protein6]))
...
```

**Example:**

*run_ShortLoop3_commonality_example.py*

- Input : CML_ShortLoop3.dat

- Output : CML_ShortLoopCommonality_95_stringent.dat
