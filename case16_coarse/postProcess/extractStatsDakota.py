#!/usr/bin/python
import numpy as np
import pyvista

## Open the file with read only permit
# read mean, variance, skewness and 
# kurtosis from dakota.out
f = open('../dakota.out', "r")
Umean=[];Uvar=[];Uskew=[];Ukurt=[];
c=0
for line in f:
	if line.startswith("  integration:"):
			Umean.append(float(line.split()[1]))
			Uvar.append(float(line.split()[2]))
			Uskew.append(float(line.split()[3]))
			Ukurt.append(float(line.split()[4]))
f.close()
#print(len(Umean))

outputStats = [Umean, Uvar, Uskew, Ukurt]
outputStatsName = ['Umean', 'Uvar', 'Uskew', 'Ukurt']
c=0
for iE in outputStats: 
    grid_new = pyvista.PolyData('../workdir.1/postProcessing/surfaces/3000/U_zNormal.vtk')
    grid_new.point_arrays['U'] = iE  
    grid_new.save(outputStatsName[c]+'.vtk', binary=False) 
    c=c+1
