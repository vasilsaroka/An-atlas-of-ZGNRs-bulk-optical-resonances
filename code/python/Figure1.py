# -*- coding: utf-8 -*-
"""
Created on Tue May  7 23:14:22 2019

This python script is used to plot Figure 1 of the manuscript "2N+4-rule and an
atlas of bulk optical resonances of zigzag graphene nanoribbons"

This python script implies the following file structure for the code and data:
'code' directory contains two folders 'Mathematica' and 'python'.
Upon running this python script determines the parent directory for the 'code'
directory. In the parent directory, python implies that there is 'raw data' 
directory that contains 'TB' directory with 'armchair tubes' and 'zigzag ribbons' 
subdirectories with the data files that can be read and plotted to reproduce 
Figure 1 of the manuscript.

Having plotted the data, the script save the figure to the 'test' subfolder  of 
the parent directory.

The parent directory can be successfully determined only if the script is run as 
a file not cell by cell.

@author: Vasil Saroka
"""

import numpy as np
import scipy as sc

import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.gridspec as gridspec
import re
import os

from scipy import interpolate
from datetime import datetime
matplotlib.rcParams.update({'font.size': 18, 'text.usetex': True,
                            'font.family': 'Latin Modern Roman'})

formatter = ticker.ScalarFormatter(useMathText=False)
formatter.set_scientific(True) 
formatter.set_powerlimits((0,1)) 

#%%
def ReadKTPData(path,fname,nrow,ncol):
    """
    This function simple reads the data from the text file and present them in 
    form suitable for the input of pcolor plotting routine
    
    """
    stream=open(path+fname,'r')    
    rdata=list(stream) # this list still contains special characters '\n'
    stream.close()
    # removing '\n' characters from the list elements and splitting at '\t'
    rdata=list(map(lambda x: list(map(float,re.split('\t',re.sub("\n","",x)))),rdata)) 


    dpdata=sc.array(rdata).transpose()
    X=sc.array([[dpdata[0][j*ncol+i] for i in range(ncol)] for j in range(nrow)])
    Y=sc.array([[dpdata[1][j*ncol+i] for i in range(ncol)] for j in range(nrow)])
    Z=sc.array([[dpdata[2][j*ncol+i] for i in range(ncol)] for j in range(nrow)])
    
    return X, Y, Z


#%%  Figure for publication with 4 panels comparing results for tubes and ribbons
# reading file content
    
ncol=2000

parentDir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(parentDir)
path = os.path.join(parentDir, 'raw data/TB/zigzag ribbons/')

fname='Kataura_Plot_ZGNR_Partoens2006_n_20190525_time_21_05_39.txt'
nrow=59
X1, Y1, Z1 = ReadKTPData(path,fname,nrow,ncol)

Z1list=list(Z1)
Z1list.insert(0,list(sc.zeros(ncol)))
Z1=sc.array(Z1list,dtype=float)

fname='Kataura_Plot_ZGNR_19May2019MyFit_n_20190525_time_21_07_03.txt'
X2, Y2, Z2 = ReadKTPData(path,fname,nrow,ncol)
Z2list=list(Z2)
Z2list.insert(0,list(sc.zeros(ncol)))
Z2=sc.array(Z2list,dtype=float)

path = os.path.join(parentDir, 'raw data/TB/armchair tubes/')
fname='Kataura_Plot_ACNT_Partoens2006_n_20190525_time_21_04_09.txt'
nrow=57
X3, Y3, Z3 = ReadKTPData(path,fname,nrow,ncol)
Z3list=list(Z3)
for i in range(3):
    Z3list.insert(0,list(sc.zeros(ncol)))
Z3=sc.array(Z3list,dtype=float)

fname='Kataura_Plot_ACNT_Reich2002_n_20190525_time_21_04_29.txt'
X4, Y4, Z4 = ReadKTPData(path,fname,nrow,ncol)
Z4list=list(Z4)
for i in range(3):
    Z4list.insert(0,list(sc.zeros(ncol)))
Z4=sc.array(Z4list,dtype=float)

#%% 4 density plots comparing results for tubes and ribbons
Z=[Z1, Z2, Z3, Z4]
label=[r'(a)',r'(b)',r'(c)',r'(d)']

xticks=np.linspace(0,60,4)
yticks=np.linspace(0,8,5)

fig = plt.figure(figsize=(9, 8))
gs = gridspec.GridSpec(2, 2, height_ratios=[1, 1], width_ratios=[1, 1])
tfcolor='black'
#'YlOrRd'

for ind, g in enumerate(gs):
    ax = fig.add_subplot(g)
    im = ax.imshow(Z[ind].T[::-1], cmap='RdBu', vmin=abs(Z[ind]).min(), vmax=abs(Z[ind]).max(), aspect=7.5, extent=[0, 60, 0, 8])
    im.set_interpolation('bilinear')
    #p = ax.pcolor(X[ind], Y[ind], Z[ind], cmap=matplotlib.cm.coolwarm, vmin=abs(Z[ind]).min(), vmax=abs(Z[ind]).max())
       
    if ind<2:
        ax.set_xlabel(r'$w$, width index')
    else:
        ax.set_xlabel(r'$n$, diameter index')
    ax.set_ylabel(r'$\hbar \omega$, eV')
    ax.set_xticks(xticks)
    ax.set_yticks(yticks)
    ax.text(55, 7, label[ind],
         {'color': 'white', 'fontsize': 24, 'ha': 'center', 'va': 'center'})
    for spine in ax.spines.values():
        spine.set_edgecolor(tfcolor)
    ax.tick_params(which='major',direction='in', length=6, width=1, colors=tfcolor,labelcolor='black')
    ax.tick_params(which='minor',direction='in', length=3, width=1, colors=tfcolor)
    ax.minorticks_on()
    cb = fig.colorbar(im, ax=ax).ax.tick_params(axis='y', direction='in')

    
fig.tight_layout()
path2savefig=os.path.join(parentDir, 'test/')
datetag=datetime.now().strftime('%Y-%m-%d_%H_%M_%S')
figfname='Fig_1.png'
fig.savefig(path2savefig+figfname,dpi=300,bbox_inches='tight',transparent=False)