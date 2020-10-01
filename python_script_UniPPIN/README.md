# Scripts for generating a unified large-scale human protein-protein interaction network (UniPPIN) which amalgamates multiple protein-protein interaction resources. 

# Prerequisite: the UniPPIN is based on UniProt accession ID so download ID mapping file from the UniProt and unzip it
ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/idmapping/by_organism/HUMAN_9606_idmapping.dat.gz

# Download human PPINs from different resources

##Public databases:

IntAct: ftp://ftp.ebi.ac.uk/pub/databases/intact/current/all.zip

BioGRID: https://downloads.thebiogrid.org/File/BioGRID/Release-Archive/BIOGRID-4.1.190/BIOGRID-ORGANISM-4.1.190.mitab.zip

Human Protein Reference Database (HPRD): http://hprd.org/download

String-DB: https://stringdb-static.org/download/protein.links.v11.0/9606.protein.links.v11.0.txt.gz

DIP: https://dip.doe-mbi.ucla.edu/dip/Download.cgi


##Large-scale studies:

hspn (A census of human soluble protein complexes): Havugimana et al. (2012) https://thebiogrid.org/142063/publication/a-census-of-human-soluble-protein-complexes.html

Metazoan complexes: Wan et al. (2015) http://metazoa.med.utoronto.ca/projected_ppi/Hsapiens_projected_PPI_metazoan_conserved_map.txt

vidal14: Rolland et al. (2014) http://www.interactome-atlas.org/data/HI-II-14.tsv

BioPlex: Huttlin et al. (2015) https://bioplex.hms.harvard.edu/data/BioPlex_interactionList_v4a.tsv

HeinMS: Hein et al. (2015) https://thebiogrid.org/188719/publication/a-human-interactome-in-three-quantitative-dimensions-organized-by-stoichiometries-and-abundances.html

# Modify generate_PPINs.py upon your PPIN list

# Run unify_PPINs.py to generate a UniPPIN 
