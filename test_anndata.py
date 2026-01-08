import numpy as np
import pandas as pd
import anndata as ad
from scipy.sparse import csr_matrix
import matplotlib.pyplot as plt

counts = csr_matrix(np.random.poisson(2, size=(1000, 1000)), dtype=np.float32)
adata = ad.AnnData(counts)


ct = np.random.choice(["B","T","Monocyte"], size=(adata.n_obs))
adata.obs["cell_type"] = pd.Categorical(ct)

ct = np.random.choice(range(0,100), size=(adata.n_obs))
adata.obs["x"] = pd.Categorical(ct)

ct = np.random.choice(range(0,100), size=(adata.n_obs))
adata.obs["y"] = pd.Categorical(ct)

#print(adata.obs)



#print(adata[adata.obs.cell_type == "B"].obs)

#a = adata.obs["cell_type"][1]
#print(a)



# Monocytes
bdata = adata[adata.obs.cell_type == "Monocyte"]

y_B = np.array([])
x_B = np.array([])

for cell in bdata:
    y_B = np.append(y_B, cell.obs.y.iloc[0])
    x_B = np.append(x_B, cell.obs.x.iloc[0])
plt.scatter(x_B,y_B)


plt.savefig("anndata")