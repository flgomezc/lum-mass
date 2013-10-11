# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(
                  '/home/flgomez10/lum-mass/data/MD_3840_Planck1/BDM/reduced_catshortV_007.dat',
                  usecols=(0,1,2,3), skiprows=17)

M_halos_list = np.zeros(data.shape[0])
M_max = 10.5
M_min = 11.5

for i in xrange(0, data.shape[0]):
#    b[i] = np.log10( data[i,3])
    M_halos_list[i] = np.log10(data[i,3])
    if M_halos_list[i] > M_max:
        M_max = M_halos_list[i]
    if M_halos_list[i] < M_min:
        M_min = M_halos_list[i]
      

# <codecell>

print M_min, M_max

# <codecell>

BINS = 20
log_part_array = np.linspace( M_min, M_max, BINS )
N_halos = np.zeros(BINS)
print log_part_array
print N_halos

# <codecell>

for i in range( BINS-1 ):
    index = np.where((log_part_array[i] <= M_halos_list)&
                     (log_part_array[i+1] > M_halos_list))
#    print index[0].size
    N_halos[i] = index[0].size
print N_halos

# <codecell>

import matplotlib.pyplot as plt
plt.plot( log_part_array, N_halos)
plt.show()

