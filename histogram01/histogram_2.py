import numpy as np
#open the datafile
#data = open('/home/flgomez10/lum-mass/data/MD_3840_Planck1/BDM/test.dat',"r")
data = open('/home/flgomez10/lum-mass/data/MD_3840_Planck1/BDM/reduced_catshortV_007.dat',"r")

#bin range & counter
mass_hist = np.zeros(50)
mass_bin = np.zeros(50)
mass_bin[0] = 1.5e+10
for i in range (1,50):
    mass_bin[i] = mass_bin[i-1]*np.math.pow(500,0.02)

#read and ignore header lines
data.seek(0)
for i in range(0,17):
    data.readline()
    
for line in data:
    line = line.strip()
    columns = line.split()
    mass = float(columns[3])
    i = 0
    while mass > mass_bin[i]:
        i += 1
    mass_hist[i-1] += 1
#    print mass_bin[i], mass, mass_bin[i+1], mass_hist[i], i
data.close()    


#number of haloes in the file
N = 10937974-17

datos = open("datos.dat", "w")
datos.write("mass\tdensity\n")
for i in xrange(0,50):
    datos.write(str(mass_bin[i])+"\t"+str(mass_hist[i])+"\n")
datos.close()
