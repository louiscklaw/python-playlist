#!/usr/bin/env python3

import os,sys
from pprint import pprint
import re

CSV_OUT=[]

i = 0

with open('./DW11.csv','r+',encoding="utf-16-le") as f:
  temp = f.readlines()
  for row in temp:
    # print(row)
    i+=1
    # print(len(row.split('\t')))

    if i == 1:
      cleared_cell = ['"id"']
    else:
      cleared_cell = [str(i)]

    
    temp_cell = ''
    for cell in row.split('\t'):
      try:
        temp_cell = re.findall('"[\S| ]+"', cell.strip())[0]
      except Exception as e:
        print(cell)
        break

      temp_cell = temp_cell.replace(' ','_')
      temp_cell = temp_cell.replace('_*"','"')
      temp_cell = temp_cell.replace('_*"','"')
      temp_cell = temp_cell.replace('._','_')
      temp_cell = temp_cell.replace('**"','"')
      temp_cell = temp_cell.replace('^"','"')
      temp_cell = temp_cell.replace('(%)','Pct')
      temp_cell = temp_cell.replace('%','Pct')
      temp_cell = temp_cell.replace('/','_')
      for j in range(1, 10):
        temp_cell = temp_cell.replace('__','_')
        temp_cell = temp_cell.replace('_"','"')
      

      
      cleared_cell.append(temp_cell)
      # pprint(cleared_cell)
    
    if (len(cleared_cell) == 30):
      CSV_OUT.append(','.join(cleared_cell))    

    
    if i > 9999:
      # break
      pass

# pprint(CSV_OUT)

with open('./DW11_out.csv','r+') as fo:
  fo.truncate(0)
  fo.write('\n'.join(CSV_OUT))
