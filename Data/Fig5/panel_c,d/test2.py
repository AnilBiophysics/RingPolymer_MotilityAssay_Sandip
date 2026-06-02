import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    'text.usetex': True,
    'font.family': 'serif',
    'font.serif': ['Times New Roman'],
    'text.color': 'black',
    'axes.labelcolor': 'black',
    'xtick.color': 'black',
    'ytick.color': 'black',
    'figure.dpi': 800
})

plt.close('all')

x1, y1, z1err = np.loadtxt('rd2_vs_Pe_t2.txt', unpack=True)
x2, y2, z2err = np.loadtxt('rd2_vs_Pe_t10.txt', unpack=True)
x3, y3, z3err = np.loadtxt('rd2_vs_Pe_t30.txt', unpack=True)

z1err= z1err/np.sqrt(20)
z2err= z2err/np.sqrt(20)
z3err= z3err/np.sqrt(20)

x4, y4, z4err = np.loadtxt('rd2_vs_persistence_omega0.1.txt', unpack=True)
x5, y5, z5err = np.loadtxt('rd2_vs_persistence_omega0.5.txt', unpack=True)
x6, y6, z6err = np.loadtxt('rd2_vs_persistence_omega0.9.txt', unpack=True)

z4err= z4err/np.sqrt(20)
z5err= z5err/np.sqrt(20)
z6err= z6err/np.sqrt(20)

fig, axs = plt.subplots(1, 2, figsize=(12, 6))

scale = 10 * (50**2)
norm = 50**2

axs[0].errorbar(x1 * scale, y1 / norm, yerr=z1err / norm,
                fmt='o', color='blue', markersize=8,
                markerfacecolor='none', linewidth=2,
                capsize=3, label=r'\boldmath$l_p/L=0.5$')

axs[0].errorbar(x2 * scale, y2 / norm, yerr=z2err / norm,
                fmt='s', color='red', markersize=8,
                markerfacecolor='none', linewidth=2,
                capsize=3, label=r'\boldmath$l_p/L=0.1$')

axs[0].errorbar(x3 * scale, y3 / norm, yerr=z3err / norm,
                fmt='D', color='magenta', markersize=8,
                markerfacecolor='none', linewidth=2,
                capsize=3, label=r'\boldmath$l_p/L=0.03$')

axs[0].set_xlabel(r'\boldmath$Pe$', fontsize=20)
axs[0].set_ylabel(r'\boldmath$\langle r_d^2\rangle/L^2$', fontsize=20)
axs[0].legend(loc='best', fontsize=16, markerscale=1.5)
axs[0].set_title(r'\boldmath$(c)$', fontsize=20)

axs[0].set_xticks([0,0.50*1e6,1e6,1.5*1e6,2.0*1e6])
#axs[0].set_yticks([0.05,0.06,0.07,0.08,0.09])
axs[0].set_xticklabels([r'\boldmath$0$', r'\boldmath$5.0$',r'\boldmath$10.0$',r'\boldmath$15.0$',r'\boldmath$20.0$'], fontsize=14)
#axs[0].set_yticklabels([r'\boldmath$0.05$', r'\boldmath$0.06$', r'\boldmath$0.07$',r'\boldmath$0.08$',r'\boldmath$0.09$'], fontsize=14)
axs[0].text(1.0, -0.1, r'\boldmath$(\times 10^6)$',
            transform=axs[0].transAxes, fontsize=14,
            fontweight='bold', ha='right')

axs[1].errorbar(1/x4, y4 / norm, yerr=z4err / norm,
                fmt='o-', color='blue', markersize=8,
                markerfacecolor='none', linewidth=2,
                capsize=3, label=r'\boldmath$\Omega=0.1$')

axs[1].errorbar(1/x5, y5 / norm, yerr=z5err / norm,
                fmt='s-', color='red', markersize=8,
                markerfacecolor='none', linewidth=2,
                capsize=3, label=r'\boldmath$\Omega=0.5$')

axs[1].errorbar(1/x6, y6 / norm, yerr=z6err / norm,
                fmt='D-', color='magenta', markersize=8,
                markerfacecolor='none', linewidth=2,
                capsize=3, label=r'\boldmath$\Omega=0.9$')

axs[1].set_xlabel(r'\boldmath$l_p/L$', fontsize=20)
axs[1].set_xticks([0.1, 0.2, 0.3, 0.4, 0.5])
#axs[1].set_yticks([0.05, 0.06, 0.07, 0.08, 0.09])
axs[1].set_xticklabels([r'\boldmath$0.1$', r'\boldmath$0.2$', r'\boldmath$0.3$', r'\boldmath$0.4$', r'\boldmath$0.5$'], fontsize=14)
#axs[1].set_yticklabels([r'\boldmath$0.05$', r'\boldmath$0.06$', r'\boldmath$0.07$', r'\boldmath$0.08$', r'\boldmath$0.09$'], fontsize=14)
axs[1].legend(loc='best', fontsize=16, markerscale=1.5)
axs[1].set_title(r'\boldmath$(d)$', fontsize=20)

for ax in axs:
    ax.minorticks_on()
    ax.tick_params(which='minor', length=4, width=1,
                   colors='black', direction='in', top=True, right=True)
    ax.tick_params(which='major', length=6, width=1,
                   colors='black', direction='in', top=True, right=True)
    for spine in ax.spines.values():
        spine.set_linewidth(2.2)

plt.tight_layout()
plt.savefig('radiusSqr_M1_gamma10.pdf')
