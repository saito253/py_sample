#!/usr/bin/python3

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

plt.style.use('default')
sns.set()
sns.set_style('whitegrid')
sns.set_palette('Set1')

x = np.array([0, 2, 4, 6, 8, 10])
gene_1 = np.array([0.3, 1.2, 1.3, 1.8, 1.7, 1.5])
gene_2 = np.array([2.1, 2.4, 2.3, 2.1, 2.2, 2.1])
gene_3 = np.array([0.3, 0.6, 1.1, 1.8, 2.2, 2.8])

df = pd.DataFrame({
    'x': x, 'gene1': gene_1, 'gene2': gene_2, 'gene3': gene_3
})

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

ax.plot('x', 'gene1', data=df, label='gene 1', marker='o')
ax.plot('x', 'gene2', data=df, label='gene 3', marker='o')
ax.plot('x', 'gene3', data=df, label='gene 3', marker='o')

ax.legend()
ax.set_xlabel("time [hour]")
ax.set_ylabel("gene expression [log(TPM)]")
ax.set_ylim(0, 3)
plt.show()
