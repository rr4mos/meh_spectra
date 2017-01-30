# meh_spectra
working on optical spectra ensemble - based on orca CI-zindo 

1) clean.sh (typical, dependent on output name) on working directory (one .out file / chain --> one directory / file (chain)
2) call_spec.sh  (pack="<local directory>") --> bash call_spec.sh

-- calling :  
    1) generating spectra and orbital analysis
              getTrans.py  --> TransLabels.in & 
              list_orbs.py  --> TRANS.txt
              sum_spec_broadening.py --> spec data
              gnuplot :: generates >> Spec.png
              
              
DEV: 

cleaning scripts (style/structures)
orbital contribution to a Log (similar to TRANS.txt improving simplicity)
orbital localization analysis  (based on RREEtools) >> confronting with CUBE data (already calculated)
