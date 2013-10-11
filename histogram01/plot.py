# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

import numpy as np
import matplotlib.pyplot as plt

data = open("datos.dat", "r")
data.readline()
mass_hist = np.zeros(50)
mass_bin = np.zeros(50)

i=0
for line in data:
    line = line.strip()
    columns = line.split()
    mass = float(columns[0])
    hist = float(columns[1])
    mass_hist[i]=hist
    mass_bin[i]=mass
    i +=1

# <codecell>

mass_hist += 1
#box volume: 1000x1000x1000 Mpc³ h⁻³
mass_hist /= 1e9
#mass_hist /= (10937974-13)

print mass_bin, mass_hist

# <codecell>

plt.loglog( mass_bin, mass_hist )
plt.title("Mass Density Function")
plt.xlabel(r"$\log_{10} M_\odot$")
plt.ylabel(r"$\log \frac{dM}{dN}\left( Mpc^3 h^{-1} \right)$")
plt.show()

# <codecell>


# <codecell>


