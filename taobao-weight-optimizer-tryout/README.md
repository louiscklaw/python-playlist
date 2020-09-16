# README

### Question:
To find the nearest kg to save the travffic fee.

### Case:
given that the following items with their weight. find the combination of the items (e.g. 1,3,4,5) having the closest total weight (e.g. 7.9kg, 6.9kg ... etc) to make use the available weight and save the cost

### scripts:
test-weight-with-comp-item.py
```
./run.sh
+ pipenv run python3 test-weight-with-comp-item.py


--------------------------------------------------------------------------------
with all comp items [3, 5, 6, 7]
close to the nearest integer weight is:
--------------------------------------------------------------------------------
nearest roundup
(([0, 2, 3, 4, 5, 6, 7], [3.04, 0.1, 1.15, 0.05, 0.22, 2.8, 0.57], 7.93),)
second nearest roundup
(([2, 3, 4, 5, 6, 7], [0.1, 1.15, 0.05, 0.22, 2.8, 0.57], 4.89),)
third nearest roundup
(([0, 2, 3, 5, 6, 7], [3.04, 0.1, 1.15, 0.22, 2.8, 0.57], 7.88),)


--------------------------------------------------------------------------------
without comp items
close to the nearest integer weight is:
--------------------------------------------------------------------------------
nearest roundup
(([3, 4, 6], [1.15, 0.05, 2.8], 4.0),)
second nearest roundup
(([0, 3, 6], [3.04, 1.15, 2.8], 6.99),
 ([0, 2, 4, 6], [3.04, 0.1, 0.05, 2.8], 5.99),
 ([3, 4, 5, 7], [1.15, 0.05, 0.22, 0.57], 1.99))
third nearest roundup
(([0, 3, 5, 7], [3.04, 1.15, 0.22, 0.57], 4.98),
 ([0, 2, 4, 5, 7], [3.04, 0.1, 0.05, 0.22, 0.57], 3.98))
```
