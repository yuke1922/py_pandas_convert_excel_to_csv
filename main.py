import os
import pandas as pd
import csv

def cls():
    os.system("clear")

cls()

os.system("rm -rf ./output/")
os.system("mkdir ./output")

config_excel = "./config.xls"

all_sheets = pd.read_excel(config_excel, sheet_name=None)
sheets = all_sheets.keys()

for sheet_name in sheets:
    sheet = pd.read_excel(config_excel, sheet_name=sheet_name)
    sheet.to_csv("./output/%s.csv" % sheet_name, index=False)
