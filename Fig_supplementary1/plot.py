import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator

# Plot style and font configuration
plt.rcParams['text.usetex'] = True
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.rcParams['font.sans-serif'] = ['Helvetica', 'Arial', 'Droid Sans']
plt.rcParams['text.color'] = 'black'
plt.rcParams['axes.labelcolor'] = 'black'
plt.rcParams['xtick.color'] = 'black'
plt.rcParams['ytick.color'] = 'black'
plt.rcParams['font.weight'] = 'normal'
plt.rcParams['figure.dpi'] = 600  

plt.close('all')

x1, y1 = np.loadtxt('V24_M1_omega0.5_gamma10_avg_MSD_t.txt', unpack=True)
x2, y2 = np.loadtxt('V65_M1_omega0.5_gamma10_avg_MSD_t.txt', unpack=True)

scale = 0.001/5277.14498137
fig, ax = plt.subplots(figsize=(6.5, 5), constrained_layout=True)

ax.plot(x2[::50]*scale, y2[::50]/50**2, label=r"\boldmath$Pe=16.2\times10^5$", color='darkblue', linestyle='-', linewidth=2, marker='o', markersize=6, markeredgecolor='darkblue', markerfacecolor='none')

ax.plot(x1[::50]*scale, y1[::50]/50**2, label=r"\boldmath$Pe=6\times10^5$", color='red', linestyle='--', linewidth=2, marker='s', markersize=6, markeredgecolor='red', markerfacecolor='none')

ax.set_ylabel(r'\boldmath$\langle (\Delta r)^2 \rangle/L^2$', fontsize=16)
ax.set_xlabel(r'\boldmath$\Delta t/\tau$', fontsize=14)
ax.legend(loc='lower right', fontsize=16)

ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xticks([1e-7, 1e-6,1e-5, 1e-4,1e-3,1e-2])
ax.set_yticks([1e-5,1e-4, 1e-3, 1e-2,1e-1])
ax.set_yticklabels([r'\boldmath$10^{-5}$', r'\boldmath$10^{-4}$', r'\boldmath$10^{-3}$', r'\boldmath$10^{-2}$',r'\boldmath$10^{-1}$'], fontsize=18)
ax.set_xticklabels([r'\boldmath$10^{-7}$', r'\boldmath$10^{-6}$', r'\boldmath$10^{-5}$', r'\boldmath$10^{-4}$',r'\boldmath$10^{-3}$',r'\boldmath$10^{-2}$'], fontsize=18)

ax.minorticks_on()
ax.tick_params(which='both', length=4, width=1, colors='black', direction='in', labelsize=0)
ax.xaxis.set_minor_locator(LogLocator(base=10.0, subs='auto', numticks=10))
ax.yaxis.set_minor_locator(LogLocator(base=10.0, subs='auto', numticks=10))
ax.set_xlim(3*1e-5, 2*1e-2)
ax.set_ylim(1e-4, 5*1e-1)
#ax.set_title(r'\boldmath$(a)$', fontsize=20, verticalalignment='top')

x_subs = np.arange(2, 10)
ax.xaxis.set_minor_locator(LogLocator(base=10.0, subs=x_subs, numticks=40))
ax.yaxis.set_minor_locator(LogLocator(base=10.0, subs=x_subs, numticks=40))  
ax.tick_params(which='minor', length=4, width=1, colors='black', direction='in', labelsize=0, top=True, right=True)
ax.tick_params(which='major', length=6, width=1, colors='black', direction='in', labelsize=14, top=True, right=True)

border_width = 1.7
for spine in ax.spines.values():
    spine.set_linewidth(border_width)

# Save figure
plt.savefig('MSD_COM_vs_t_M1_gamma10_omega_0.5.pdf', bbox_inches='tight')

