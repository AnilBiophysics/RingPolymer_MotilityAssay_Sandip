import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import LogLocator

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

scale = 0.001 / 7915.71747

x2, y2 = np.loadtxt('V24_M1_omega0.5_gamma10_avg_MSD_t.txt', unpack=True)
x3, y3 = np.loadtxt('V65_M1_omega0.5_gamma10_avg_MSD_t.txt', unpack=True)

fig, ax = plt.subplots(figsize=(8, 6), constrained_layout=True)

ax.plot(x3 * scale, y3 / 50**2, label=r"\boldmath$Pe=16.2\times10^5$", color='red', linestyle='-', marker='s', linewidth=1.5, markersize=6, markeredgecolor='red', markerfacecolor='none', markevery=10)
ax.plot(x2 * scale, y2 / 50**2, label=r"\boldmath$Pe=6\times10^5$", color='darkblue', linestyle='--', marker='o', linewidth=1.5, markersize=6, markeredgecolor='darkblue', markerfacecolor='none', markevery=10)

ax.set_ylabel(r'\boldmath$\langle \Delta r_{tot}^2 \rangle/L^2$', fontsize=16)
ax.set_xlabel(r'\boldmath$\Delta t/\tau$', fontsize=14)
ax.legend(loc='lower right', fontsize=15)

ax.set_xscale('log')
ax.set_yscale('log')

ax.set_xticks([1e-7, 1e-6, 1e-5, 1e-4, 1e-3,1e-2])
ax.set_xticklabels([ r'\boldmath$10^{-7}$', r'\boldmath$10^{-6}$', r'\boldmath$10^{-5}$', r'\boldmath$10^{-4}$',r'\boldmath$10^{-3}$',r'\boldmath$10^{-2}$'], fontsize=15)

ax.set_yticks([1e-5, 1e-4, 1e-3, 1e-2, 1e-1])
ax.set_yticklabels([r'\boldmath$10^{-5}$', r'\boldmath$10^{-4}$', r'\boldmath$10^{-3}$', r'\boldmath$10^{-2}$', r'\boldmath$10^{-1}$'], fontsize=15)

xfit = x3 * scale
yfit = y3 / 50**2

mask1 = (xfit >= 1e-5) & (xfit <= 1e-4)

if np.sum(mask1) > 2:
    lx = np.log10(xfit[mask1])
    ly = np.log10(yfit[mask1])
    slope1, intercept1 = np.polyfit(lx, ly, 1)
    t1 = np.logspace(np.log10(1e-5), np.log10(1e-4), 100)
    fit_line1 = 0.8*10**intercept1 * t1**slope1
    #ax.plot(t1, fit_line1, color='black', linestyle='-', linewidth=1.2)
    #print("Scaling exponent (regime) =", slope1)

ax.minorticks_on()

ax.xaxis.set_minor_locator(LogLocator(base=10.0, subs=np.arange(2, 10), numticks=40))
ax.yaxis.set_minor_locator(LogLocator(base=10.0, subs=np.arange(2, 10), numticks=40))

ax.tick_params(which='minor', length=4, width=1, colors='black', direction='in', top=True, right=True)
ax.tick_params(which='major', length=6, width=1, colors='black', direction='in', labelsize=14, top=True, right=True)

ax.set_xlim(1e-7, 1e-2)
ax.set_ylim(1e-6, 5*1e-1)

border_width = 1.7
for spine in ax.spines.values():
    spine.set_linewidth(border_width)

plt.savefig('MSD_COM_vs_t_M1_gamma10_omega_0.5.pdf', bbox_inches='tight')
