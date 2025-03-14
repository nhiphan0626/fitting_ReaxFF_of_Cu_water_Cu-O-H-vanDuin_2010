import os, sys, glob

files = glob.glob('O_head' + '/' + 'O_head_*')

for file in files:
	print(file)
	os.system('cp lammps.in %s'%file)
