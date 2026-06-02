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

x1, y1 = np.loadtxt('V1_M1_omega0.5_gamma10_avg_MSD_t.txt', unpack=True)
x3, y3 = np.loadtxt('V60_M1_omega0.5_gamma10_avg_MSD_t.txt', unpack=True)
#x4, y4 = np.loadtxt('V100_M1_omega0.5_gamma10_t30_avg_MSD_t.txt', unpack=True)


fig, ax = plt.subplots(figsize=(6, 5), constrained_layout=True)


#ax.plot(x4*0.001/42217.1599, y4/100**2, label=r"\boldmath$Pe=2.5\times10^6$", color='black', linestyle='-', linewidth=1.5, markersize=1.5, markeredgecolor='black', markerfacecolor='none')
ax.plot(x3*0.001/42217.1599, y3/100**2, label=r"\boldmath$Pe=6\times10^6$", color='red', linestyle='-.', linewidth=1.5, markersize=1.5, markeredgecolor='red', markerfacecolor='none')
ax.plot(x1*0.001/42217.1599, y1/100**2, label=r"\boldmath$Pe=10^5$", color='darkblue', linestyle='-',linewidth=1.5, markersize=2, markeredgecolor='darkblue', markerfacecolor='none')

ax.set_ylabel(r'\boldmath$\langle (\Delta r)^2 \rangle/L^2$', fontsize=16)
ax.set_xlabel(r'\boldmath$\Delta t/\tau$', fontsize=14)
ax.legend(loc='lower right', fontsize=14)

ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xticks([1e-7,1e-6,1e-5,1e-4,1e-3])
ax.set_yticks([1e-5,1e-4,1e-3, 1e-2, 1e-1])
ax.set_yticklabels([r'\boldmath$10^{-5}$',r'\boldmath$10^{-4}$', r'\boldmath$10^{-3}$', r'\boldmath$10^{-2}$', r'\boldmath$10^{-1}$'], fontsize=15)
ax.set_xticklabels([r'\boldmath$10^{-7}$', r'\boldmath$10^{-6}$', r'\boldmath$10^{-5}$', r'\boldmath$10^{-4}$',r'\boldmath$10^{-3}$'], fontsize=15)



xfit = x1 * 0.001 / 42217.1599
yfit = y1 / 100**2

mask = (xfit >= 1e-8) & (xfit <= 9*1e-8)

lx = np.log10(xfit[mask])
ly = np.log10(yfit[mask])

slope, intercept = np.polyfit(lx, ly, 1)

t = np.logspace(np.log10(xfit[mask].min()),
                np.log10(xfit[mask].max()), 100)

fit_line = 2.5*10**intercept * t**0.70

ax.plot(t, fit_line, color='black', linestyle='-', linewidth=1.2)

ax.text(0.1, 0.05,
        rf'\boldmath$\Delta t^{{0.7}}$',
        transform=ax.transAxes,
        fontsize=14)

print("Scaling exponent1 =", slope)


'''xfit = x1 * 0.001 / 42217.1599
yfit = y1 / 100**2

mask = (xfit >= 6*1e-6) & (xfit <= 2*1e-5)

lx = np.log10(xfit[mask])
ly = np.log10(yfit[mask])

slope, intercept = np.polyfit(lx, ly, 1)

t = np.logspace(np.log10(xfit[mask].min()),
                np.log10(xfit[mask].max()), 100)

fit_line = 0.8*10**intercept * t**slope

ax.plot(t, fit_line, color='black', linestyle='-', linewidth=1.2)

ax.text(0.8, 0.7,rf'\boldmath$\Delta t^{{{slope:.2f}}}$',transform=ax.transAxes,fontsize=14)

print("Scaling exponent2 =", slope)'''





'''xfit = x3 * 0.001 / 42217.1599
yfit = y3 / 100**2

mask = (xfit >= 2*1e-8) & (xfit <= 8*1e-8)

lx = np.log10(xfit[mask])
ly = np.log10(yfit[mask])

slope, intercept = np.polyfit(lx, ly, 1)

t = np.logspace(np.log10(xfit[mask].min()),
                np.log10(xfit[mask].max()), 100)

fit_line = 10**intercept * t**slope

ax.plot(t, fit_line, color='black', linestyle='-', linewidth=1.2)

ax.text(0.7, 0.6,
        rf'\boldmath$\Delta t^{{{slope:.2f}}}$',
        transform=ax.transAxes,
        fontsize=14)

print("Scaling exponent3 =", slope)'''



'''xfit = x3 * 0.001 / 42217.1599
yfit = y3 / 100**2

mask = (xfit >= 1e-6) & (xfit <= 3*1e-6)

lx = np.log10(xfit[mask])
ly = np.log10(yfit[mask])

slope, intercept = np.polyfit(lx, ly, 1)

t = np.logspace(np.log10(xfit[mask].min()),
                np.log10(xfit[mask].max()), 100)

fit_line = 10**intercept * t**slope

ax.plot(t, fit_line, color='black', linestyle='-', linewidth=1.2)

ax.text(0.7, 0.6,rf'\boldmath$\Delta t^{{{slope:.2f}}}$',transform=ax.transAxes,fontsize=14)

print("Scaling exponent3 =", slope)'''




xfit = x1 * 0.001 / 42217.1599
yfit = y1 / 100**2

mask = (xfit >= 1e-4) & (xfit <= 5*1e-4)

lx = np.log10(xfit[mask])
ly = np.log10(yfit[mask])

slope, intercept = np.polyfit(lx, ly, 1)

t = np.logspace(np.log10(xfit[mask].min()),
                np.log10(xfit[mask].max()), 100)

fit_line = 0.6*10**intercept * t**slope

ax.plot(t, fit_line, color='black', linestyle='-', linewidth=1.2)

ax.text(0.8, 0.7,
        rf'\boldmath$\Delta t^{{{slope:.2f}}}$',
        transform=ax.transAxes,
        fontsize=14)

print("Scaling exponent =", slope)


'''xfit = x2 * 0.001 / 42217.1599
yfit = y2 / 100**2

mask = (xfit >= 6*1e-6) & (xfit <= 5*1e-5)
#mask = (xfit >= 5*1e-3) & (xfit <= 1e-2)

lx = np.log10(xfit[mask])
ly = np.log10(yfit[mask])

slope, intercept = np.polyfit(lx, ly, 1)

t = np.logspace(np.log10(xfit[mask].min()),np.log10(xfit[mask].max()), 100)
#t = np.logspace(-5.7, -4.8, 100)

fit_line = 10**intercept * t**slope

ax.plot(t, fit_line, color='black', linestyle='-', linewidth=1.2)

ax.text(0.38, 0.5,
        rf'\boldmath$\Delta t^{{{slope:.2f}}}$',
        transform=ax.transAxes,
        fontsize=14)

print("Scaling exponent =", slope)'''




ax.minorticks_on()
ax.tick_params(which='both', length=4, width=1, colors='black', direction='in', labelsize=0)
ax.xaxis.set_minor_locator(LogLocator(base=10.0, subs='auto', numticks=10))
ax.yaxis.set_minor_locator(LogLocator(base=10.0, subs='auto', numticks=10))
ax.set_xlim(2*1e-8, 2*1e-3)
ax.set_ylim(5*1e-6, 2*1e-1)
#ax.set_title(r'\boldmath$(b)$', fontsize=20, verticalalignment='top')

x_subs = np.arange(2, 10)
ax.xaxis.set_minor_locator(LogLocator(base=10.0, subs=x_subs, numticks=40))
ax.yaxis.set_minor_locator(LogLocator(base=10.0, subs=x_subs, numticks=40))  
ax.tick_params(which='minor', length=4, width=1, colors='black', direction='in', labelsize=0, top=True, right=True)
ax.tick_params(which='major', length=6, width=1, colors='black', direction='in', labelsize=14, top=True, right=True)

border_width = 1.4
for spine in ax.spines.values():
    spine.set_linewidth(border_width)

# Save figure
plt.savefig('MSD_vs_t_M1_gamma10_omega0.5_L100_new.pdf', bbox_inches='tight')

