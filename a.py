import openpyxl
import json

f = open('F:/Users/14304/Desktop/aa.json','r', encoding='utf-8')

cont = f.read()


cont_json = json.loads(cont)

book = openpyxl.load_workbook('F:/Users/14304/Desktop/a.xlsx')
sheet = book.worksheets[0]

row_n = 2
col_n = 1
for row in cont_json['datas']['kzkccx']['rows']:
    col_n = 1
    for item in row:
        sheet.cell(row_n, col_n, row[item])
        col_n = col_n + 1
    row_n = row_n + 1

book.save('F:/Users/14304/Desktop/ab.xlsx')

