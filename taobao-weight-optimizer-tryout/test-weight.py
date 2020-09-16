#!/usr/bin/env python3

import os,sys
from pprint import pprint
from functools import reduce
from math import ceil

actual_weight=[
3.04,
1.45,
0.1,
1.15,
0.05,
0.22,
2.8,
0.57
  ]
weights=range(0,len(actual_weight))
items_weight_range=list(range(2,len(actual_weight)+1))

len_weights=len(weights)
range_len_weights = range(len_weights)

def findRoundUp(int_in):
  return ceil(int_in)

def distanceToRoundUp(int_in):
  return round(findRoundUp(int_in)-int_in, 2)

def findNearestRoundUp(master_list, list_in, min_index=0):

  output = []
  dist_to_round_up = list(map(lambda int_in: distanceToRoundUp(int_in), list_in))
  # print(temp)
  min_dist_to_round_up = sorted(set(dist_to_round_up))[min_index]
  # print(min_dist_to_round_up)

  temp = list(zip(master_list, dist_to_round_up))
  output = list(filter(lambda x: x[1] == min_dist_to_round_up, temp))
  return list(zip(*output))[0]

def getWeight(list_idx):
  return round(sum(lookupWeight(list_idx)), 2)

def lookupWeight(list_idx):
  return list(map(lambda x: actual_weight[x], list_idx))

def secondList():
  output=[]
  for i in range_len_weights:
    for ii in range_len_weights:
      if (ii != i):
        output.append([i,ii])
  return output

def showCombine(countdown):
  list_combination=[]
  if countdown==2:
    return secondList()
  else:
    temp = countdown-1
    output = []
    for i in range_len_weights:
      for ii in sorted(showCombine(temp)):
        if i not in ii:
          pre_add = sorted(ii+[i])
          # print('try pre_add {}'.format(pre_add))
          if pre_add not in list_combination:
            list_combination.append(pre_add)
            output.append(pre_add)

    return list(output)

all_combination=[]
for i in items_weight_range:
  all_combination = all_combination+showCombine(i)

lookup_weights = list(map(lambda x: lookupWeight(x), all_combination))
sub_total_weights=list(map(lambda x: getWeight(x), all_combination))

master_list = list(zip(all_combination,lookup_weights, sub_total_weights))

print('close to the nearest integer weight is:')
print('-'*80)

print("nearest roundup")
pprint(findNearestRoundUp(master_list, sub_total_weights))


print("second nearest roundup")
pprint(findNearestRoundUp(master_list, sub_total_weights, 1))

print('third nearest roundup')
pprint(findNearestRoundUp(master_list, sub_total_weights, 2))