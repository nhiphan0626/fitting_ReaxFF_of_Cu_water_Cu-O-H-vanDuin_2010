import numpy as np
import os
import shutil

#Place the source directory in the same directory
source_dirs=['O-head']

#Place the script to generate ffield.RexPoN in the same directory
generate_force_field='generate_ffield.py'

for d1 in [0.0700]: 
  for r1 in  [1.40000]:
    for l1 in  [16.000]:
       for d2 in  [0.0548]:
         for r2 in  [1.4037]:
           for l2 in [16.0562]:
     
            dir_name = f"{d1:.4f}_{r1:.4f}_{l1:.4f}_{d2:.4f}_{r2:.4f}_{l2:.4f}"
            
            os.system('mkdir ' + dir_name)
            
            #Run the external script to generate ffield.RexPoN
            os.system(f'python {generate_force_field} {d1} {r1} {l1} {d2} {r2} {l2}')
                
            shutil.copy('ffield.Reaxff', dir_name)
            
            #Copy source directories (O_head and H_down) to each created directory
            for src_dir in source_dirs:
                dest_dir=os.path.join(dir_name, src_dir)
                
                
                shutil.copytree(src_dir, dest_dir, dirs_exist_ok=True)
                
                #Copy ffield.RexPoN to every subdirectory 
                for root, dirs, _ in os.walk(dest_dir):
                    for sub_dir in dirs:
                        target_dir= os.path.join(root,sub_dir)
                        shutil.copy('ffield.Reaxff',target_dir)
        
print("All directories and files have been processed successfully!")
            
