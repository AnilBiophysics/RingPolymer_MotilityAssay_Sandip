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

scale = 10 * (100**2)
x, y0, y2, y3, y4, y5, y6 = np.loadtxt('mode_vs_Pe.txt', unpack=True)

fig, ax = plt.subplots(figsize=(8.5,6))




ax.plot(x * scale, y5/50, marker='v', linestyle='-', markersize=8, markeredgecolor='brown', color='brown',label=r"\boldmath$k=5$")
ax.plot(x * scale, y4/50, marker='D', linestyle='-', markersize=8, markeredgecolor='green', color='green',label=r"\boldmath$k=4$")
ax.plot(x * scale, y3/50, marker='s', linestyle='-', markersize=8, markeredgecolor='red', color='red',label=r"\boldmath$k=3$")
ax.plot(x * scale, y2/50, marker='^', linestyle='-', markersize=8, markeredgecolor='orange', color='orange',label=r"\boldmath$k=2$")
ax.plot(x * scale, y0/50, marker='o', linestyle='-', markersize=8, markeredgecolor='blue', color='blue',label=r"\boldmath$k=0$")

#ax.plot(x * scale, y6/50, marker='P', linestyle='-', markersize=8,markerfacecolor='none', markeredgecolor='green', color='green',label=r"\boldmath$k=6$")


'''ax.plot(x * scale, y1, color='blue', linestyle='--', linewidth=2)
ax.plot(x * scale, y2, color='red', linestyle=':', linewidth=3)
ax.plot(x * scale, y3, color='green', linestyle='-', linewidth=2)'''

ax.set_xlabel(r'\boldmath$Pe$', fontsize=21, fontweight='bold')
ax.set_ylabel(r'\boldmath$\langle A_k\rangle/L $', fontsize=21, fontweight='bold')

ax.set_xticks([0, 0.2e7, 0.4e7,  0.6e7, 0.8e7,1.0e7,1.2e7,1.4e7])
ax.set_yticks([0.05,0.10,0.15,0.20,0.25])
ax.set_xticklabels([r'\boldmath$0$',  r'\boldmath$0.2$', r'\boldmath$0.4$', r'\boldmath$0.6$',  r'\boldmath$0.8$',r'\boldmath$1.0$',r'\boldmath$1.2$',r'\boldmath$1.2$'],fontsize=18)
ax.set_yticklabels([r'\boldmath$0.05$', r'\boldmath$0.10$', r'\boldmath$0.15$', r'\boldmath$0.20$',
                    r'\boldmath$0.25$'],
                   fontsize=18)

ax.tick_params(axis='both', which='major', length=8, width=2, direction='in', top=True, right=True)
ax.tick_params(axis='both', which='minor', length=4, width=1.5, direction='in', top=True, right=True)
ax.minorticks_on()

#ax.set_title(r"\boldmath{$(c)$}", fontsize=20)
ax.legend(fontsize=16,loc = 'center right')

ax.text(1.12, -0.04, r'\boldmath$(\times 10^7)$', transform=ax.transAxes,
        fontsize=18, fontweight='bold', ha='right')

for spine in ax.spines.values():
    spine.set_linewidth(1.6)

plt.tight_layout()
plt.savefig('ModeAmplitude_vs_pe_M1_gamma10_omega0.9_varyModes_L100.pdf')

