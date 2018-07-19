#-*-coding:utf-8-*- 
from selenium import webdriver
import xlrd

class ReadExcel():
    # 路径和excel的第一个sheet1
    def __init__(self,excelPath, sheetName="Sheet1"):
        # 打开Excel
        self.data=xlrd.open_workbook(excelPath)
        # 根据sheetname获取当前数据
        self.table=self.data.sheet_by_name(sheetName)
        # 获取第一行作为key值
        self.keys=self.table.row_values(0)
        # 获取总行数和总列数
        self.rowNum=self.table.nrows
        self.colNum=self.table.ncols

    def dict_data(self):
        if self.rowNum<=1:
            print("总行数小于1，该Excel表无数据")
        else:
            r=[]
            for i in list(range(self.rowNum-1)):
                s={}
                # 记录条目
                s['rowNum']=i+1
                # 第二行数值
                values=self.table.row_values(i+1)
                for x in list(range(self.colNum)):
                    # 对应的['username', 'psw', 'result']获取对应的值
                    s[self.keys[x]]=values[x]
                r.append(s)
            return r
if __name__ == "__main__":
    filepath = "testdata.xlsx"
    sheetName = "Sheet1"
    data = ReadExcel(filepath, sheetName)
    # print(data.dict_data())
    for i in data.dict_data():
        print(i)