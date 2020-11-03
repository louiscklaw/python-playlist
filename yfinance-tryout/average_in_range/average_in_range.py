import pandas as pd
import numpy as np

def getMA(df, samples=10):
  df['SMA_'+str(samples)] = df.loc[:,'Close'].rolling(window=samples).mean()

hist = pd.read_json('./0027_dump.json')

# filling dividends
# eps = earn_per_share
dividend_and_eps = {
  '2015':[pd.NA,pd.NA],
  '2016':[0.44, 1.473],
  '2017':[0.74, 2.451],
  '2018':[0.95, 3.128],
  '2019':[0.91,3.0118]
}

def getPE(df_in):
  dividend_test = df_in
  return ('{:06.3f}%'.format(dividend_test['dividends']/dividend_test['Close'] * 100))

years = ['2015','2016','2017','2018','2019']

df_PEs = pd.DataFrame(pd.NA, index=years, columns=['mean','min','max','PE_by_mean','PE_by_min','PE_by_max'])

for year in years:
  earn_per_share = dividend_and_eps[year][1]
  dividend = dividend_and_eps[year][0]
  close_mean = hist['{}0101'.format(year):'{}1231'.format(year)].mean()['Close']
  close_min = hist['{}0101'.format(year):'{}1231'.format(year)].min()['Close']
  close_max = hist['{}0101'.format(year):'{}1231'.format(year)].max()['Close']
  df_PEs.loc[year,'mean'] = close_mean
  df_PEs.loc[year,'min'] = close_min
  df_PEs.loc[year,'max'] = close_max
  df_PEs.loc[year,'dividend'] = dividend
  df_PEs.loc[year,'eps'] = earn_per_share
  df_PEs.loc[year,'PE_by_mean'] = close_mean/earn_per_share
  df_PEs.loc[year,'PE_by_min'] = close_min/earn_per_share
  df_PEs.loc[year,'PE_by_max'] = close_max/earn_per_share

print(df_PEs)

print('mean_PEs')
print(df_PEs.mean())

print('getting projected stock price')
last_earn_per_share = df_PEs.iloc[-1]['eps']
print('last earn per share: {}'.format(last_earn_per_share))

# project stock price by PE_mean
df_PEs_result = pd.DataFrame(pd.NA, index=['result'], columns=[
  'project_stock_price_by_PE_mean',
  'project_stock_price_by_PE_min',
  'project_stock_price_by_PE_max',
])

df_PEs_result.loc['result','project_stock_price_by_PE_mean'] = last_earn_per_share * df_PEs.mean()['PE_by_mean']
df_PEs_result.loc['result','project_stock_price_by_PE_min'] = last_earn_per_share * df_PEs.mean()['PE_by_min']
df_PEs_result.loc['result','project_stock_price_by_PE_max'] = last_earn_per_share * df_PEs.mean()['PE_by_max']

print(df_PEs_result)

# change format before out

# import pandas as pd
# df = pd.DataFrame([123.4567, 234.5678, 345.6789, 456.7890],
#                   index=['foo','bar','baz','quux'],
#                   columns=['cost'])
