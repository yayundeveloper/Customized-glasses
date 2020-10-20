import csv
import os

file_old = './Write/Writes.csv'
file_temp = './Write/Writestemp.csv'


with open(file_old, 'r', newline='', encoding='gbk') as f_old, \
    open(file_temp, 'w', newline='', encoding='gbk') as f_temp:

    f_csv_old = csv.reader(f_old)
    f_csv_temp = csv.writer(f_temp)

    for rows in f_csv_old:
        if rows[2] != '20100800124243':
            f_csv_temp.writerow(rows)

os.remove(file_old)
os.rename(file_temp, file_old)
