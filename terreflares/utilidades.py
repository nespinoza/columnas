import numpy as np
import datetime
from datetime import datetime as dt
import time

# Codigo para convertir fracciones de anio: 
# https://stackoverflow.com/questions/6451655/python-how-to-convert-datetime-dates-to-decimal-years
def toYearFraction(date):
    def sinceEpoch(date): # returns seconds since epoch
        return time.mktime(date.timetuple())
    s = sinceEpoch

    year = date.year
    startOfThisYear = dt(year=year, month=1, day=1)
    startOfNextYear = dt(year=year+1, month=1, day=1)

    yearElapsed = s(date) - s(startOfThisYear)
    yearDuration = s(startOfNextYear) - s(startOfThisYear)
    fraction = yearElapsed/yearDuration

    return date.year + fraction

def leer_manchas(narchivo):
    fin = open(narchivo,'r')
    fechas = []
    manchas = []
    while True:
        linea = fin.readline()
        if linea != '':
          if linea[0] != '#':
            vector = linea.split()
            ano = vector[0]
            mancha = vector[1:]
            for i in range(12):
                fechas.append(toYearFraction(datetime.datetime(int(ano),int(i+1),15,0,0,0)))
                manchas.append(np.double(mancha[i]))
        else:
            break
    # Convertimos fechas a fracciones de anio:
    #t = Time(fechas, format='isot', scale='utc')
    return np.array(fechas),np.array(manchas)

def leer_terremotos(narchivo):
    fin = open(narchivo,'r')
    fechas = []
    magnitudes = []
    while True:
        linea = fin.readline()
        if linea != '':
          if linea[0] != '#':
            vector = linea.split(',')
            fecha,magnitud = vector[0],np.double(vector[4])
            fecha = fecha[:-1]
            yymmdd,hhmmss = fecha.split('T')
            yy,mo,dd = yymmdd.split('-')
            hh,mm,ss = hhmmss.split(':')
            ss = ss.split('.')[0]
            fechas.append(toYearFraction(datetime.datetime(int(yy),int(mo),int(dd),int(hh),int(mm),int(ss))))
            magnitudes.append(np.double(magnitud))
        else:
            break
    t = np.array(fechas)
    idx_min = np.where(t==np.min(t))[0]
    idx_max = np.where(t==np.max(t))[0]
    magnitudes = np.array(magnitudes)
    idx_8 = np.where(magnitudes>8.0)[0]
    return t,magnitudes,fechas[idx_min[0]],fechas[idx_max[0]],idx_8,np.array(fechas)[idx_8]
