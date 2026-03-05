import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

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

x1_0, y1_0 = np.loadtxt('Avg_spatial_correlation_v24_t2_omega0.2.txt', unpack=True)
x2_0, y2_0 = np.loadtxt('Avg_spatial_correlation_v24_t3.33_omega0.2.txt', unpack=True)
x3_0, y3_0 = np.loadtxt('Avg_spatial_correlation_v24_t10_omega0.2.txt', unpack=True)
x4_0, y4_0 = np.loadtxt('Avg_spatial_correlation_v24_t30_omega0.2.txt', unpack=True)

x1_2, y1_2 = np.loadtxt('Avg_spatial_correlation_v24_t2_omega0.8.txt', unpack=True)
x2_2, y2_2 = np.loadtxt('Avg_spatial_correlation_v24_t3.33_omega0.8.txt', unpack=True)
x3_2, y3_2 = np.loadtxt('Avg_spatial_correlation_v24_t10_omega0.8.txt', unpack=True)
x4_2, y4_2 = np.loadtxt('Avg_spatial_correlation_v24_t30_omega0.8.txt', unpack=True)

fig, axs = plt.subplots(1, 2, figsize=(12, 6))
scale = 1/50

axs[0].plot(x1_0 * scale, y1_0, label=r"\boldmath$l_p/L=0.5$", color='black', linestyle='-', linewidth=1.0, marker='o', markersize=6, markeredgecolor='magenta', markerfacecolor='none', markeredgewidth=1.5)
axs[0].plot(x2_0 * scale, y2_0, label=r"\boldmath$l_p/L=0.3$", color='black', linestyle='-', linewidth=1.0, marker='s', markersize=6, markeredgecolor='lime', markerfacecolor='none', markeredgewidth=1.5)
axs[0].plot(x3_0 * scale, y3_0, label=r"\boldmath$l_p/L=0.1$", color='black', linestyle='-', linewidth=1.0, marker='^', markersize=6, markeredgecolor='darkblue', markerfacecolor='none', markeredgewidth=1.5)
axs[0].plot(x4_0 * scale, y4_0, label=r"\boldmath$l_p/L=0.03$", color='black', linestyle='-', linewidth=1.0, marker='D', markersize=6, markeredgecolor='red', markerfacecolor='none', markeredgewidth=1.5)
axs[0].legend(loc='best', markerscale=1.5, fontsize=16)
axs[0].set_xlabel('\\boldmath$s/L$', fontsize=20)
axs[0].set_ylabel('\\boldmath$\langle \hat{t}(s)\cdot \hat{t}(s^{\prime})\\rangle$', fontsize=20)
axs[0].set_yticks([-0.8,-0.6,-0.4,-0.2,0,0.2,0.4,0.6,0.8,1.0])
axs[0].set_yticklabels(['\\boldmath$-0.8$', '\\boldmath$-0.6$','\\boldmath$-0.4$', '\\boldmath$-0.2$', '\\boldmath$0.0$', '\\boldmath$0.2$','\\boldmath$0.4$','\\boldmath$0.6$','\\boldmath$0.8$','\\boldmath$1.0$'], fontsize=28)
axs[0].set_xticks([0,0.2,0.4,0.6,0.8,1.0])
axs[0].set_xticklabels(['\\boldmath$0$', '\\boldmath$0.2$', '\\boldmath$0.4$', '\\boldmath$0.6$','\\boldmath$0.8$','\\boldmath$1.0$'], fontsize=28)

axs[1].plot(x1_2 * scale, y1_2, label=r"\boldmath$l_p/L=0.5$", color='black', linestyle='-', linewidth=1.0, marker='o', markersize=6, markeredgecolor='magenta', markerfacecolor='none', markeredgewidth=1.5)
axs[1].plot(x2_2 * scale, y2_2, label=r"\boldmath$l_p/L=0.3$", color='black', linestyle='-', linewidth=1.0, marker='s', markersize=6, markeredgecolor='lime', markerfacecolor='none', markeredgewidth=1.5)
axs[1].plot(x3_2 * scale, y3_2, label=r"\boldmath$l_p/L=0.1$", color='black', linestyle='-', linewidth=1.0, marker='^', markersize=6, markeredgecolor='darkblue', markerfacecolor='none', markeredgewidth=1.5)
axs[1].plot(x4_2 * scale, y4_2, label=r"\boldmath$l_p/L=0.03$", color='black', linestyle='-', linewidth=1.0, marker='D', markersize=6, markeredgecolor='red', markerfacecolor='none', markeredgewidth=1.5)
axs[1].legend(loc='best', markerscale=1.5, fontsize=16)
axs[1].set_xlabel('\\boldmath$s/L$', fontsize=20)
axs[1].set_yticks([-0.8,-0.6,-0.4,-0.2,0,0.2,0.4,0.6,0.8,1.0])
axs[1].set_yticklabels(['\\boldmath$-0.8$', '\\boldmath$-0.6$','\\boldmath$-0.4$', '\\boldmath$-0.2$', '\\boldmath$0.0$', '\\boldmath$0.2$','\\boldmath$0.4$','\\boldmath$0.6$','\\boldmath$0.8$','\\boldmath$1.0$'], fontsize=16)
axs[1].set_xticks([0,0.2,0.4,0.6,0.8,1.0])
axs[1].set_xticklabels(['\\boldmath$0$', '\\boldmath$0.2$', '\\boldmath$0.4$', '\\boldmath$0.6$','\\boldmath$0.8$','\\boldmath$1.0$'], fontsize=16)

axs[0].minorticks_on()
axs[1].minorticks_on()
axs[0].tick_params(which='minor', length=4, width=1, colors='black', direction='in', top=True, right=True)
axs[0].tick_params(which='major', length=6, width=1, colors='black', direction='in', labelsize=14, top=True, right=True)
axs[1].tick_params(which='minor', length=4, width=1, colors='black', direction='in', top=True, right=True)
axs[1].tick_params(which='major', length=6, width=1, colors='black', direction='in', labelsize=14, top=True, right=True)

axs[0].set_xlim(0,1)
axs[1].set_xlim(0,1)

axs[0].set_title('\\boldmath$(a)$', fontsize=20)
axs[1].set_title('\\boldmath$(b)$', fontsize=20)

for ax in axs:
    for spine in ax.spines.values():
        spine.set_linewidth(2.2)

plt.tight_layout()
plt.savefig('Tangent_tangentcorrelation_M1_gamma10.pdf')

