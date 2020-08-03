import openpyxl
import pprint
wb = openpyxl.load_workbook(r"C:\Users\v4h4\Desktop\censuspopdata.xlsx")
sheet = wb.active
data = {}

for i in range(2, sheet.max_row+1):
    state = sheet["B"+str(i)].value
    county = sheet["C"+str(i)].value
    pop = sheet["D"+str(i)].value

    data.setdefault(state, {})
    data[state].setdefault(county,{'tracts':0, "pop":0})

##    data[state][county]["tracts"]+=1
##    data[state][county]["pop"] += int(pop)

    with open(r"C:\Users\v4h4\Desktop\test.txt", "w") as f:
        f.write(data[state][county]["tracts"]+=1)
        f.write(data[state][county]["pop"] += int(pop))
