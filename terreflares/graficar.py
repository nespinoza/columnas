# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from astropy.time import Time
import pandas as pd 
import numpy as np
import utilidades

# Extraemos los tiempos de cada terremoto con magnitud > 5,
# ademas de los indices y fechas en los cuales hay terremotos mayores a 
# magnitud 8 (el ultimo es Chile - 27F):
tt,mag,tmin,tmax,idx_8,fechas_8 = utilidades.leer_terremotos('datos/terremotos.csv')
# Extraemos numero de manchas solares por mes:
tm,m = utilidades.leer_manchas('datos/manchas.dat')

# Graficamos. Algunas definiciones primero:
from matplotlib import rcParams
fac_text = 1.2
rcParams["font.size"] = 8*fac_text#17
rcParams["legend.fontsize"] = 6*fac_text#13
rcParams["font.family"] = "sans-serif"
rcParams["font.sans-serif"] = ["Computer Modern Sans"]
rcParams["text.usetex"] = True
rcParams["text.latex.preamble"] = r"\usepackage{cmbright}"
rcParams['axes.linewidth'] = 1.2 #set the value globally
rcParams['xtick.direction'] = 'out'
rcParams['ytick.direction'] = 'out'

plt.figure(figsize=(20, 5))
fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

# Grafico de los terremotos:
ax1.plot(tt, mag,color='steelblue')
# Marcamos el de Chile (29F):
diff_t = np.abs(2010.2-tt[idx_8])
iidx = np.where(diff_t==np.min(diff_t))[0]
ax1.plot(tt[idx_8][iidx],mag[idx_8][iidx],'o',color='white',markeredgecolor='black',markersize=10)

# Misma cosa, manchas solares:
ax2.plot(tm,m, 'b-',color='orangered')

# Graficamos los anios para mejor visualizacion de fechas:
#fechas = []
#anios = range(1985,2015,5)
#for anio in anios:
#    fechas.append(str(anio)+'-01-01T00:00:00')
#print fechas
#tanios = Time(fechas, format='isot', scale='utc').jd
#for i in range(len(tanios)):
#    ax1.plot([tanios[i],tanios[i]],[5,9.5],'--',color='black')
#    ax1.text(tanios[i]-900,9.0,str(anios[i]))

# Seteamos los ejes:
ax1.set_xlabel(r'Tiempo (a\~nos)')
ax1.set_ylabel('Magnitud de terremotos', color='steelblue')
ax2.set_ylabel('Numero de manchas solares', color='orangered')
ax1.set_ylim(5.,9.2)
#ax2.set_ylim(0)
plt.xlim([np.min(tt),np.max(tt)])
plt.savefig("terremotos_vs_manchas.png", bbox_inches="tight") 
#plt.show()
