import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import maxwell


df = pd.read_csv('test.csv', header=0, sep=',')

colnames = list(df.columns)
print(colnames)
colnames.pop(0)
for i in colnames:
    df[i] = (df[i] - df[i].min()) / (df[i].max() - df[i].min())


print(df)
df.plot(x='Temperature')
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

plt.show()
d3 = d2.set_index(['Temperature'])
d4 = d3 - 0.5
d5 = d4.abs()
d6 = d5.idxmin()

print(d6)
d6.to_csv('Results.csv')
d6.plot(kind='bar')
plt.show()
