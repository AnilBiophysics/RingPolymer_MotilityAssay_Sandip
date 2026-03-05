import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['font.sans-serif'] = ['Helvetica', 'Arial', 'Droid Sans']
plt.rcParams['text.color'] = 'black'
plt.rcParams['axes.labelcolor'] = 'black'
plt.rcParams['xtick.color'] = 'black'
plt.rcParams['ytick.color'] = 'black'
plt.rcParams['font.weight'] = 'normal'
plt.rcParams['figure.dpi'] = 800  

plt.close('all')

#x = np.array([1, 5, 10, 15, 24, 35, 45, 55, 65, 75, 85, 95]) * (50**2)*10

scale = 10*(50**2)

x0_1, y0_1, error_1 = np.loadtxt('omega0.5_t2_angular_velocity_vs_Pe.txt', unpack=True)
x0_2, y0_2, error_2 = np.loadtxt('omega0.5_t10_angular_velocity_vs_Pe.txt', unpack=True)
x0_3, y0_3, error_3 = np.loadtxt('omega0.5_t30_angular_velocity_vs_Pe.txt', unpack=True)

y0_1 = 50*np.abs(y0_1)*(10*50**3/(24*np.pi**2))
y0_2 = 50*np.abs(y0_2)*(10*50**3/(24*np.pi**2))
y0_3 = 50*np.abs(y0_3)*(10*50**3/(24*np.pi**2))

fig, ax = plt.subplots(figsize=(8,6))



ax.errorbar(x0_1* scale, y0_1, yerr=error_1/np.sqrt(20), fmt='o', color='blue', markersize=10, capsize=4, linewidth=2, label=r"\boldmath$l_p/L=0.5$")
ax.errorbar(x0_2* scale, y0_2, yerr=error_2/np.sqrt(20), fmt='s', color='red', markersize=10, capsize=4, linewidth=2, label=r"\boldmath$l_p/L=0.1$")
ax.errorbar(x0_3* scale, y0_3, yerr=error_3/np.sqrt(20), fmt='D', color='green', markersize=10, capsize=4, linewidth=2, label=r"\boldmath$l_p/L=0.03$")

ax.scatter(x0_1 * scale, y0_1, marker='o', color='blue', s=64, facecolors='none')
ax.scatter(x0_2 * scale, y0_2, marker='s', color='red', s=64, facecolors='none')
ax.scatter(x0_3 * scale, y0_3, marker='D', color='green', s=64, facecolors='none')



ax.plot(x0_1* scale, y0_1, color='blue', linestyle='--',linewidth=2)
ax.plot(x0_2* scale, y0_2, color='red', linestyle=':',linewidth=3)
ax.plot(x0_3* scale, y0_3, color='green', linestyle='-',linewidth=2)


#ax.set_xlabel(r'\boldmath$Pe$', fontsize=21, fontweight='bold')
ax.set_ylabel(r'\boldmath$\langle|\omega_{ang}|\rangle \tau $', fontsize=21, fontweight='bold')

ax.set_xticks([0,0.50*1e6,1e6,1.5*1e6,2.0*1e6])
ax.set_yticks([0,1000,2000,3000,4000,5000,6000,7000])
ax.set_xticklabels([r'\boldmath$0$',  r'\boldmath$0.50$', 
                    r'\boldmath$1.0$',r'\boldmath$1.50$',r'\boldmath$2.00$'], fontsize=18)
ax.set_yticklabels([r'\boldmath$0$', r'\boldmath$1000$', r'\boldmath$2000$',r'\boldmath$3000$',r'\boldmath$4000$',r'\boldmath$5000$',r'\boldmath$6000$',r'\boldmath$7000$'], fontsize=18)


ax.tick_params(axis='both', which='major', length=8, width=2, direction='in', top=True, right=True)
ax.tick_params(axis='both', which='minor', length=4, width=1.5, direction='in', top=True, right=True)
ax.minorticks_on()
ax.set_title(r"\boldmath{$(a)$}", fontsize=20)
ax.legend(fontsize=20)

ax.text(1, -0.1, r'\boldmath$(\times 10^6)$', transform=ax.transAxes,
        fontsize=18, fontweight='bold', ha='right')

for spine in ax.spines.values():
    spine.set_linewidth(2.5)

#plt.xlim(0,240000)
#plt.ylim(0.05,0.25)
plt.tight_layout()
plt.savefig('angularVel_vs_pe_M1_gamma10_omega0.5_varyPersistence.pdf')

