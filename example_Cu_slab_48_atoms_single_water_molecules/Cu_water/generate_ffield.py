#!/usr/bin/env python
# coding: utf-8

# In[7]:


from math import sqrt 
import sys

# Atoms should be provided with the same order as in the ffied.RexPoN
# The parameters are: De, Re, and L
# Use Table II of "J. Chem. Phys. 151, 154111 (2019); doi: 10.1063/1.5113811" for the above parameters
# If not available use UFF values 

#Check if the required arguments are provided
if len(sys.argv) != 7:
    print("Usage: python generate_vdw.py <De1> <Re1> <L1> <De2> <Re2> <L2>")
    sys.exit(1)

#Parse the input arguments
De1=float(sys.argv[1])
Re1=float(sys.argv[2])
L1=float(sys.argv[3])
De2=float(sys.argv[4])
Re2=float(sys.argv[5])
L2=float(sys.argv[6])


file_name= "ffield.Reaxff"

#General parameters
general_params="""\
ReaxFF reactive force field. Cu/O/H: van Duin et al., JPCA 2010; Cu/C, Cu/H, Cu/N: Hu et al., 2017;
 39       ! Number of general parameters                                        
   50.0000 !Overcoordination parameter                                          
    9.5469 !Overcoordination parameter                                          
    1.6725 !Valency angle conjugation parameter                                 
    1.7224 !Triple bond stabilisation parameter                                 
    6.8702 !Triple bond stabilisation parameter                                 
   60.4850 !C2-correction                                                       
    1.0588 !Undercoordination parameter                                         
    4.6000 !Triple bond stabilisation parameter                                 
   12.1176 !Undercoordination parameter                                         
   13.3056 !Undercoordination parameter                                         
  -70.5044 !Triple bond stabilization energy                                    
    0.0000 !Lower Taper-radius                                                  
   10.0000 !Upper Taper-radius                                                  
    2.8793 !Not used                                                            
   33.8667 !Valency undercoordination                                           
    6.0891 !Valency angle/lone pair parameter                                   
    1.0563 !Valency angle                                                       
    2.0384 !Valency angle parameter                                             
    6.1431 !Not used                                                            
    6.9290 !Double bond/angle parameter                                         
    0.3989 !Double bond/angle parameter: overcoord                              
    3.9954 !Double bond/angle parameter: overcoord                              
   -2.4837 !Not used                                                            
    5.7796 !Torsion/BO parameter                                                
   10.0000 !Torsion overcoordination                                            
    1.9487 !Torsion overcoordination                                            
   -1.2327 !Conjugation 0 (not used)                                            
    2.1645 !Conjugation                                                         
    1.5591 !vdWaals shielding                                                   
    0.1000 !Cutoff for bond order (*100)                                        
    1.7602 !Valency angle conjugation parameter                                 
    0.6991 !Overcoordination parameter                                          
   50.0000 !Overcoordination parameter                                          
    1.8512 !Valency/lone pair parameter                                         
    0.5000 !Not used                                                            
   20.0000 !Not used                                                            
    5.0000 !Molecular energy (not used)                                         
    0.0000 !Molecular energy (not used)                                         
    0.7903 !Valency angle conjugation parameter                                 
  3    ! Nr of atoms; cov.r; valency;a.m;Rvdw;Evdw;gammaEEM;cov.r2;#            
            alfa;gammavdW;valency;Eunder;Eover;chiEEM;etaEEM;n.u.               
            cov r3;Elp;Heat inc.;n.u.;n.u.;n.u.;n.u.                            
            ov/un;val1;n.u.;val3,vval4                                          
 H    0.8930   1.0000   1.0080   1.3550   0.0930   0.8203  -0.1000   1.0000     
      8.2230  33.2894   1.0000   0.0000 121.1250   3.7248   9.6093   1.0000     
     -0.1000   0.0000  55.6606   3.0408   2.4197   0.0003   1.0698   0.0000     
    -19.4571   4.2733   1.0338   1.0000   2.8793   0.0000   0.0000   0.0000     
 O    1.2450   2.0000  15.9990   2.3890   0.1000   1.0898   1.0548   6.0000     
      9.7300  13.8449   4.0000  37.5000 116.0768   8.5000   8.3122   2.0000     
      0.9049   0.4056  63.0626   3.5027   0.7640   0.0021   0.9745   0.0000     
     -3.5500   2.9000   1.0493   4.0000   2.9225   0.0000   0.0000   0.0000     
 Cu   1.9202   2.0000  63.5460   1.9221   0.2826   1.0000   0.1000   1.0000     
     10.9889 100.0000   1.0000   0.0000   0.0000   2.7875   6.0000   0.0000     
     -1.0000   0.0000  80.7000  34.9555   0.4988   0.0000   0.8563   0.0000     
     -5.1872   3.1491   1.0000   4.0000   2.5791   0.0000   0.0000   0.0000     
 6      ! Nr of bonds; Edis1;LPpen;n.u.;pbe1;pbo5;13corr;pbo6                  
                         pbe2;pbo3;pbo4;Etrip;pbo1;pbo2;ovcorr                  
  1  1 153.3934   0.0000   0.0000  -0.4600   0.0000   1.0000   6.0000   0.7300  
         6.2500   1.0000   0.0000   1.0000  -0.0790   6.0552   0.0000   0.0000  
  2  2 142.2858 145.0000  50.8293   0.2506  -0.1000   1.0000  29.7503   0.6051  
         0.3451  -0.1055   9.0000   1.0000  -0.1225   5.5000   1.0000   0.0000  
  1  2 160.0000   0.0000   0.0000  -0.5725   0.0000   1.0000   6.0000   0.5626  
         1.1150   1.0000   0.0000   0.0000  -0.0920   4.2790   0.0000   0.0000  
  1  3   0.0000   0.0000   0.0000   0.2000  -0.1418   1.0000  13.1260   0.5000  
         0.5000  -0.2000  20.0000   1.0000  -0.1000   9.0000   0.0000   0.0000  
  2  3  81.4346   0.0000   0.0000  -0.1594  -0.3000   1.0000  36.0000   0.0025  
         0.2904  -0.2500  12.0000   1.0000  -0.0742   9.3638   0.0000   0.0000  
  3  3  73.6263   0.0000   0.0000   0.0209  -0.2000   0.0000  16.0000   0.3414  
         0.4703  -0.2000  15.0000   1.0000  -0.1319   5.9254   0.0000   0.0000  
  3    ! Nr of off-diagonal terms; Ediss;Ro;gamma;rsigma;rpi;rpi2               
  1  2   0.0283   1.2885  10.9190   0.9215  -1.0000  -1.0000                    
"""

with open(file_name,"w") as f:
    f.write(general_params)



# print the vdW section of the RexPoN ffield

Cu_H= ("%i %i %0.5f %0.5f %0.5f  %0.5f %0.5f %0.5f "%(1, 3, De1, Re1, L1, 0.1000,  -1.0000,  -1.0000))
Cu_O= ("%i %i %0.5f %0.5f %0.5f  %0.5f %0.5f %0.5f "%(2, 3, De2, Re2, L2, 1.7228,  -1.0000,  -1.0000  ))

with open(file_name,"a") as f:
    f.write(Cu_H + "\n")

with open(file_name,"a") as f:
    f.write(Cu_O + "\n")

next_params="""\
 12    ! Nr of angles;at1;at2;at3;Thetao,o;ka;kb;pv1;pv2                        
  1  1  1   0.0000  27.9213   5.8635   0.0000   0.0000   0.0000   1.0400        
  2  2  2  80.7324  30.4554   0.9953   0.0000   3.0000  50.0000   1.0783        
  1  2  2  75.6935  50.0000   2.0000   0.0000   1.0000   0.0000   1.1680        
  1  2  1  85.8000   9.8453   2.2720   0.0000   2.8635   0.0000   1.5800        
  2  1  2   0.0000  15.0000   2.8900   0.0000   0.0000   0.0000   2.8774        
  1  1  2   0.0000   8.5744   3.0000   0.0000   0.0000   0.0000   1.0421        
  2  3  2  96.2265   4.5610  12.0000   0.0000   0.3211   0.0000   1.5204        
  2  3  2   0.0000   9.1552   7.9919   0.0000   0.1660   0.0000   1.5386        
  3  2  3 100.0000  10.1065   6.0000   0.0000   1.0000   0.0000   3.6601        
  1  2  3  55.0417   3.5032   3.9979   0.0000   1.5171   0.0000   1.0400        
  2  2  3  70.0000  30.0000   2.0000   0.0000   1.0000   0.0000   1.2500        
  2  3  3  66.7783  14.3146   0.7911   0.0000   1.0000   0.0000   1.2333        
  6    ! Nr of torsions;at1;at2;at3;at4;;V1;V2;V3;V2(BO);vconj;n.u;n            
  1  2  2  2   0.8302  -4.0000  -0.7763  -2.5000  -1.0000   0.0000   0.0000     
  2  2  2  2  -2.5000  -4.0000   1.0000  -2.5000  -1.0000   0.0000   0.0000     
  0  1  1  0   0.0000   0.0000   0.0000   0.0000   0.0000   0.0000   0.0000     
  0  1  2  0   0.0000   0.1000   0.0200  -2.5415   0.0000   0.0000   0.0000     
  0  2  2  0   0.5511  25.4150   1.1330  -5.1903  -1.0000   0.0000   0.0000     
  1  2  3  2  -1.5000   6.8333  -0.1978  -1.4683   0.0000   0.0000   0.0000     
  1    ! Nr of hydrogen bonds;at1;at2;at3;Rhb;Dehb;vhb1                         
  2  1  2   2.1200  -3.5800   1.4500  19.5000                           
"""

with open(file_name,"a") as f:
      f.write(next_params)
