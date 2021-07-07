#!/usr/bin/python
import numpy as np
import pyvista

## Open the file with read only permit
# read mean, variance, skewness and 
# kurtosis from dakota.out
f = open('../dakota.out', "r")
lines = f.readlines()
S1=[];S2=[];
c=0
#for line in f:
for index, line in enumerate(lines):
	if 'Sobol' in line:
		if 'negligible variance' in line:
			S1.append(0)
			S2.append(0)
		else:
			S1.append(float(lines[index+2].split()[1]))
			S2.append(float(lines[index+3].split()[1]))
			c=c+1
f.close()

print(S1)

outputStats = [S1,S2]
outputStatsName = ['S1', 'S2']
c=0
for iE in outputStats: 
    grid_new = pyvista.PolyData('U_zNormal.vtk')
    grid_new.point_arrays['U'] = iE  
    grid_new.save(outputStatsName[c]+'.vtk', binary=False) 
    c=c+1
