import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Set LaTeX and font properties
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

matrix = np.array([
    [0.1041340,0.10283220,0.10522148,0.104529244,0.103648411,0.10475482,0.10575706,0.106237361,0.106054038],
    [0.10160159,0.1079027,0.10579448,0.10547039,0.10992159,0.11386774,0.12357885,0.12507083,0.14069993],
    [0.10526012,0.1037989,0.111438815,0.130744353,0.152403163,0.188165420,0.22904223,0.27905068,0.32377353],
    [0.105494615,0.11097182,0.123740930,0.162210121,0.20219917,0.261754786,0.3269182721,0.38224892,0.420238690],
    [0.10369223,0.110416863,0.13683562,0.17253872,0.23743766,0.314504682,0.369116928,0.40706773,0.44477084],
    [0.10458413,0.11389519,0.14556578,0.19232216,0.265566331,0.326576667,0.365803320,0.38965077,0.41993119],
    [0.10693714,0.11508904,0.151435687,0.201449631,0.25934982,0.315666911,0.351076482,0.36106051,0.37145824],
    [0.10632600,0.112768043,0.15354307,0.20122187,0.24286292,0.28529175,0.317257640,0.31537012,0.30441763],
    [0.10620408,0.11732535,0.14940874,0.19589638,0.234776486,0.26337397,0.271076978,0.2696915,0.252782309],
    [0.10701565,0.11823208,0.14963286,0.1832577,0.21514186,0.227583362,0.21861009,0.22211359,0.21109373],
    [0.10620336,0.12338510,0.15154199,0.18606592,0.19214363,0.19504296,0.190002355,0.187315028,0.1888983],
    [0.10711304,0.11737984,0.14587005,0.16388138,0.17569861,0.17512257,0.172704888,0.170817805,0.18966941],
    [0.10740908,0.11950296,0.14082420,0.14972934,0.15573669,0.15312728,0.16182839,0.17022733,0.2011714],
    [0.104320322,0.122954160,0.13778230,0.14746470,0.15053390,0.14841951,0.16344187,0.177686006,0.223206910],
    [0.108698255,0.118307961,0.13242573,0.13846250,0.14212185,0.14855720,0.16717870,0.195154332,0.23851756],
    [ 0.10754112,0.121055179,0.12929877,0.12976378,0.13413973,0.14679703,0.17471347,0.217530136,0.257874695]
])


low_threshold = 0.14       
medium_threshold = 0.25  


custom_cmap = LinearSegmentedColormap.from_list("custom_cmap", ["#FFCCCC", "#87CEEB", "#4682B4", "#00008B"])
matrix_normalized = matrix 
#matrix_normalized = np.clip(matrix_normalized, 0, 1)

fig, ax = plt.subplots(figsize=(8.5, 6.5))
im = ax.imshow(matrix_normalized, cmap=custom_cmap, interpolation="bicubic", aspect="auto")

for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        value = matrix[i, j]
        if value < low_threshold:
            ax.scatter(j, i, marker='o', facecolor='none', edgecolor='red', s=60, linewidths=2.2, label="Isotropic" if (i == 0 and j == 0) else "")
        elif low_threshold <= value < medium_threshold:
            ax.scatter(j, i, marker='s', facecolor='none', edgecolor='blue', s=60, linewidths=2.2, label="Moderate" if (i == 0 and j == 1) else "")
        else:
            ax.scatter(j, i, marker='D', facecolor='none', edgecolor='yellow', s=60, linewidths=2.2, label="Anisotropic" if (i == 0 and j == 2) else "")


cbar = plt.colorbar(im, ax=ax)
#cbar.set_label('\\boldmath$\\langle \psi_N^2 \\rangle$', fontsize=20)

tick_positions = [0.15,0.20,0.25,0.30,0.35,0.40]
cbar.set_ticks(tick_positions)
cbar.set_ticklabels([f'\\boldmath{{$%.2f$}}' % tick for tick in tick_positions])
cbar.ax.tick_params(labelsize=16)
cbar.set_label('\\boldmath$\langle A \\rangle$', fontsize=18, labelpad=10)

yticks = [0, 1.25, 3.75, 6.25, 8.75, 11.25, 13.75, 16.25, 18.75, 21.25, 23.75,26.25,28.75,31.25,33.75,36.25]
xticks = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6,0.7,0.8,0.9]

ax.set_xticks(np.arange(len(xticks)))
#ax.set_yticks(np.arange(len(yticks)))
ax.set_yticks(np.arange(len(yticks)))

# Show labels only on alternate ticks
ytick_labels = [
    '\\boldmath{$%.1f$}' % tick if i % 2 == 0 else ''   # label only for even indices
    for i, tick in enumerate(yticks)
]

ax.set_yticklabels(ytick_labels, fontsize=18)


ax.set_xticklabels(['\\boldmath{$%.1f$}' % tick for tick in xticks], fontsize=18)
#ax.set_yticklabels(['\\boldmath{$%.1f$}' % tick for tick in yticks], fontsize=18)
ax.set_title(r"\boldmath{$(a)$}", fontsize=20)

plt.xlabel('\\boldmath$\Omega$', fontsize=21, fontweight='bold')
plt.ylabel('\\boldmath$Pe$', fontsize=21, fontweight='bold')

ax.invert_yaxis()

handles, labels = ax.get_legend_handles_labels()
unique_handles_labels = list(dict(zip(labels, handles)).items())  # Remove duplicates
#ax.legend([h for l, h in unique_handles_labels], [l for l, h in unique_handles_labels], fontsize=14, loc="upper right")


#plt.ylim(-0.5, 4.5)
plt.tight_layout()
plt.text(-1.4, 16.0, '\\boldmath$(\\times 10^5)$', fontsize=16, fontweight='bold')
plt.savefig("Phase_diagram_asphericity_M1_t2_gamma10.pdf")

