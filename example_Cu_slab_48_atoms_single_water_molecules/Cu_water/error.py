import os, sys, glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('./data_DFT/DFT_data.csv')
dft = np.transpose(df.to_numpy())
#print(dft)
directory = glob.glob('*.*_*.*_*.*_*_*_*')

results = []
for d in directory:
	for j in ['O-head']:
		filelist = os.listdir(d + '/' + j)
		print(filelist)
		for k in filelist:
			if not j in k:
				continue
			else:
				with open(d + '/' + j + '/' + k + '/qeq.eng') as f:
					data = f.readlines()
				for n, i in enumerate(data):
					if 'TotEng' in i:
						e_bind_reaxff = (float(data[n+1].split()[1]) - (-3535.4738)- (-252.497))
						index = np.where(dft[0] == k)[0]
						if len(index) > 0:	
							e_bind_dft = dft[2][index[0]]
						 		
							error_ = (float(abs(e_bind_dft - e_bind_reaxff)))		
							results.append([d + '/' + j + '/' + k, e_bind_dft, e_bind_reaxff, error_])
							#print(results)
results_df = pd.DataFrame(results, columns = ['path','e_bind_dft', 'e_bind_reaxff', 'abs_error'])
results_df.to_csv('results.csv',index = False)
print("Results was written to 'results.csv'.")
				#print(k.split('_')[-1])
df = pd.read_csv('results.csv')

df['ffield_params'] = df['path'].apply(lambda x: x.split('/')[0])

mae_error = df.groupby('ffield_params')['abs_error'].mean().reset_index()

with open('mae_error', 'w') as f:
	f.write(mae_error.to_string(index = False))
min_mae_error = mae_error.loc[mae_error['abs_error'].idxmin()]
with open('min_error', 'w') as f:
	f.write(f"The minimum mae error from ffield(De, Re, L): {min_mae_error['ffield_params']}' with and the value error of {min_mae_error['abs_error']} + '\n'")
get1 = df[df['ffield_params'] == min_mae_error['ffield_params']].reset_index()
print(get1)
data1 = get1.drop(get1.columns[[0, -1]], axis = 1)
print(data1)
data1['distance'] = data1['path'].apply(lambda x: float(x.split('-')[-1]))
data1_O_head = data1[data1['path'].str.contains('O-head')].sort_values(by = 'distance')
plt.figure(figsize=(6.5,5))

plt.plot(data1_O_head['distance'], data1_O_head['e_bind_dft'], label = 'PBE', color = 'grey', marker = 'o')
plt.plot(data1_O_head['distance'], data1_O_head['e_bind_reaxff'], label = 'ReaxFF_Cu/O/H_2010', color = 'red', marker = 'o')

plt.xlim(1,8)
plt.ylim(-5,50)
plt.xlabel('Distance', fontsize = 16)
plt.ylabel('E_bind (kcal/mol)', fontsize = 16)
plt.xticks(fontsize = 16)
plt.yticks(fontsize = 16)
plt.legend(fontsize = 16)
plt.grid(alpha = 0.3)
plt.tight_layout()
plt.show()

