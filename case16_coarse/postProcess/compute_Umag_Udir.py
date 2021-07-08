import pyvista
import numpy as np 
import math

#Saving Umag to txt

grid = pyvista.PolyData('../../workdir.1/postProcessing/surfaces/3000/U_zNormal.vtk')
values=grid.point_arrays['U']
val=np.asarray(values)

Umag=[]
Udir=[]
for vv in values:
    Umag.append(np.power(np.power(vv[0],2)+np.power(vv[1],2),0.5))
    Udir.append(np.degrees(math.atan2(vv[1],vv[0])))

#UmagUdir = np.zeros(len(Umag)*2)
#j=0
#for i in range(0, len(Umag)*2, 2):
#    UmagUdir[i] = Umag[j]
#    UmagUdir[i+1] = Udir[j]
#    j=j+1
UmagUdir = Umag
np.savetxt('output_Utheta.txt',UmagUdir,fmt="%.10f") 

#np.savetxt('output_Utheta.txt',UmagUdir,fmt="%.10f") 
