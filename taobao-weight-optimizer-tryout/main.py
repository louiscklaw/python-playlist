#!/usr/bin/env python3

import os,sys
from pprint import pprint
from functools import reduce
from math import ceil

actual_weight=[
3.04,
1.45,
0.14,
0.44,
0.6,
0.26,
0.11,
0.3,
0.1
  ]
len_actual_weight=len(actual_weight)
range_actual_weights=range(0,len_actual_weight)

comp_items=[8,7,6,5,4,3,2]

len_comp_item = len(comp_items)

items_weight_range=list(range(2,len_actual_weight+1))


def findRoundUp(int_in):
  return ceil(int_in)

def distanceToRoundUp(int_in):
  return round(findRoundUp(int_in)-int_in, 2)


def lookupWeight(list_idx):
  return list(map(lambda x: actual_weight[x], list_idx))

def getWeight(list_idx):
  return round(sum(lookupWeight(list_idx)), 2)

def findNearestRoundUp(master_list, list_in, min_index=0):

  output = []
  dist_to_round_up = list(map(lambda int_in: distanceToRoundUp(int_in), list_in))
  # print(temp)
  min_dist_to_round_up = sorted(set(dist_to_round_up))[min_index]
  # print(min_dist_to_round_up)

  temp = list(zip(master_list, dist_to_round_up))
  output = list(filter(lambda x: x[1] == min_dist_to_round_up, temp))
  return list(zip(*output))[0]


def secondList():
  output=[]
  for i in range_actual_weights:
    for ii in range_actual_weights:
      if (ii != i):
        if sorted([ii,i]) not in output:
          output.append(sorted([ii,i]))

  return output

def showCombine(countdown):
  list_combination=[]
  if countdown==2:
    return secondList()
  else:
    temp = countdown-1
    output = []
    for i in range_actual_weights:
      for ii in sorted(showCombine(temp)):
        if i not in ii:
          pre_add = sorted(ii+[i])
          if pre_add not in output:
            output.append(pre_add)

    return list(output)

def filterOutWithoutCompItems(list_combination, comp_items):
  output = []
  for combination in list_combination:
    all_comp_item_in_list = True
    for comp_item in comp_items:
      if comp_item not in combination:
        all_comp_item_in_list = False
    if all_comp_item_in_list:
      output.append(combination)

  return output


def printWithAllCompItems(list_in):

  lookup_weights = list(map(lambda x: lookupWeight(x), list_in))
  sub_total_weights=list(map(lambda x: getWeight(x), list_in))
  master_list = list(zip(list_in,lookup_weights, sub_total_weights))

  print('\n')
  print('-'*80)
  print("with all comp items {}".format(comp_items))
  print('close to the nearest integer weight is:')
  print('-'*80)

  print("nearest roundup")
  pprint(findNearestRoundUp(master_list, sub_total_weights))

  print("second nearest roundup")
  pprint(findNearestRoundUp(master_list, sub_total_weights, 1))

  print('third nearest roundup')
  pprint(findNearestRoundUp(master_list, sub_total_weights, 2))

def printWithoutCompItems(list_in):

  lookup_weights = list(map(lambda x: lookupWeight(x), list_in))
  sub_total_weights=list(map(lambda x: getWeight(x), list_in))
  master_list = list(zip(list_in,lookup_weights, sub_total_weights))

  print('\n')
  print('-'*80)
  print('without comp items')
  print('close to the nearest integer weight is:')
  print('-'*80)

  print("nearest roundup")
  pprint(findNearestRoundUp(master_list, sub_total_weights))

  print("second nearest roundup")
  pprint(findNearestRoundUp(master_list, sub_total_weights, 1))

  print('third nearest roundup')
  pprint(findNearestRoundUp(master_list, sub_total_weights, 2))

def main():

  all_combination=[]
  for i in items_weight_range:
    all_combination = all_combination+showCombine(i)

  # pprint(showCombine(2))
  # pprint(showCombine(3))
  # pprint(showCombine(4))

  list_with_comp_item=filterOutWithoutCompItems(all_combination, comp_items)


  printWithAllCompItems(list_with_comp_item)

  printWithoutCompItems(all_combination)

if __name__=='__main__':
  main()