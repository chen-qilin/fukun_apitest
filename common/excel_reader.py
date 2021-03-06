# ! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: 1.0
@author: fky
@site: 
@software: PyCharm
@file: excel_reader.py
@time: 2018/3/24 9:37
"""
import os
import ast
import get_path_info
from xlrd import open_workbook


class ExcelReader:
    def __init__(self):
        self.path = get_path_info.get_Path()  # 拿到该项目所在的绝对路径

    def read(self, filename, sheet_name="Sheet1"):
        xls_path = os.path.join(self.path, "testdata", filename)

        file = open_workbook(xls_path)  # 打开用例Excel

        table = file.sheet_by_name(sheet_name)  # 获得打开Excel的sheet

        # 获取总行数、总列数
        rows = table.nrows
        # ncols = table.ncols
        if rows > 1:
            # 获取第一列的内容，列表格式
            keys = table.row_values(0)
            # print(keys)

            api_data_lists = []
            # 获取每一行的内容，列表格式
            for col in range(1, rows):
                values = table.row_values(col)
                # keys，values这两个列表一一对应来组合转换为字典
                api_dict = dict(zip(keys, values))
                # print(api_dict)
                api_data_lists.append(api_dict)

            return api_data_lists
        else:
            print("表格未填写数据")
            return None

    def read_basic_data(self, filename="basic_data.xlsx", sheet_name="Sheet1"):
        xls_path = os.path.join(self.path, "testdata", filename)

        file = open_workbook(xls_path)  # 打开用例Excel

        table = file.sheet_by_name(sheet_name)

        # 获取总行数、总列数
        rows = table.nrows

        if rows == 2:
            # 获取第一列的内容，列表格式
            keys = table.row_values(0)
            # print(keys)

            temp_data_lists = []
            # 获取每一行的内容，列表格式
            for col in range(1, rows):
                values = table.row_values(col)
                # keys，values这两个列表一一对应来组合转换为字典
                api_dict = dict(zip(keys, values))
                # print(api_dict)
                temp_data_lists.append(api_dict)

            return temp_data_lists

        else:
            print("basic_data.xlsx只能有2行：第一行表头，第二行数据")
            return None


if __name__ == '__main__':
    pass
    # s = ExcelReader().read('mc_lpn.xlsx', "Sheet1")
    s = ExcelReader().read_basic_data('basic_data.xlsx')
    for i in range(len(s)):
        print(s[i]["basic_cookie"])
        print(s[i]["basic_headers"])





