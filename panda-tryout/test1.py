#!/usr/bin/env python3

import numpy as np
import pandas as pd
import os,sys

from pprint import pprint

s = pd.Series([1,2,3,np.nan, 6,8])

pprint(s)

dates = pd.date_range('20130101', periods=6)

pprint(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))

pprint(df)

df2 = pd.DataFrame({'A': 1.,
  'B': pd.Timestamp('20130102'),
  'C': pd.Series(1, index=list(range(4)), dtype='float32'),
  'D': np.array([3] * 4, dtype='int32'),
  'E': pd.Categorical(["test", "train", "test", "train"]),
  'F': 'foo'})

pprint(df2)
pprint(df2.dtypes)


pprint(df.head())

pprint(df.tail(3))



pprint(df.index)

pprint(df.columns)


pprint(df.to_numpy())
pprint(df2.to_numpy())

pprint(df.describe())

pprint(df.T)

pprint(df.sort_index(axis=1, ascending=False))

pprint(df.sort_values(by='B'))

pprint(df['A'])

pprint(df[0:3])
pprint(df['20130102':'20130104'])

pprint(df.loc[dates[0]])

pprint(df.loc[:,['A','B']])

pprint(df.loc['20130102':'20130104',['A','B']])

pprint(df.loc['20130102',['A','B']])

pprint(df.loc[dates[0],'A'])

pprint(df.at[dates[0],'A'])

pprint(df.iloc[3])

pprint(df.iloc[3:4+1,0:1+1])

pprint(df.iloc[[1,2,4],[0,2]])

pprint(df.iloc[1:3,:])

pprint(df.iloc[:,1:2+1])

pprint(df.iloc[1,1])

pprint(df.iat[1,1])

print('Boolean indexing')
pprint(df[df['A']>0])


pprint(df[df > 0])

df2 = df.copy()
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']

pprint(df2)

pprint(df2[df2['E'].isin(['two', 'four'])])

print('setting')
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130102', periods=6))

df['F'] = s1
pprint(df)

df.at[dates[0],'A'] = 0
pprint(df)

df.iat[0,1] = 0
pprint(df)

df.loc[:,'D'] = np.array([5]*len(df))
pprint(df)

df2 = df.copy()
df2[df2 > 0] = -df2

pprint(df2)

print('Missing data')


df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
pprint(df1)

df1.loc[dates[0]:dates[1], 'E'] = 1
pprint(df1)

pprint(df1.dropna(how="any"))

pprint(df1.fillna(value=5))

pprint(pd.isna(df1))

print('Operations')

pprint(df.mean())

pprint(df.mean(1))

s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates).shift(2)
pprint(s)

# substraction
pprint(df.sub(s,axis='index'))

pprint(df.apply(np.cumsum))

pprint(df)
pprint(df.apply(lambda x: x.max()-x.min()))

s = pd.Series(np.random.randint(0, 7, size=10))
pprint(s)
pprint(s.value_counts())

print('String Methods')

s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, 'CABA', 'dog', 'cat'])
pprint(s)
pprint(s.str.lower())

print("merge")
df = pd.DataFrame(np.random.randn(10, 4))
pprint(df)

pieces = [df[:3], df[3:7], df[7:]]
pprint(pieces)
pprint(pd.concat(pieces))

print("Join")
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
pprint(left)

right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
pprint(right)
pprint(pd.merge(left, right, on='key'))



left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
pprint(left)
right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})
pprint(right)
pprint(pd.merge(left, right, on='key'))

print('Grouping')
df = pd.DataFrame({
  'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
  'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
  'C': np.random.randn(8),
  'D': np.random.randn(8)
  })
pprint(df)

pprint(df.groupby('A').sum())
pprint(df.groupby(['A', 'B']).sum())


print('Reshaping')
tuples = list(
  zip(
    *[['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
    ['one', 'two', 'one', 'two','one', 'two', 'one', 'two']])
  )

index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
df2 = df[:4]
# stacked => pivot table
stacked = df2.stack()
pprint(stacked)

pprint(stacked.unstack())
pprint(stacked.unstack(1))
pprint(stacked.unstack(0))


print('Pivot tables')
df = pd.DataFrame({
  'A': ['one', 'one', 'two', 'three'] * 3,
  'B': ['A', 'B', 'C'] * 4,
  'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
  'D': np.random.randn(12),
  'E': np.random.randn(12)})

pprint(df)

pprint(pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C']))

print('Time series')

rng = pd.date_range('1/1/2012', periods=100, freq='S')
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
pprint(ts.resample('5Min').sum())


rng = pd.date_range('3/6/2012 00:00', periods=5, freq='D')
ts = pd.Series(np.random.randn(len(rng)), rng)
pprint(ts)

ts_utc = ts.tz_localize('UTC')
pprint(ts_utc)
pprint(ts_utc.tz_convert('Asia/Hong_Kong'))


rng = pd.date_range('1/1/2012', periods=5, freq='M')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
pprint(ts)

ps = ts.to_period()
pprint(ps)

pprint(ps.to_timestamp())

prng = pd.period_range('1990Q1', '2000Q4', freq='Q-NOV')
pprint(prng)
ts = pd.Series(np.random.randn(len(prng)), prng)
ts.index = (prng.asfreq('M', 'e') + 1).asfreq('H', 's') + 9
pprint(ts.head())

print('Categoricals')
df = pd.DataFrame({
  "id": [1, 2, 3, 4, 5, 6],
  "raw_grade": ['a', 'b', 'b', 'a', 'a', 'e']
})
df["grade"] = df["raw_grade"].astype("category")
pprint(df["grade"])

df["grade"].cat.categories = ["very good", "good", "very bad"]

df["grade"] = df["grade"].cat.set_categories([
  "very bad", "bad", "medium", "good", "very good"
  ])

pprint(df["grade"])
pprint(df.sort_values(by="grade"))
pprint(df.groupby("grade").size())


print('Getting data in/out')
df.to_csv('foo.csv')

pprint(pd.read_csv('foo.csv'))

print('HDF5')
# df.to_hdf('foo.h5', 'df')
# pd.read_hdf('foo.h5', 'df')

print('excel')
df.to_excel('foo.xlsx', sheet_name='Sheet1')
pd.read_excel('foo.xlsx', 'Sheet1', index_col=None, na_values=['NA'])
