import numpy as np 
import math

f = open('postProcessing/probes/0/U', "r")

c=0
for line in f:
    if line.startswith("3000"):
        data=line.strip()
data = data.replace('(','')
data = data.replace(')','')
data = np.fromstring(data, dtype=float, sep=' ')

f.close()

UVW = data[1:]
U = []
V = []
W = []
Umag = []
Udir = []
for i in range(0,int(len(data)/3)):
    U.append(float(UVW[3*i]))
    V.append(float(UVW[1+3*i]))
    W.append(float(UVW[2+3*i]))
for i in range(0,int(len(U))):
    Umag.append((np.power(np.power(U[i],2)+np.power(V[i],2),0.5))) 
    Udir.append(np.degrees(math.atan2(V[i],U[i])))
    Udir_list=list(Udir)

UmagUdir = np.zeros(len(Umag)*2)
j=0
for i in range(0, len(Umag)*2, 2):
    UmagUdir[i] = Umag[j]
    UmagUdir[i+1] = Udir[j]
    j=j+1

#UmagUdir = np.concatenate(([Umag, Udir]), axis=0)
#UmagUdir = Umag
np.savetxt('output_Utheta.txt',UmagUdir,fmt="%.10f") 
