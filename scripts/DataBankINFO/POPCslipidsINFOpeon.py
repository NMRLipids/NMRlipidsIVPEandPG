DOI="10.5281/zenodo.3235552"
user_information = """
POPC slipids from A. Peon
#NMRLIPIDS BEGIN

@SIM
@SYSTEM=POPC_T310K
@MAPPING=POPC,mappingPOPCslipids.txt
@SOFTWARE=gromacs
@FF=Slipids
@FF_SOURCE=??
@FF_DATE=??
@TRJ=total_4_500.xtc
@TPR=md_0.tpr
@PREEQTIME=400
@TIMELEFTOUT=0

@POPC=POPC
@POPG=POPG
@POPS=POPS
@POPE=POPE

@POT=K
@SOD=NA
@CLA=CL
@CAL=CA
@SOL=TIP3p

@NPOPC=[0,0]
@NPOPG=[0,0]
@NPOPS=[0,0]
@NPOPE=[0,0]

@NPOT=0
@NSOD=0
@NCLA=0
@NCAL=0
@NSOL=0

@TEMPERATURE=0
@TRJLENGTH=0

#NMRLIPIDS END

"""
dir_wrk = "/media/osollila/Data/tmp/DATABANK/"
