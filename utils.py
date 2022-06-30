import xlsxwriter 

def GenerateExcel(array):
    workbook = xlsxwriter.Workbook('relat_zukerman.xlsx') 
    worksheet = workbook.add_worksheet("My sheet") 

    row = 0
    col = 0
    for item in (array): 
        worksheet.write(row, 0, item.title) 
        worksheet.write(row, 1, item.value) 
        worksheet.write(row, 3, item.date) 
        worksheet.write(row, 4, item.link) 
        row += 1
    
    workbook.close(); 