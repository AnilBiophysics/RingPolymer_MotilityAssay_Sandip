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

scale = 10 * (50**2)
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
ax.plot(x * scale, y3, color='magenta', linestyle='-', linewidth=2)'''

ax.set_xlabel(r'\boldmath$Pe$', fontsize=21, fontweight='bold')
#ax.set_ylabel(r'\boldmath$\langle \sqrt(a_k^2+b_k^2)\rangle/L $', fontsize=21, fontweight='bold')
ax.set_ylabel(r'\boldmath$\langle A_k \rangle/L $', fontsize=21, fontweight='bold')

ax.set_xticks([0, 0.50e6, 1.0e6,  1.5e6, 2.0e6,2.5e6,3.0e6,3.5e6])
ax.set_yticks([0.02,0.04,0.06,0.08,0.10,0.12,0.14])
ax.set_xticklabels([r'\boldmath$0$',  r'\boldmath$0.5$', 
                    r'\boldmath$1.0$', r'\boldmath$1.5$',  r'\boldmath$2.0$',r'\boldmath$2.5$',r'\boldmath$3.0$',r'\boldmath$3.5$'],
                   fontsize=18)
ax.set_yticklabels([r'\boldmath$0.02$', r'\boldmath$0.04$', r'\boldmath$0.06$', r'\boldmath$0.08$',
                    r'\boldmath$0.1$',r'\boldmath$0.12$',r'\boldmath$0.14$'],
                   fontsize=18)

ax.tick_params(axis='both', which='major', length=8, width=2, direction='in', top=True, right=True)
ax.tick_params(axis='both', which='minor', length=4, width=1.5, direction='in', top=True, right=True)
ax.minorticks_on()

ax.set_title(r"\boldmath{$(b)$}", fontsize=20)
ax.legend(fontsize=18,loc = 'center right')

ax.text(1.12, -0.04, r'\boldmath$(\times 10^6)$', transform=ax.transAxes,
        fontsize=18, fontweight='bold', ha='right')

for spine in ax.spines.values():
    spine.set_linewidth(2.5)

plt.tight_layout()
plt.savefig('ModeAmplitude_vs_pe_M1_gamma10_omega0.9_varyModes.pdf')

