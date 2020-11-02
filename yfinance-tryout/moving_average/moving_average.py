import pandas as pd
import numpy as np

product = {
  'month' : [1,2,3,4,5,6,7,8,9,10,11,12],
  'demand':[290,260,288,300,310,303,329,340,316,330,308,310]
  }

df = pd.DataFrame(product)

print(df.head())

for i in range(0,df.shape[0]-2):
    df.loc[df.index[i+2],'SMA_3'] = np.round(((df.iloc[i,1]+ df.iloc[i+1,1] +df.iloc[i+2,1])/3),1)

df['pandas_SMA_3'] = df.iloc[:,1].rolling(window=3).mean()

for i in [3,4,5,6,7,8]:
    df['pandas_SMA_'+str(i)] = df.iloc[:,1].rolling(window=i).mean()

print(df.head())


import matplotlib.pyplot as plt

plt.figure(figsize=[15,10])
plt.grid(True)
plt.plot(df['demand'],label='data')
for i in [3,4,5,6,7,8]:
    plt.plot(df['pandas_SMA_'+str(i)],label='SMA 3 Months')
plt.legend(loc=2)
