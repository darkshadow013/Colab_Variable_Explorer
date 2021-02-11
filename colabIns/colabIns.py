# %%
from IPython.core.magics.namespace import NamespaceMagics # Used to query namespace.
from IPython import get_ipython 
import os,sys
from ipywidgets import widgets
import pandas as pd
import numpy as np
import ipysheet
from ipysheet import sheet, cell, column
from ipywidgets import  Layout, Textarea

get_ipython().user_ns_hidden['NamespaceMagics'] = NamespaceMagics
get_ipython().user_ns_hidden['os'] = os
get_ipython().user_ns_hidden['sys'] = sys
get_ipython().user_ns_hidden['get_ipython'] = get_ipython()

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

def dataSheet(values):
    cnt = 0
    sheet1 = sheet(columns = 4, column_headers=['Name', 'Type', 'Size', 'Value'])
    l = Layout(flex='0 1 auto', height='40px', min_height='40px', width='auto')
    for item in values:
        name = item
        type_of_item = str(type(eval(item)))
        function = "function"
        module = "module"
        if(str(type_of_item) == function or (str(type_of_item) == module)):
            continue
        cnt = cnt + 1 
        value = str(eval(item))
        size_of_item = int(sys.getsizeof(item))
        textarea = Textarea(value=value, layout=l)
        cell(cnt-1,0,name,read_only=True,font_weight='bold')
        cell(cnt-1,1,type_of_item,read_only=True)
        cell(cnt-1,2,size_of_item,read_only=True,numeric_format='0')
        cell(cnt-1,3,value = textarea,read_only=True)
    
    if(cnt == 0):
        return "No Variables Present"

    sheet1.column_width = [15,10,10,35]
    sheet1.layout = widgets.Layout(height='auto', width = '600px')
    
    for k,c in enumerate(sheet1.cells):
        c.style['textAlign']='center'
        c.send_state()
    
    return sheet1

# %%
def main():
	VariableExplorer()
	
if __name__ == "__main__":
    main()
