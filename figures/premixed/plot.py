
import numpy as np
import matplotlib
matplotlib.use('PDF')       
import matplotlib.pyplot as plt

########################################################################

#-------------- DEFINE THE DATA TO PLOT (or get it from somewhere)
rhosoot = 1850

e1  = np.loadtxt('soot.exp_1')
e2  = np.loadtxt('soot.exp_2')
e3  = np.loadtxt('soot.exp_3')
s   = np.loadtxt('burner.out')
ss  = np.loadtxt('burner_static.out')


x1  = e1[:,0] * 100
x2  = e2[:,0] * 100
x3  = e3[:,0] * 100
xs  = s[ :,0] * 100
xss = ss[ :,0] * 100
y1  = e1[:,1] * 1E6
y2  = e2[:,1] * 1E6
y3  = e3[:,1] * 1E6
ys  = s[ :,8] * 1E6 / rhosoot
yss = ss[ :,2] * 1E6 / rhosoot

#-------------- SET UP SOME PLOT BOILERPLATE

matplotlib.rcParams.update({'font.size':20, 'figure.autolayout': True}) 
fig, ax = plt.subplots()
ax.tick_params(which='both', direction='in', top=True, right=True)
plt.cla()

#-------------- MAKE THE PLOT

ax.plot(xs, ys,   '-',  color='black',  linewidth=2) 
ax.plot(xss,yss,  '--', color='black',   linewidth=1) 
ax.plot(x1, y1,   'o',  color='black',  markersize=4) 
ax.plot(x2, y2,   's',  color='black',  markersize=4) 
ax.plot(x3, y3,   '^',  color='black',  markersize=4) 

ax.set_xlabel("z (cm)", fontsize=22)
ax.set_ylabel(r"$f_v$ (ppmv)",fontsize=22)
ax.set_yscale('log')
ax.set_xlim([0,3])
#ax.set_ylim([1E-10,1E-4])
ax.set_ylim([1E-4,10])

ax.xaxis.set_minor_locator(matplotlib.ticker.AutoMinorLocator())


ax.legend(['SootLib Cantera', 'SootLib static', 'Xu & Faeth Laser', 'Xu & Faeth Sampling', 'Menon Laser'], loc='lower right', frameon=False, fontsize=16)

#-------------- SAVE PLOT TO FILE CALLED plot.pdf (the ".pdf" is left off below)

plt.savefig("burner")

