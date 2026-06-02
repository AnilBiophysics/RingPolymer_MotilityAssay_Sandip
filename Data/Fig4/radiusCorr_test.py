import numpy as np
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D, HandlerTuple
from matplotlib.ticker import FormatStrFormatter
from scipy.interpolate import UnivariateSpline

plt.rcParams.update({
    'text.usetex': True,
    'font.family': 'serif',
    'font.serif': ['Times New Roman'],
    'font.sans-serif': ['Helvetica', 'Arial', 'Droid Sans'],
    'text.color': 'black',
    'axes.labelcolor': 'black',
    'xtick.color': 'black',
    'ytick.color': 'black',
    'font.weight': 'normal',
    'figure.dpi': 800
})

plt.close('all')

x1_0, y1_0 = np.loadtxt('V25_M1_omega0.5_gamma10_t2_radicorr.txt', unpack=True)
x2_0, y2_0 = np.loadtxt('V25_M1_omega0.5_gamma10_t10_radicorr.txt', unpack=True)
x3_0, y3_0 = np.loadtxt('V25_M1_omega0.5_gamma10_t30_radicorr.txt', unpack=True)

x0_1, y0_1, yerr0_1, z0_1, zerr0_1 = np.loadtxt('timescale_omega0.5_t2.txt', unpack=True)
x0_2, y0_2, yerr0_2, z0_2, zerr0_2 = np.loadtxt('timescale_omega0.5_t10.txt', unpack=True)
x0_3, y0_3, yerr0_3, z0_3, zerr0_3 = np.loadtxt('timescale_omega0.5_t30.txt', unpack=True)

fig, axs = plt.subplots(1, 3, figsize=(24, 7))

scale = 10 * 50**2
tau = 10 * 50**3 / (24 * np.pi**2)

axs[0].plot(x1_0*0.0009 /tau, y1_0, label=r"\boldmath$l_p/L=0.5$",color='darkblue', linestyle='-', linewidth=2.0, markersize=6, markeredgecolor='red', markerfacecolor='none',markeredgewidth=1.5)
axs[0].plot(x2_0*0.0009 /tau, y2_0, label=r"\boldmath$l_p/L=0.1$",color='darkgreen', linestyle='-', linewidth=2.0, markersize=6, markeredgecolor='green', markerfacecolor='none',markeredgewidth=1.5)
axs[0].plot(x3_0*0.0009 /tau, y3_0, label=r"\boldmath$l_p/L=0.03$",color='red', linestyle='-', linewidth=2.0, markersize=6, markeredgecolor='darkblue', markerfacecolor='none',markeredgewidth=1.5)
axs[0].set_xlabel(r'\boldmath$t$', fontsize=23)
axs[0].set_ylabel(r'\boldmath$\langle \mathbf{r}_d(t)\mathbf{r}_d(0) \rangle/\langle r_d^2\rangle$', fontsize=20)
axs[0].legend(fontsize=20)
axs[0].set_xlim(0, 0.0008)
axs[0].set_title(r'\boldmath$(a)$', fontsize=20)

axs[0].set_xticks([0,1e-4,2e-4,3e-4,4e-4,5e-4,6e-4,7e-4,8e-4])
axs[0].set_xticklabels([r'\boldmath$0$', r'\boldmath$1$', r'\boldmath$2$', r'\boldmath$3$', r'\boldmath$4$', r'\boldmath$5$', r'\boldmath$6$', r'\boldmath$7$',r'\boldmath$8$'], fontsize=22)
axs[0].text(0.90, -0.09, r'\boldmath$(\times 10^{-4})$', transform=axs[0].transAxes, fontsize=20, fontweight='bold')
axs[0].set_yticks([-0.75,-0.50,-0.25,0.00,0.25,0.50,0.75,1.00])
axs[0].set_yticklabels([r'\boldmath$-0.75$', r'\boldmath$-0.50$', r'\boldmath$-0.25$', r'\boldmath$0.0$', r'\boldmath$0.25$', r'\boldmath$0.50$', r'\boldmath$0.75$', r'\boldmath$1.0$'], fontsize=20)

axs[1].errorbar(x0_1 * scale, y0_1, yerr=yerr0_1, fmt='o',  capsize=4,markersize = 10, color='darkgreen', label=r"\boldmath$l_p/L=0.5$")
axs[1].errorbar(x0_2 * scale, y0_2, yerr=yerr0_2, fmt='s',  capsize=4,markersize = 10, color='darkblue',label=r"\boldmath$l_p/L=0.1$")
axs[1].errorbar(x0_3 * scale, y0_3, yerr=yerr0_3, fmt='D',  capsize=4,markersize = 10, color='red', label=r"\boldmath$l_p/L=0.03$")
'''axs[1].plot(x0_1 * scale, y0_1, linestyle=':', linewidth=0.6, color='darkgreen')
axs[1].plot(x0_2 * scale, y0_2, linestyle=':', linewidth=0.6, color='darkblue')
axs[1].plot(x0_3 * scale, y0_3, linestyle=':', linewidth=0.6, color='red')'''

axs[1].set_xlabel(r'\boldmath$Pe$', fontsize=20)
axs[1].set_ylabel(r'\boldmath$\tau_1$', fontsize=20)
axs[1].legend(fontsize=20)
axs[1].set_title(r'\boldmath$(b)$', fontsize=20)

axs[1].set_xticks([0 * 1e6, 0.5 * 1e6, 1.0 * 1e6, 1.5 * 1e6, 2.0 * 1e6])
axs[1].set_xticklabels([r'\boldmath$0$', r'\boldmath$0.50$', r'\boldmath$1.0$', r'\boldmath$1.50$', r'\boldmath$2.0$'], fontsize=20)
axs[1].text(0.90, -0.08, r'\boldmath$(\times 10^6)$', transform=axs[1].transAxes, fontsize=20, fontweight='bold')
axs[1].set_yticks([0.00010, 0.00015, 0.00020, 0.00025, 0.00030, 0.00035, 0.00040, 0.00045])
axs[1].set_yticklabels([r'\boldmath$1.0$', r'\boldmath$1.5$', r'\boldmath$2.0$', r'\boldmath$2.5$', r'\boldmath$3.0$', r'\boldmath$3.5$', r'\boldmath$4.0$', r'\boldmath$4.5$'], fontsize=20)
axs[1].text(-0.08, 1.04, r'\boldmath$(\times 10^{-4})$', transform=axs[1].transAxes, fontsize=20, fontweight='bold')

axs[2].errorbar(x0_1 * scale, z0_1, yerr=zerr0_1, fmt='o',  capsize=4,markersize = 10, color='darkgreen',label=r"\boldmath$l_p/L=0.5$")
axs[2].errorbar(x0_2 * scale, z0_2, yerr=zerr0_2, fmt='s',  capsize=4,markersize = 10, color='darkblue',label=r"\boldmath$l_p/L=0.1$")
axs[2].errorbar(x0_3 * scale, z0_3, yerr=zerr0_3, fmt='D',  capsize=4,markersize = 10, color='red',label=r"\boldmath$l_p/L=0.03$")
'''axs[2].plot(x0_1 * scale, z0_1, linestyle=':', linewidth=0.6, color='darkgreen')
axs[2].plot(x0_2 * scale, z0_2, linestyle=':', linewidth=0.6, color='darkblue')
axs[2].plot(x0_3 * scale, z0_3, linestyle=':', linewidth=0.6, color='red')'''

axs[2].set_xlabel(r'\boldmath$Pe$', fontsize=20)
axs[2].set_ylabel(r'\boldmath$\omega_1$', fontsize=20)
axs[2].legend(fontsize=20)
axs[2].set_title(r'\boldmath$(c)$', fontsize=20)

axs[2].set_xticks([0 * 1e6, 0.5 * 1e6, 1.0 * 1e6, 1.5 * 1e6, 2.0 * 1e6])
axs[2].set_xticklabels([r'\boldmath$0$', r'\boldmath$0.50$', r'\boldmath$1.0$', r'\boldmath$1.50$', r'\boldmath$2.0$'], fontsize=20)
axs[2].text(0.90, -0.08, r'\boldmath$(\times 10^6)$', transform=axs[2].transAxes, fontsize=20, fontweight='bold')
axs[2].set_yticks([0,50000,100000,150000,200000,250000,300000])
axs[2].set_yticklabels([r'\boldmath$0$', r'\boldmath$5$', r'\boldmath$10$', r'\boldmath$15$', r'\boldmath$20$', r'\boldmath$25$', r'\boldmath$30$'], fontsize=20)
axs[2].text(-0.08, 1.04, r'\boldmath$(\times 10^{4})$', transform=axs[2].transAxes, fontsize=20, fontweight='bold')


x1s = np.linspace(min(x0_1*scale), max(x0_1*scale), 500)
x2s = np.linspace(min(x0_2*scale), max(x0_2*scale), 500)
x3s = np.linspace(min(x0_3*scale), max(x0_3*scale), 500)

spline1 = UnivariateSpline(x0_1*scale, y0_1, k=3, s=0)
spline2 = UnivariateSpline(x0_2*scale, y0_2, k=3, s=0)
spline3 = UnivariateSpline(x0_3*scale, y0_3, k=3, s=0)

axs[1].plot(x1s, spline1(x1s), linestyle=':', linewidth=3, color='darkgreen')
axs[1].plot(x2s, spline2(x2s), linestyle=':', linewidth=3, color='darkblue')
axs[1].plot(x3s, spline3(x3s), linestyle=':', linewidth=3, color='red')

spline4 = UnivariateSpline(x0_1*scale, z0_1, k=3, s=0)
spline5 = UnivariateSpline(x0_2*scale, z0_2, k=3, s=0)
spline6 = UnivariateSpline(x0_3*scale, z0_3, k=3, s=0)

axs[2].plot(x1s, spline4(x1s), linestyle=':', linewidth=3, color='darkgreen')
axs[2].plot(x2s, spline5(x2s), linestyle=':', linewidth=3, color='darkblue')
axs[2].plot(x3s, spline6(x3s), linestyle=':', linewidth=3, color='red')



for ax in axs:
    ax.minorticks_on()
    ax.tick_params(which='major', length=6, width=1, direction='in', top=True, right=True)
    ax.tick_params(which='minor', length=4, width=1, direction='in', top=True, right=True)
    for spine in ax.spines.values():
        spine.set_linewidth(2)
axs[0].set_xlim(0,5e-4)
plt.tight_layout()
plt.savefig('decayTime_radiusCorr_M1_gamma10_omega0.5_varyPersistence.pdf')
plt.close()
