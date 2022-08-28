#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import csv
import os
import sys 
import pyexcel
#from openpyxl import Workbook

if os.name == 'nt':
    symbol = '\\'
if os.name == 'posix':
    symbol = '/'
#/home/me/PycharmProjects/velocity_vs acc001/data01/0.CSV
#print(os.environ)
dir_path = os.path.dirname(os.path.abspath(__file__)) + symbol

orig_stdout = sys.stdout
file_log = open(dir_path + 'log_file.txt', 'w')
sys.stdout= file_log
dir_path+='csv'
#dir_path ='/media/me/data/doc-i/работа/india/SERCEL 508 XT/'
print('dir_path=', dir_path)

csv_files = []  # составляю общий список файлов с вопросами
for root, dirs, files in os.walk(dir_path):
    for file in files:
        if (file.endswith(".csv")):
            csv_files.append(os.path.join(root, file))
print(len(csv_files))

file_name = csv_files[0]
print((file_name))
with open(file_name, encoding='utf-8-sig') as r_file:
    # Создаем объект DictReader, указываем символ-разделитель ","
    file_reader = csv.DictReader(r_file, delimiter = ",")
    field_names = file_reader.fieldnames
    print(field_names)
    count = 0
    dat = {}
    for row in file_reader:
        print(type(row))
        if row['Box Type']=='CX_508':
            print('CX_508')
            
        if row['Box Type']=='SCI_508':
            print('SCI_508')
        if row['Box Type']=='FDU_508':
            print('FDU_508')
        print(row['Box Type'] + ' ' + str(row['Serial Nb']))
        count += 1
      #  dat=row 
      dat = {"Sheet 1": [[1, 2, 3],[4, 5, 6]]}
    #print('Serial Nb', len(row))
    print(*dat)
    my_dest_file_name=dir_path+"arraydata.xls"
    pyexcel.save_book_as(dest_file_name=my_dest_file_name, bookdict=dat)
    #pyexcel.save_as(array=dat, dest_file_name=dir_path+"array_data.xls", dest_delimiter=',')
    r_file.close()
print(count)

file_log.close()
#Max. Distortion: -103 dB.
#Min. Common Mode Rejection (CMRR): 100 dB.
#Max. Gain error: 1.0%.
#Max. Phase error: 20 μs.
#Max. Noise (0 dB gain, 1600 mV scale): 1.0 μV.
#Max. Noise (12 dB gain, 400 mV scale): 0.25 μV.
#print(*file_reader.reader)

#SignalFileName = dir_path + 'data01'+symbol+'0.CSV'
#print(SignalFileName)
#with open(SignalFileName, 'r') as csvfile:
#    reader = csv.reader(csvfile, delimiter=',')
#    data = np.array(list(reader)).astype(float)

#print(data[:][:, 1])
#print(data[:][:, 0])

#from openpyxl import Workbook
#
#reload(sys)
#sys.setdefaultencoding('utf8')
#
#if __name__ == '__main__':
#    workbook = Workbook()
#    worksheet = workbook.active
#    with open('input.csv', 'r') as f:
#        reader = csv.reader(f)
#        for r, row in enumerate(reader):
#            for c, col in enumerate(row):
#                for idx, val in enumerate(col.split(',')):
#                    cell = worksheet.cell(row=r+1, column=c+1)
#                    cell.value = val
#    workbook.save('output.xlsx')