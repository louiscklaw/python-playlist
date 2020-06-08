#!/usr/bin/env python
# coding:utf-8

import os
import sys
import logging
import traceback
from pprint import pprint


D_QUESTION={
    0:[4,12],
    1:[2,2],
    2:[2,1],
    3:[1,1],
    4:[10,4]
}
no_of_item=5
k=0

def calculate_total(list_of_weight):
    total_weight=0
    total_price=0
    for key,value in list_of_weight.items():
        price, weight = value
        total_weight +=weight
        total_price += price

    return total_price, total_weight

def get_all_combination(number_of_length,number_selected, last_combination,accumulated_combination):
    global k
    if number_of_length>0:
        number_of_length-=1
        for i in range(0,no_of_item):
            current_combination = list(last_combination)
            if i not in last_combination:
                current_combination.append(i)
                get_all_combination(number_of_length, number_selected,current_combination, accumulated_combination)
    elif number_of_length ==0:
        accumulated_combination[(','.join(map(str,sorted(last_combination))))]=''
        last_combination=list()
    else:
        pass

def get_price_and_weight(list_items):
    total_price = 0
    total_weight = 0
    for i in list_items:
        price, weight=D_QUESTION[int(i)]
        total_price+=price
        total_weight+=weight
    return total_price, total_weight

def get_unique_combination(list_combination):
    d_unique = {}
    l_unique = []
    for combination in list_combination:
        s_temp =  ','.join(str(combination))
        if s_temp not in d_unique.keys():
            d_unique[s_temp]=''
            l_unique.append(combination)
    return l_unique

def try_solve(weight_total, combine_list, item_to_add):
    for i in range(0,len(D_QUESTION)):

        if weight_total >=15:
            return combine_list
        else:
            try_solve(current_weight, combine_list, item_to_add)


def main():
    from pprint import pprint
    combinations={}
    # get_combination(2,[],[], combination)

    for i in range(1,5):
        get_all_combination(i,0,[],combinations)

    d_price_and_weight = {}
    l_combination_meet_weight = []
    max_price_meet_weight = 0

    for combination in combinations.keys():
        price, weight = get_price_and_weight(combination.split(','))
        d_price_and_weight[combination] =[price,weight]

    print "under 15 kg"
    for combination in d_price_and_weight.keys():
        price, weight = d_price_and_weight[combination]
        print "combination %s, p:%d => w:%d" %(combination, price, weight)
        if weight <= 15:
            l_combination_meet_weight.append(combination)
            max_price_meet_weight = max(max_price_meet_weight, price)

    for combination in l_combination_meet_weight:
        price, weight = d_price_and_weight[combination]
        print "possible answer ",
        print "%s p:%d, w:%d" % (combination, price, weight)
        if price == max_price_meet_weight:
            print "%s p:%d, w:%d" % (combination, price, weight)


if __name__ == '__main__':
    main()
