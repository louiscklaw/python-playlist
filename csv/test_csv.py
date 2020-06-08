#!/usr/bin/env python
# coding:utf-8

import os
import sys
import logging
import traceback
from pprint import pprint
import csv

ld_test = [
    {'col_a':'123'},
    {'col_a':'456'}

]
ld_contacts_raw=[{
                u'etag': u'%EgcBAj0JPjcuGgwBAgMEBQYHCAkKCwwiDGZ6dEFseEJyQXVZPQ==',
                u'names': [
                    {u'displayName': u'Notebook.battery',
                    u'displayNameLastFirst': u'Notebook.battery',
                    u'familyName': u'Notebook.battery',
                    u'metadata': {
                        u'primary': True,
                        u'source':
                        {u'id': u'd108b050ba47fa3',u'type': u'CONTACT'}

                        }
                    }
                ],
                u'resourceName': u'people/c941405175906860963'
    }]


ld_contacts_flattened=[]
l_test_simple=[]

def main1():
    with open('test.csv','r+') as test_csv:
        field_names = ['col_1','col_2']
        writer = csv.DictWriter(test_csv,field_names)
        # writer.writerows([{'col_1':'value1', 'col_2':'value2'}])
        writer.writerows([{'col_1':row_no, 'col_2':value } for (row_no, value) in d_test_simple.items()])


# output a list, a list that contains all nodes
def get_all_keys(d_object, current_node, list_of_all_nodes):
        if type(d_object) == type({}):
            for key in d_object.keys():
                get_all_keys(d_object[key], '/'.join([current_node,key]), list_of_all_nodes)

        elif type(d_object) == type([]):
            for l in d_object:
                get_all_keys(l, '/'.join([current_node]),list_of_all_nodes)

        else:
            return list_of_all_nodes.append(current_node)

def main():
    d_contacts_flattened={}
    # for d_contacts_raw in ld_contacts_raw:
        # pprint(type(d_contacts_raw['names'][0]['metadata']))
        # pprint(type(d_contacts_raw['names'][0]['displayName']))

    l_test=[]
    get_all_keys(ld_contacts_raw[0],'.',l_test)
    pprint(l_test)

if __name__ == '__main__':
    main()
