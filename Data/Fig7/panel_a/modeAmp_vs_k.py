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
x, y01 = np.loadtxt('modeAmp_vs_k_omega0.1.txt', unpack=True)
x, y02 = np.loadtxt('modeAmp_vs_k_omega0.5.txt', unpack=True)
x, y03 = np.loadtxt('modeAmp_vs_k_omega0.9.txt', unpack=True)

fig, ax = plt.subplots(figsize=(8.5,6))

ax.plot(x , y03/50, marker='D', color='magenta', linewidth=2, markersize=8, label=r"\boldmath$\Omega=0.9$")
ax.plot(x , y02/50, marker='s', color='red', linewidth=2, markersize=8, label=r"\boldmath$\Omega=0.5$")
ax.plot(x , y01/50, marker='o', color='blue', linewidth=2, markersize=8, label=r"\boldmath$\Omega=0.1$")


#ax.set_xscale('log')
#ax.set_yscale('log')
'''ax.plot(x * scale, y1, color='blue', linestyle='--', linewidth=2)
ax.plot(x * scale, y2, color='red', linestyle=':', linewidth=3)
ax.plot(x * scale, y3, color='magenta', linestyle='-', linewidth=2)'''

ax.set_xlabel(r'\boldmath$k$', fontsize=21, fontweight='bold')
ax.set_ylabel(r'\boldmath$\langle \sqrt(a_k^2+b_k^2) \rangle/L$', fontsize=21, fontweight='bold')

ax.set_xticks([2,3,4,5,6,7,8,9,10])
ax.set_yticks([0.02,0.04,0.06,0.08,0.10,0.12,0.14])
ax.set_xticklabels([r'\boldmath$2$',  r'\boldmath$3$', 
                    r'\boldmath$4$', r'\boldmath$5$',  r'\boldmath$6$',r'\boldmath$7$',r'\boldmath$8$',r'\boldmath$9$',r'\boldmath$10$'],
                   fontsize=18)
ax.set_yticklabels([r'\boldmath$0.02$', r'\boldmath$0.04$', r'\boldmath$0.06$', r'\boldmath$0.08$',
                    r'\boldmath$0.1$',r'\boldmath$0.12$',r'\boldmath$0.14$'],
                   fontsize=18)

ax.tick_params(axis='both', which='major', length=8, width=2, direction='in', top=True, right=True)
ax.tick_params(axis='both', which='minor', length=4, width=1.5, direction='in', top=True, right=True)
ax.minorticks_on()

ax.set_title(r"\boldmath{$(a)$}", fontsize=20)
ax.legend(fontsize=18)

#ax.text(1.1, -0.04, r'\boldmath$(\times 10^6)$', transform=ax.transAxes,
        #fontsize=18, fontweight='bold', ha='right')

for spine in ax.spines.values():
    spine.set_linewidth(2.5)
plt.ylim(0.0,0.08)
plt.tight_layout()
plt.savefig('ModeAmplitude_vs_m_M1_gamma10_varyOmega_v45.pdf')

