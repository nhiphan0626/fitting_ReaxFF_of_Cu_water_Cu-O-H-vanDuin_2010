import os, sys, glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

e_water = []
with open('./H2O_RexPoN/qeq.eng') as f:
	data1 = f.readlines()
	for a, b in enumerate(data1):
		if 'TotEng' in b:
			e_water = float(data1[a+1].split()[1])

df = pd.read_csv('./data_DFT/DFT_data.csv')
dft = np.transpose(df.to_numpy())
#print(dft)

with open('../Cu_RexPoN/Cu_2r3x4/qeq.eng') as f:
	data = f.readlines()
	for a, b in enumerate(data):
		if 'TotEng' in b:
			e_Cu = float(data[a+1].split()[1])

directory = glob.glob('*.*_*.*_*.*')
#energy = []
#with open('Cu_total_energy_RexPoN_data') as f:
#	for i in f.readlines():
#		directory.append(i.split()[0])
#		energy.append(float(i.split()[1]))

results = []
for d in directory:
	for j in ['O_head']:
		filelist = os.listdir(d + '/' + j + '/' + 'O_head_7.0')
		#print(filelist)
		with open(d + '/' + j + '/' + 'O_head_7.0' + '/' + 'qeq.eng') as f:
			data = f.readlines()
		for a, b in enumerate(data):
			if 'TotEng' in b:
				e_shift_RexPoN = (float(data[a+1].split()[1]) - e_Cu - e_water)
				#print(e_shift_RexPoN)

	for j in ['O_head']:
		filelist = os.listdir(d + '/' + j)
		#print(filelist)
		for k in filelist:
			if not j in k:
				continue
			else:
				with open(d + '/' + j + '/' + k + '/qeq.eng') as f:
					data = f.readlines()
				for n, i in enumerate(data):
					if 'TotEng' in i:
						TotEng = float(data[n+1].split()[1])
						PotEng = float(data[n+1].split()[2])
						KinEng = float(data[n+1].split()[3])
						E_coul = float(data[n+1].split()[4])
						E_bond = float(data[n+1].split()[5])
						E_angle = float(data[n+1].split()[6])
						E_vdwl  = float(data[n+1].split()[7])
						path   = str(d + '/' + j + '/' + k)
						distance = float(path.split('_')[-1])
						results.append([distance, TotEng, PotEng, KinEng, E_coul, E_bond, E_angle, E_vdwl])
							#print(results)
results_df = pd.DataFrame(results, columns = ['distance', 'TotEng', 'PotEng', 'KinEng','E_coul', 'E_bond', 'E_angle', 'E_vdwl'])
results_df.to_csv('eng.csv',index = False)
print("Results was written to 'eng.csv'.")

file_path='./eng.csv'
data = pd.read_csv(file_path)

plt.figure(figsize=(6.5,5))


plt.scatter(data['distance'], data['TotEng'], label = 'TotEng', color = 'grey', marker = 'o')
plt.scatter(data['distance'], data['PotEng'], label = 'PotEng', color = 'red', marker = 'o')
plt.scatter(data['distance'], data['KinEng'], label = 'KinEng', color = 'blue', marker = 'o')
plt.scatter(data['distance'], data['E_coul'], label = 'E_coul', color = 'green', marker = 'o')
plt.scatter(data['distance'], data['E_bond'], label = 'E_bond', color = 'orange', marker = 'o')
plt.scatter(data['distance'], data['E_angle'], label = 'E_angle', color = 'purple', marker = 'o')
plt.scatter(data['distance'], data['E_vdwl'], label = 'E_vdwl', color = 'black', marker = 'o')


plt.xlim(1,8)
plt.ylim(-6000,1000)
plt.xlabel('Distance (angstrom)', fontsize = 14)
plt.ylabel('Energy (kcal/mol)', fontsize = 14)
plt.xticks(fontsize = 14)
plt.yticks(fontsize = 14)
plt.legend(fontsize = 14)
plt.tight_layout()

plt.show()


