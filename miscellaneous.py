from openpyxl import Workbook
import pandas as pd
from pandas import read_json
import numpy as np
import os

file = pd.read_csv('C:\Pytest_Demo\BBGW_OPENET_20220202_000107.csv')
openet = file.to_excel('abc.xlsx')


cwd = os.getcwd()

files = os.listdir(cwd)
print("files in %r: %s" % (cwd, files))



readfile = pd.read_csv('C:\Pytest_Demo\BBGW_OPENET_20220202_000107.csv')
readfile.to_excel('C:\Pytest_Demo\Python_openet.xlsx',index = None, header=True)


#first_excel = Workbook()

#sheet = first_excel.active
#sheet["A1"] = "hello"
#sheet["B1"] = "all good"
#first_excel.save(filename='PythonExcel.xlsx')
#ws1 = first_excel.create_sheet("Sheet2")
#print(first_excel.get_sheet_names)



