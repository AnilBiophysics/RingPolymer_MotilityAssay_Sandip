import numpy as np
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D, HandlerTuple
from matplotlib.ticker import FormatStrFormatter
from matplotlib.ticker import LogLocator


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

x1_0, y1_0 = np.loadtxt('V1_M1_omega0.1_gamma10_avg_MSD_t.txt', unpack=True)
x2_0, y2_0 = np.loadtxt('V24_M1_omega0.1_gamma10_avg_MSD_t.txt', unpack=True)
x3_0, y3_0 = np.loadtxt('V60_M1_omega0.1_gamma10_avg_MSD_t.txt', unpack=True)
#x4_0, y4_0 = np.loadtxt('V100_M1_omega0.1_gamma10_avg_MSD_t.txt', unpack=True)

x1_1, y1_1 = np.loadtxt('V1_M1_omega0.5_gamma10_avg_MSD_t.txt', unpack=True)
x2_1, y2_1 = np.loadtxt('V24_M1_omega0.5_gamma10_avg_MSD_t.txt', unpack=True)
x3_1, y3_1 = np.loadtxt('V60_M1_omega0.5_gamma10_avg_MSD_t.txt', unpack=True)
#x4_1, y4_1 = np.loadtxt('V100_M1_omega0.5_gamma10_avg_MSD_t.txt', unpack=True)


x1_2, y1_2 = np.loadtxt('V1_M1_omega0.9_gamma10_avg_MSD_t.txt', unpack=True)
x2_2, y2_2 = np.loadtxt('V24_M1_omega0.9_gamma10_avg_MSD_t.txt', unpack=True)
x3_2, y3_2 = np.loadtxt('V60_M1_omega0.9_gamma10_avg_MSD_t.txt', unpack=True)
#x4_2, y4_2 = np.loadtxt('V100_M1_omega0.9_gamma10_avg_MSD_t.txt', unpack=True)

line_colors = ['orange', 'black', '#2ca02c']

fig, axs = plt.subplots(1, 3, figsize=(20, 7))
scale = 0.001/5277.144


axs[0].plot(x3_0*scale, (y3_0/49**2), label=r"\boldmath$Pe=14.4\times10^5$", color='red', linestyle=':', linewidth=2.0, markersize=1.5, markeredgecolor='red', markerfacecolor='none')
axs[0].plot(x2_0*scale, (y2_0/49**2), label=r"\boldmath$Pe=57.6\times10^4$", color='darkblue', linestyle='-.',linewidth=2.0, markersize=2, markeredgecolor='green', markerfacecolor='none')
axs[0].plot(x1_0*scale, (y1_0/49**2), label=r"\boldmath$Pe=2.4\times10^4$", color='green', linestyle='-',linewidth=2.0, markersize=2, markeredgecolor='darkblue', markerfacecolor='none')



axs[0].set_xscale('log')
axs[0].set_yscale('log')

axs[0].legend(loc='best', markerscale=1.5, fontsize=18)

axs[0].set_xlabel('\\boldmath$\\Delta t/\\tau$', fontsize=20)
axs[0].set_ylabel('\\boldmath $\\langle \\Delta r_{tot}^2 \\rangle/L^2$', fontsize=20)
axs[0].text(0.7, 0.2, '\\textbf{(a)}', transform=axs[0].transAxes, fontsize=20, verticalalignment='top')
axs[0].set_yticks([1e-5,1e-4, 1e-3, 1e-2, 1e-1, 1e0])
axs[0].set_yticklabels(['\\boldmath$10^{-5}$','\\boldmath$10^{-4}$', '\\boldmath$10^{-3}$', '\\boldmath$10^{-2}$', '\\boldmath$10^{-1}$', '\\boldmath$10^{0}$'], fontsize=14)
axs[0].set_xticks([1e-6, 1e-5, 1e-4, 1e-3, 1e-2])
axs[0].set_xticklabels(['\\boldmath$10^{-6}$', '\\boldmath$10^{-5}$', '\\boldmath$10^{-4}$', '\\boldmath$10^{-3}$', '\\boldmath$10^{-2}$'], fontsize=14)
axs[0].minorticks_on()
axs[0].tick_params(which='minor', length=4, width=1, colors='black', direction='in', labelsize=0)


t = np.logspace(-7.2, -6, 100)
y = 3*t**0.75 
coeffs = np.polyfit(np.log10(t), np.log10(y), 1)
slope, intercept = coeffs
fit_line = 10**intercept * t**slope
axs[0].plot(t, fit_line, color='black', linestyle='-', label=f'Fitted Line\n$y={slope:.2f}x + {intercept:.2f}$')

t = np.logspace(-3.6, -3, 100)
y = 15*t**1 
coeffs = np.polyfit(np.log10(t), np.log10(y), 1)
slope, intercept = coeffs
fit_line = 10**intercept * t**slope
axs[0].plot(t, fit_line, color='black', linestyle='-', label=f'Fitted Line\n$y={slope:.2f}x + {intercept:.2f}$')

t = np.logspace(-5, -4.6, 100)
y = 50000000*t**2 
coeffs = np.polyfit(np.log10(t), np.log10(y), 1)
slope, intercept = coeffs
fit_line = 10**intercept * t**slope
axs[0].plot(t, fit_line, color='black', linestyle='-', label=f'Fitted Line\n$y={slope:.2f}x + {intercept:.2f}$')

axs[0].text(0.04, 0.28, '\\boldmath$\\Delta t^{3/4}$', transform=axs[0].transAxes, fontsize=20, verticalalignment='top')
axs[0].text(0.72, 0.6, '\\boldmath$\\Delta t^1$', transform=axs[0].transAxes, fontsize=20, verticalalignment='top')
axs[0].text(0.3, 0.7, '\\boldmath$\\Delta t^{2}$', transform=axs[0].transAxes, fontsize=20, verticalalignment='top')

axs[0].xaxis.set_minor_locator(LogLocator(base=10.0, subs='auto', numticks=10))
axs[0].yaxis.set_minor_locator(LogLocator(base=10.0, subs='auto', numticks=10))


axs[1].plot(x3_1*scale, y3_1/49**2, label=r"\boldmath$Pe=14.4\times10^5$", color='red', linestyle=':', linewidth=2.0, markersize=1.5, markeredgecolor='red', markerfacecolor='none')
axs[1].plot(x2_1*scale, y2_1/49**2, label=r"\boldmath$Pe=57.6\times10^4$", color='darkblue', linestyle='-',linewidth=2.0, markersize=2, markeredgecolor='green', markerfacecolor='none')
axs[1].plot(x1_1*scale, y1_1/49**2, label=r"\boldmath$Pe=2.4\times10^4$", color='green', linestyle='-',linewidth=2.0, markersize=2, markeredgecolor='darkblue', markerfacecolor='none')

axs[1].set_xscale('log')
axs[1].set_yscale('log')

axs[1].legend(loc='best', markerscale=1.5, fontsize=18)
axs[1].set_xlabel('\\boldmath$\\Delta t/\\tau$', fontsize=20)
#axs[1].set_ylabel('\\boldmath $\langle \\tilde{v}^4 \\rangle$', fontsize=20)
#axs[1].text(0.7, 0.2, '\\textbf{(b)}', transform=axs[1].transAxes, fontsize=20, verticalalignment='top')
axs[1].set_yticks([1e-5,1e-4, 1e-3, 1e-2, 1e-1, 1e0])
axs[1].set_yticklabels(['\\boldmath$10^{-5}$','\\boldmath$10^{-4}$', '\\boldmath$10^{-3}$', '\\boldmath$10^{-2}$', '\\boldmath$10^{-1}$', '\\boldmath$10^{0}$'], fontsize=14)
axs[1].set_xticks([1e-6, 1e-5, 1e-4, 1e-3, 1e-2])
axs[1].set_xticklabels(['\\boldmath$10^{-6}$', '\\boldmath$10^{-5}$', '\\boldmath$10^{-4}$', '\\boldmath$10^{-3}$', '\\boldmath$10^{-2}$'], fontsize=14)

t = np.logspace(-5.7, -5, 100)
y = 4*t**0.75 
coeffs = np.polyfit(np.log10(t), np.log10(y), 1)
slope, intercept = coeffs
fit_line = 10**intercept * t**slope
axs[1].plot(t, fit_line, color='black', linestyle='-', label=f'Fitted Line\n$y={slope:.2f}x + {intercept:.2f}$')

t = np.logspace(-3.8, -3, 100)
y = 30*t**1.1 
coeffs = np.polyfit(np.log10(t), np.log10(y), 1)
slope, intercept = coeffs
fit_line = 10**intercept * t**slope
axs[1].plot(t, fit_line, color='black', linestyle='-', label=f'Fitted Line\n$y={slope:.2f}x + {intercept:.2f}$')

t = np.logspace(-5, -4.6, 100)
y = 50000000*t**2 
coeffs = np.polyfit(np.log10(t), np.log10(y), 1)
slope, intercept = coeffs
fit_line = 10**intercept * t**slope
axs[1].plot(t, fit_line, color='black', linestyle='-', label=f'Fitted Line\n$y={slope:.2f}x + {intercept:.2f}$')

axs[1].text(0.3, 0.22, '\\boldmath$\\Delta t^{3/4}$', transform=axs[1].transAxes, fontsize=20, verticalalignment='top')
axs[1].text(0.7, 0.5, '\\boldmath$\\Delta t^{1.1}$', transform=axs[1].transAxes, fontsize=20, verticalalignment='top')
axs[1].text(0.26, 0.7, '\\boldmath$\\Delta t^{2}$', transform=axs[1].transAxes, fontsize=20, verticalalignment='top')


axs[2].plot(x3_2*scale, y3_2/49**2, label=r"\boldmath$Pe=14.4\times10^5$", color='red', linestyle=':', linewidth=2.0, markersize=1.5, markeredgecolor='red', markerfacecolor='none')
axs[2].plot(x2_2*scale, y2_2/49**2, label=r"\boldmath$Pe=57.6\times10^4$", color='darkblue', linestyle='-.',linewidth=2.0, markersize=2, markeredgecolor='green', markerfacecolor='none')
axs[2].plot(x1_2*scale, y1_2/49**2, label=r"\boldmath$Pe=2.4\times10^4$", color='green', linestyle='-',linewidth=2.0, markersize=2, markeredgecolor='darkblue', markerfacecolor='none')

axs[2].set_xscale('log')
axs[2].set_yscale('log')

axs[2].legend(loc='best', markerscale=1.5, fontsize=18)
axs[2].set_xlabel('\\boldmath$\\Delta t/\\tau$', fontsize=20)
#axs[1].set_ylabel('\\boldmath $\langle \\tilde{v}^4 \\rangle$', fontsize=20)
#axs[2].text(0.7, 0.2, '\\textbf{(c)}', transform=axs[2].transAxes, fontsize=20, verticalalignment='top')
axs[2].set_yticks([1e-5,1e-4, 1e-3, 1e-2, 1e-1, 1e0])
axs[2].set_yticklabels(['\\boldmath$10^{-5}$','\\boldmath$10^{-4}$', '\\boldmath$10^{-3}$', '\\boldmath$10^{-2}$', '\\boldmath$10^{-1}$', '\\boldmath$10^{0}$'], fontsize=14)
axs[2].set_xticks([1e-6, 1e-5, 1e-4, 1e-3, 1e-2])
axs[2].set_xticklabels(['\\boldmath$10^{-6}$', '\\boldmath$10^{-5}$', '\\boldmath$10^{-4}$', '\\boldmath$10^{-3}$', '\\boldmath$10^{-2}$'], fontsize=14)
t = np.logspace(-5.7, -5, 100)
y = 4*t**0.75 
coeffs = np.polyfit(np.log10(t), np.log10(y), 1)
slope, intercept = coeffs
fit_line = 10**intercept * t**slope
axs[2].plot(t, fit_line, color='black', linestyle='-', label=f'Fitted Line\n$y={slope:.2f}x + {intercept:.2f}$')

t = np.logspace(-3.8, -3, 100)
y = 30*t**1.1 
coeffs = np.polyfit(np.log10(t), np.log10(y), 1)
slope, intercept = coeffs
fit_line = 10**intercept * t**slope
axs[2].plot(t, fit_line, color='black', linestyle='-', label=f'Fitted Line\n$y={slope:.2f}x + {intercept:.2f}$')

t = np.logspace(-5.3, -4.8, 100)
y = 70000000*t**2 
coeffs = np.polyfit(np.log10(t), np.log10(y), 1)
slope, intercept = coeffs
fit_line = 10**intercept * t**slope
axs[2].plot(t, fit_line, color='black', linestyle='-', label=f'Fitted Line\n$y={slope:.2f}x + {intercept:.2f}$')

axs[2].text(0.3, 0.22, '\\boldmath$\\Delta t^{3/4}$', transform=axs[2].transAxes, fontsize=20, verticalalignment='top')
axs[2].text(0.7, 0.5, '\\boldmath$\\Delta t^{1.1}$', transform=axs[2].transAxes, fontsize=20, verticalalignment='top')
axs[2].text(0.19, 0.6, '\\boldmath$\\Delta t^{2}$', transform=axs[2].transAxes, fontsize=20, verticalalignment='top')

x_subs = np.arange(2, 10)
axs[0].xaxis.set_minor_locator(LogLocator(base=10.0, subs=x_subs, numticks=40))
axs[0].yaxis.set_minor_locator(LogLocator(base=10.0, subs=x_subs, numticks=40))  
axs[0].tick_params(which='minor', length=4, width=1, colors='black', direction='in', labelsize=0, top=True, right=True)
axs[0].tick_params(which='major', length=6, width=1, colors='black', direction='in', labelsize=14, top=True, right=True)

axs[1].xaxis.set_minor_locator(LogLocator(base=10.0, subs=x_subs, numticks=40))
axs[1].yaxis.set_minor_locator(LogLocator(base=10.0, subs=x_subs, numticks=40))  
axs[1].tick_params(which='minor', length=4, width=1, colors='black', direction='in', labelsize=0, top=True, right=True)
axs[1].tick_params(which='major', length=6, width=1, colors='black', direction='in', labelsize=14, top=True, right=True)

axs[2].xaxis.set_minor_locator(LogLocator(base=10.0, subs=x_subs, numticks=40))
axs[2].yaxis.set_minor_locator(LogLocator(base=10.0, subs=x_subs, numticks=40))  
axs[2].tick_params(which='minor', length=4, width=1, colors='black', direction='in', labelsize=0, top=True, right=True)
axs[2].tick_params(which='major', length=6, width=1, colors='black', direction='in', labelsize=14, top=True, right=True)


axs[0].set_xlim(1.5*1e-7, 2*1e-2)
axs[0].set_ylim(1.5*1e-5,8*1e-1)
axs[1].set_xlim(1.5*1e-7, 2*1e-2)
axs[2].set_xlim(1.5*1e-7, 2*1e-2)

axs[0].set_title('\\boldmath$(a)$',fontsize=20)
axs[1].set_title('\\boldmath$(b)$',fontsize=20)
axs[2].set_title('\\boldmath$(c)$',fontsize=20)

for ax in axs:
	for spine in ax.spines.values():
		spine.set_linewidth(2.2)


plt.tight_layout()
plt.savefig('MSD_vs_t_M1_varyOmega.pdf')

