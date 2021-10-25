# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 10:43:59 2021

@author: anugi
"""


import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
#from iminuit import Minuit

my_frame = pd.read_csv('samples/acceptance_mc.csv')

print(my_frame)
#%%
data_path = 'samples/'
files = [f'{data_path}toy_data_bin_{i}.pkl' for i in range(7)]
bins = [pd.read_pickle(file) for file in files]

bins[0].head()
#%%
acc = np.loadtxt('samples/acceptance_mc.csv', skiprows =1 )
#%%
######### IMPORT PACKAGES IN THIS CELL SO THAT i DON'T HAVE TO RUN PREVIOUS CELLS ########
import csv
import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

#load k_pi_swap
table = pd.read_csv('C:\My Documents\Physics\Year 3\Comprehensives\samples\k_pi_swap.csv')
col_no = len(table.columns) # Number of columns
print(table.columns)
#%%

column = 'K_MC15TuneV1_ProbNNp'# Here, you can insert whatever column you want!
plt.hist(table[column],bins=50)
plt.grid()
plt.xlabel("PT (MeV)")
plt.ylabel("Frequency")
plt.title(column)
plt.axvline(table[column].mean(), color='k', linestyle='dashed', linewidth=1)
print(table[column].mean())
plt.show()
#%%
column = 'Kstar_MM'# Here, you can insert whatever column you want!
k_star = (table[column])
column = 'J_psi_MM'
jpsi = (table[column])

kandjpsi= k_star + jpsi
plt.hist(kandjpsi,bins=500, label="Jpsi + K")
plt.legend()
plt.show()
#%%
column = 'B0_MM'
b0 = (table[column])
plt.hist(b0,bins=500, label="B0")
plt.legend()
plt.show()

plt.hist(kandjpsi,bins=500, label="JPsi")
plt.hist(b0,bins=500, label="JPsi")
plt.legend()
plt.show()

