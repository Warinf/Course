import pandas as pd
import matplotlib.pyplot as plt
import numpy as py

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

df = pd.read_csv('test.csv', header=0, sep=',' )

colnames = list(df.columns)
print(colnames)
colnames.pop(0)
for i in colnames:

    df[i]= (df[i] - df[i].min()) / (df[i].max() - df[i].min())



print(df)
df.plot(x='Temperature')
plt.show()

y = input('Enter temperature')
d1 = df[:int(y)]

melt = pd.melt(d1, id_vars=["Temperature"], var_name="Exp", value_name="Intensity")
print(melt)

un=melt['Intensity']

x = 0.5
print(melt.ix[(melt.Intensity-x).abs().argsort()[:1]])

