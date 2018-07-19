#-*-coding:utf-8-*- 
from selenium import webdriver
from common.readExcel_api import ReadExcel
import os

if __name__ == "__main__":
    filepath = os.path.realpath(os.path.dirname(os.path.dirname(__file__)))
    filepath = os.path.join(filepath,"common","testdata.xlsx")
    sheetName = "Sheet1"
    data = ReadExcel(filepath, sheetName)
    # print(data.dict_data())
    for i in data.dict_data():
        print(i)