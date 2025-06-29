from openpyxl import load_workbook

workBook=load_workbook("fileop/ScoresSheet.xlsx")
workSheet=workBook.worksheets[0]
for idx, row in enumerate(workSheet.rows):
    if idx == 0:
        continue
    row[5].value =int(row[1].value) * 0.3 + int(row[2].value ) * 0.1 \
        + int(row[3].value ) * 0.2 + int(row[4].value) * 0.4

workBook.save("fileop/ScoresSheet2.xlsx")