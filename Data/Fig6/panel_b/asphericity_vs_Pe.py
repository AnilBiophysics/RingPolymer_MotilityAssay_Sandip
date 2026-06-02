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

#x = np.array([1, 5, 10, 15, 24, 35, 45, 55, 65, 75, 85, 95]) * (49**2)*10

scale = (50**2)*10

x0_1, y0_1, error_1 = np.loadtxt('asphericity_M1_gamma10_t2_omega0.1.txt', unpack=True)
x0_2, y0_2, error_2 = np.loadtxt('asphericity_M1_gamma10_t2_omega0.5.txt', unpack=True)
x0_3, y0_3, error_3 = np.loadtxt('asphericity_M1_gamma10_t2_omega0.9.txt', unpack=True)

fig, ax = plt.subplots(figsize=(9,7))

ax.errorbar(x0_3* scale, y0_3, yerr=error_3/np.sqrt(20), fmt='D', color='red', markersize=8,markerfacecolor='none', capsize=4, linewidth=2, label=r"\boldmath$\Omega=0.9$")
ax.errorbar(x0_2* scale, y0_2, yerr=error_2/np.sqrt(20), fmt='s', color='green', markersize=10,markerfacecolor='none', capsize=4, linewidth=2, label=r"\boldmath$\Omega=0.5$")
ax.errorbar(x0_1* scale, y0_1, yerr=error_1/np.sqrt(20), fmt='o', color='blue', markersize=10,markerfacecolor='none', capsize=4, linewidth=2, label=r"\boldmath$\Omega=0.1$")




ax.scatter(x0_1 * scale, y0_1, marker='o', color='blue', s=64, facecolors='none')
ax.scatter(x0_2 * scale, y0_2, marker='s', color='green', s=64, facecolors='none')
ax.scatter(x0_3 * scale, y0_3, marker='D', color='red', s=64, facecolors='none')


ax.plot(x0_1* scale, y0_1, color='blue', linestyle='--',linewidth=2)
ax.plot(x0_2* scale, y0_2, color='green', linestyle=':',linewidth=3)
ax.plot(x0_3* scale, y0_3, color='red', linestyle='-.',linewidth=2)

ax.set_xlabel(r'\boldmath$Pe$', fontsize=21, fontweight='bold')
#ax.set_ylabel(r'\boldmath$\langle A\rangle$', fontsize=21, fontweight='bold')

ax.set_xticks([0,0.50*1e6,1e6,1.5*1e6,2.0*1e6,2.50*1e6,3*1e6,3.5*1e6])
ax.set_yticks([0.10,0.15,0.20,0.25,0.30,0.35,0.40,0.45,0.50])
ax.set_xticklabels([r'\boldmath$0$', r'\boldmath$0.50$',r'\boldmath$1.0$',r'\boldmath$1.50$',r'\boldmath$2.00$',r'\boldmath$2.50$',r'\boldmath$3.0$',r'\boldmath$3.50$'], fontsize=18)
ax.set_yticklabels([r'\boldmath$0.10$', r'\boldmath$0.15$',r'\boldmath$0.20$',r'\boldmath$0.25$',r'\boldmath$0.30$',r'\boldmath$0.35$',r'\boldmath$0.40$',r'\boldmath$0.45$',r'\boldmath$0.50$'], fontsize=18)


ax.tick_params(axis='both', which='major', length=8, width=2, direction='in', top=True, right=True)
ax.tick_params(axis='both', which='minor', length=4, width=1.5, direction='in', top=True, right=True)
ax.minorticks_on()

ax.legend(fontsize=16)

ax.text(1.12, -0.04, r'\boldmath$(\times 10^6)$', transform=ax.transAxes,
        fontsize=18, fontweight='bold', ha='right')

for spine in ax.spines.values():
    spine.set_linewidth(2.5)
ax.set_title(r"\boldmath{$(b)$}", fontsize=20)
#plt.xlim(0,240000)
#plt.ylim(0.05,0.45)
plt.tight_layout()
plt.savefig('asphericity_vs_pe_M1.pdf')

