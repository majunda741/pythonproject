# #!/usr/bin/env python
# # -*- coding: UTF-8 -*-
# import xlrd
# from openpyxl import load_workbook
#
#
# class ExcelUtil():
#     def __init__(self, excelPath, sheetName="Sheet1"):
#         self.data = xlrd.open_workbook(excelPath)
#         self.table = self.data.sheet_by_name(sheetName)
#         # 获取第一行作为key值
#         self.keys = self.table.row_values(0)
#         # 获取总行数
#         self.rowNum = self.table.nrows
#         # 获取总列数
#         self.colNum = self.table.ncols
#
#     def read_excel(self):
#         if self.rowNum <= 1:
#             print("总行数小于1")
#         else:
#             r = []
#             j = 1
#             for i in list(range(self.rowNum - 1)):
#                 s = {}
#                 # 从第二行取对应values值
#                 s['rowNum'] = i + 2
#                 values = self.table.row_values(j)
#                 # print(values)
#                 for x in list(range(self.colNum)):
#                     s[self.keys[x]] = values[x]
#                 r.append(s)
#                 j += 1
#             return r
#
#
# if __name__ == '__main__':
#     file1 = open("D:\\设备信息\\设备对应device.xlsx", mode='r')
#     print(file1.name)
#     ExcelUtil.read_excel(file1)
import Phone
if __name__ == '__main__':
    ph = Phone.Phone
    a = ph.getExceldevice(ph)
    for i in range(len(a)):
        print(i)
        print("------------------------")
        print(a[i].name)