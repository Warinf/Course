import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import maxwell
import mplcursors

df = pd.read_excel('test1.xlsx', sheetname='test2')
d8=df
colnames = list(d8.columns)
print(colnames)
colnames.pop(0)
for i in colnames:

    d8[i]= (d8[i] - d8[i].min()) / (d8[i].max() - d8[i].min())



print(d8)
d8.plot(x='Temperature')
mplcursors.cursor()
plt.show()

y = input('First temperature')
d1 = df[df['Temperature'] >= int(y)]
a = input('Second temperature')
d2 = d1[d1['Temperature'] <= int(a)]

colnames2 = list(d2.columns)
colnames2.pop(0)
for col in colnames2:
    d2[col] = (d2[col] - d2[col].min()) / (d2[col].max() - d2[col].min())
main = d2.plot(x='Temperature')
line = plt.axhline(y=0.5, color='black', linestyle='-')
print(d2)
mplcursors.cursor()
plt.show()
c = input('Cutoff')
d3 = d2[d2['Temperature'] <= int(c)]
d4 = d3.set_index(['Temperature'])
d5 = d4- 0.5
d6 = d5.abs()
d7 = d6.idxmin()


print(d7)
d7.to_csv('Results.csv')
d7.plot(kind='bar')
plt.show()



