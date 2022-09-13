


# coding = utf-8
from csv import excel
from multiprocessing.sharedctypes import Value
import xlrd
from xlutils.copy import copy
class ExcelUtil:
    def __init__(self,excel_path=None,index=None):
        if excel_path == None:
            self.excel_path = 'F:/selenium_python/Imooc_selenium/config/ceshi.xls'
        else:
            self.excel_path = excel_path
        if index == None:
            index = 0
        self.data = xlrd.open_workbook(self.excel_path)      # 打开工作薄
        self.table = self.data.sheets()[index]          # 通过索引获取sheet表格
        # 获取case[[],[],[]]
        # self.rows = self.table.nrows                    # 获取行数
    # 获取excel数据 加入列表中[[],[],[]]
    def get_data(self):
        result = []
        if self.get_lines() != None:
            for i in range(self.get_lines()):
                col = self.table.row_values(i)
                result.append(col)
            return result
        return None

    # 获取excel行数
    def get_lines(self):
        rows = self.table.nrows 
        if rows >= 1:
            return rows
        return None

    # 获取单元格的数据
    def get_col_value(self,row,col):
        if self.get_lines() >= row:
            data = self.table.cell(row,col).value
            return data
        return None


    # 写入数据
    def write_value(self,row,value):
        #read_value = self.data
        read_value =  xlrd.open_workbook(self.excel_path)    
        write_data = copy(read_value)                     #复制一份excel文件(操作赋值的数据用来写入数据)
        write_data.get_sheet(0).write(row,9,value)        #在第一个sheet页 写入数据   
        write_data.save(self.excel_path) 

if __name__ == '__main__':
    ex = ExcelUtil('F:/selenium_python/Imooc_selenium/config/key_word.xls')
    print(ex.get_col_value(3,5))

