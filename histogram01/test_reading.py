# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

data = open('/home/flgomez10/lum-mass/data/MD_3840_Planck1/BDM/reduced_catshortV_007.dat',"r")
#print data

# <codecell>

data.readline(1)

# <codecell>

data = open('/home/flgomez10/lum-mass/data/MD_3840_Planck1/BDM/test.dat',"r")
print data

# <codecell>

#data.read()

# <codecell>

data.seek(0)
data.readline(800)

# <codecell>

data.seek(0)

for line in data:
    print line

# <codecell>

print line

# <codecell>

line

# <codecell>

line.strip()

# <codecell>

columns = line.split()

# <codecell>

columns

# <codecell>

mass = float(columns[3])
mass

# <codecell>

#open the datafile
#data = open('/home/flgomez10/lum-mass/data/MD_3840_Planck1/BDM/test.dat',"r")
#read and ignore header lines
data.seek(0)
for i in range(0,17):
    data.readline()
    
mass_min = 5e+10
mass_max = 5e+10
    
for line in data:
    line = line.strip()
    columns = line.split()
    mass = float(columns[3])
    print mass
    if( mass_min > mass):
        mass_min = mass
    if( mass_max < mass):
        mass_max = mass
            
print "Lower mass limit = ", mass_min, ", Upper mass limit = ", mass_max

# <codecell>


