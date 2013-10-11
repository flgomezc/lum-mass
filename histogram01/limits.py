#open the datafile
#data = open('/home/flgomez10/lum-mass/data/MD_3840_Planck1/BDM/test.dat',"r")
data = open('/home/flgomez10/lum-mass/data/MD_3840_Planck1/BDM/reduced_catshortV_007.dat',"r")
#read and ignore header lines
data.seek(0)
for i in range(0,17):
    data.readline()
    
mass_min = 5e+10
mass_max = 1e+12
x_max = 5
y_max = 5
z_max = 5
    
for line in data:
    line = line.strip()
    columns = line.split()
    x = float(columns[0])
    y = float(columns[1])
    z = float(columns[2])
    mass = float(columns[3])
#    print mass
    if( mass_min > mass):
        mass_min = mass
    if( mass_max < mass):
        mass_max = mass
# box size (Mpc h-1)
    if x > x_max:
	x_max = x
    if y > y_max:
        y_max=y
    if z > z_max:
	z_max=z
            
print "Lower mass limit = ", mass_min, "\nUpper mass limit = ", mass_max, "\nx_max =", x_max,"\ny_max =", y_max,  "\nz_max =", z_max
