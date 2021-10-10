import os,sys
from pprint import pprint

list_file_as_module=map(lambda y: y.replace('.py',''), filter(lambda x: x!='__init__.py', os.listdir('./dir_a')))
print()
__all__=list(list_file_as_module)
