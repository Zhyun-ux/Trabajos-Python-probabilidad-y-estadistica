import numpy as np
import scipy.stats as stats

n=12
sigma_x=1.7
sigma_x2= sigma_x**2

np.random.seed(42)
muestra= np.random.normal(loc=0,scale=sigma_x,size=n)

X_bar=np.mean(muestra)

S2_X=np.var(muestra,ddof=1)

S_x= np.sqrt(S2_X)

chi2_valor=(n-1)* S2_X /sigma_x2
probabilidad = stats.chi2.cdf(chi2_valor,df=n-1)

print(f"varianza muestral: {S2_X:.4f}")
print(f"Desviacion  tipica muestral: {S_x:.4f}")
print(f"Probabilidad P(S_X < 2.5):{probabilidad:.4f}")