import openpyxl
wb = openpyxl.load_workbook(r"C:\Users\v4h4\Desktop\CODIN HOBBY STUFF\small projects\example.xlsx")
sheet = wb["Sheet1"]
d = {}
for i in range(1, sheet.max_row+1):
    d[sheet["a"+str(i)].value] = {}
    d[sheet["a"+str(i)].value][sheet["b"+str(i)].value] = sheet["c"+str(i)].value


with open(r"C:\Users\v4h4\Desktop\test.txt", "w") as f:
    f.write(str(d))

