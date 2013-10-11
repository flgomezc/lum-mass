# -*- coding: utf-8 -*-
# <nbformat>2</nbformat>

# <codecell>

import numpy as np
import matplotlib.pyplot as plt
BINS = 11
#############################################
#                                           #
#            Loading data file              #
#                                           #
#############################################
data = np.loadtxt(
                  '/home/flgomez10/lum-mass/data/MD_3840_Planck1/BDM/test.dat',
                  #'/home/flgomez10/lum-mass/data/MD_3840_Planck1/BDM/reduced_catshortV_007.dat',
              # Reduce the memory usage from 'float64'(default) to 'float32'
                  'float32',
                  usecols=(0,1,2,3), skiprows=17)
# To create a little test catalog
# use the command "head" in terminal to append 
# just a few lines from the original catalog
# $ head -n10000 file.txt >> newfile.txt

#print data

# <codecell>

#############################################
#                                           #
#            Halo Mass Function             #
#                                           #
#############################################
M_halos_list = np.log10(data[:,3])
M_min = np.amin(M_halos_list)
M_max = np.amax(M_halos_list)

bins_mass = np.linspace( M_min, M_max, BINS )
N_halos = np.zeros(BINS)

for i in range( BINS-1 ):
    index = np.where((bins_mass[i]  <= M_halos_list)&
                     (bins_mass[i+1] > M_halos_list))
    N_halos[i] = index[0].size
    
M_BIN_width = (M_max - M_min)/BINS
CELL_volume = 1e+9
N_halos_norm = N_halos / ( CELL_volume * M_BIN_width)    

# <codecell>

# Plotting Mass Density Function

plt.semilogy(bins_mass, N_halos_norm)
plt.title("Mass Density Function")
plt.xlabel(r"$\log_{10} M_\odot$")
plt.ylabel(r"$\log \frac{dM}{dN}\left( Mpc^3 h^{-1} \right)$")

plt.show()

# <codecell>

#############################################
#                                           #
#           Luminosity Function             #
#                                           #
#############################################
alpha = 1.0
beta  = 1.0
# $L = \alpha * Halo_Mass ^ { \beta}$
# Luminosity units: Sun Luminosity = $L_{\odot}$
Log_Luminosity_halo_list = np.log10(alpha) + beta*M_halos_list 

# $ Mag_{UV} = 5.61 - 2.5 * \log ( L / L_\odot )
Magnitude_UV_galaxy_list = 5.61 - 2.5 *  Log_Luminosity_halo_list[:] 

Magnitude_min = np.amin(Magnitude_UV_galaxy_list)
Magnitude_max = np.amax(Magnitude_UV_galaxy_list)
Magnitude_BIN_width = (Magnitude_max - Magnitude_min)/BINS

bins_mag = np.linspace( Magnitude_min, Magnitude_max, BINS )
N_Magnitude = np.zeros(BINS)

for i in range( BINS-1 ):
    index = np.where((bins_mag[i]  <= Magnitude_UV_galaxy_list)&
                     (bins_mag[i+1] > Magnitude_UV_galaxy_list))
    N_Magnitude[i] = index[0].size

N_Magnitude_norm = N_Magnitude / ( CELL_volume * Magnitude_BIN_width )

# <codecell>

# Plotting Luminosity Function

plt.semilogy(bins_mag,N_Magnitude_norm)
plt.title("Luminosity Function")
plt.xlabel("Magnitude")
plt.ylabel(r"$\log \frac{dL}{dMag} $")

plt.show()

# <codecell>

#############################################
#                                           #
#              Cosmic Variance              #
#                                           #
#############################################
alpha=1.0
beta =1.0

csmc_cat = np.insert( data,4, 
                     #Magnitude as function of the halo mass
                     5.61 - 2.5*np.log10( alpha*(data[:,3])**beta )
                     ,axis=1)
csmc_cat[:,3] = np.log10( csmc_cat[:,3] )
# csmc_var columns:
#  X , Y , Z , \log_10 Halo_Mass , Magnitude_UV
#print csmc_cat

# <codecell>

# This part takes the HMF and LF for each one of
# the 64 parts of the whole cell

# Volume of local cell = 250*250*250 Mpc^{3} h^{-1}
Length = 250
LocalCellVolume = Length **3
cosmic_variance = np.zeros((64, BINS,2))
counter = 0

for i in range(4):
    for j in range(4):
        for k in range(4):   
            for l in range(BINS-1):
                #HMF
                index = np.where(
                                 #spatial condition
                                 (Length*i        <= csmc_cat[:,0])&
                                 (Length*(i+1)     > csmc_cat[:,0])&
                                 (Length*j        <= csmc_cat[:,1])&
                                 (Length*(j+1)     > csmc_cat[:,1])&
                                 (Length*k        <= csmc_cat[:,2])&
                                 (Length*(k+1)     > csmc_cat[:,2])&
                                 #Mass condition
                                 (bins_mass[l]    <= csmc_cat[:,3])&
                                 (bins_mass[l+1]   > csmc_cat[:,3]))
                cosmic_variance[counter,l,0] += index[0].size
                #LF
                index = np.where(
                                 #spatial condition
                                 (Length*i        <= csmc_cat[:,0])&
                                 (Length*(i+1)     > csmc_cat[:,0])&
                                 (Length*j        <= csmc_cat[:,1])&
                                 (Length*(j+1)     > csmc_cat[:,1])&
                                 (Length*k        <= csmc_cat[:,2])&
                                 (Length*(k+1)     > csmc_cat[:,2])&
                                 #Magnitude condition
                                 (bins_mag[l]    <= csmc_cat[:,4])&
                                 (bins_mag[l+1]   > csmc_cat[:,4]))
                cosmic_variance[counter,l,1] += index[0].size
                #end for l
        counter +=1
        #end for k
    #end for j
#end for i

# <codecell>


print cosmic_variance[0,:,:]

# <codecell>

cosmic_variance_norm = cosmic_variance 

cosmic_variance_norm[:,:,0] /=  LocalCellVolume*M_BIN_width
cosmic_variance_norm[:,:,1] /=  LocalCellVolume*Magnitude_BIN_width

#print cosmic_variance_norm[0,:,:]

# <codecell>

# Plotting the 64 Mass Density Functions
for counter in range(64):
    plt.semilogy(bins_mass, cosmic_variance_norm[counter,:,0])
plt.title("Mass Density Function")
plt.xlabel(r"$\log_{10} M_\odot$")
plt.ylabel(r"$\log \frac{dM}{dN}\left( Mpc^3 h^{-1} \right)$")

plt.show()

# <codecell>

# Plotting Luminosity Function
for counter in range(64):
    plt.semilogy(bins_mag, cosmic_variance_norm[counter,:,1])
plt.title("Luminosity Function")
plt.xlabel("Magnitude")
plt.ylabel(r"$\log \frac{dL}{dMag} $")

plt.show()

# <codecell>


