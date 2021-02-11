# %%
from IPython.core.magics.namespace import NamespaceMagics # Used to query namespace.
from IPython import get_ipython 
import os,sys
"""get_ipython().user_ns_hidden['NamespaceMagics'] = NamespaceMagics
get_ipython().user_ns_hidden['os'] = os
get_ipython().user_ns_hidden['sys'] = sys
get_ipython().user_ns_hidden['get_ipython'] = get_ipython()
"""
# %%
def printValues(namespaces):
    values = namespaces.who_ls()
    return values

def VariableExplorer(ipython = get_ipython()) :
    namespaces = NamespaceMagics()
    namespaces.shell = ipython.kernel.shell
    values = printValues(namespaces)
    sheet1 = dataSheet(values)
    return sheet1

import pandas as pd
import numpy as np
import ipysheet
from ipysheet import sheet, cell, column

def dataSheet(values):
    cnt = 0
    sheet1 = sheet(rows = len(values), columns = 4, column_headers=['Name', 'Type', 'Value', 'Size'])
    for item in values:
        cnt = cnt + 1 
        name = item
        type_of_item = type(item).__name__
        value = str(eval(item))
        size_of_item = sys.getsizeof(item)
        cell(cnt-1,0,name,read_only=True)
        cell(cnt-1,1,type_of_item,read_only=True)
        cell(cnt-1,2,value,read_only=True)
        cell(cnt-1,3,size_of_item,read_only=True)
    
    return sheet1
    
# %%
def main():
	VariableExplorer()
	
if __name__ == "__main__":
    main()

# %%
b = 5
c= 't'
# %%
