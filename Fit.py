import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import maxwell


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
d1 = df[df['Temperature'] >= int(y)]
a = input('Second temperature')
d2 = d1[d1['Temperature'] <= int(a)]

colnames2 = list(d2.columns)
for i in colnames2:
    df[i] = (df[i] - df[i].min()) / (df[i].max() - df[i].min())
main = d2.plot(x='Temperature')
line = plt.axhline(y=0.5, color='black', linestyle='-')

plt.show()

maxwell = stats.maxwell

for column in d2.columns:
     params= maxwell.fit(d2.columns, floc=0)
     print(params)


