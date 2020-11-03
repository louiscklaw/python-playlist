import pandas as pd
import numpy as np

product = {
  'day' : [1,2,3,4,5,6,7,8,9,10,11,12],
  'demand':[290,260,288,300,310,303,329,340,316,330,308,310]
  }

df = pd.DataFrame(product)

df['max_3'] = df.iloc[:,1].rolling(window=3).max()

print(df.tail())