DOI="10.5281/zenodo.166034"
user_information = """
POPC slipids from F. Favela
#NMRLIPIDS BEGIN

@SIM
@SYSTEM=POPC_T298K
@MAPPING=POPC,mappingPOPCslipids.txt
@SOFTWARE=gromacs
@FF=Slipids
@FF_SOURCE=??
@FF_DATE=??
@TRJ=popc00_T298_every100ps.xtc
@TPR=popc00_T298_every100ps.tpr
@PREEQTIME=0
@TIMELEFTOUT=70

@POPC=POPC
@POPG=POPG
@POPS=POPS
@POPE=POPE

@POT=K
@SOD=NA
@CLA=CL
@CAL=CA
@SOL=SOL

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
