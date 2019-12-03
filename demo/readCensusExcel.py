import openpyxl,pprint

wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb['Population by Census Tract']
#print(sheet.title)

countyData = {}
rows_num = sheet.max_row
#print(rows_num)

for row in range(2, rows_num+1):
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    countyData.setdefault(state, {})
    countyData[state].setdefault(county, {'pop': 0, 'tracts': 0})
    #不同州县各自的数据累加。
    countyData[state][county]['tracts'] += 1
    countyData[state][county]['pop'] += int(pop)

countyData = pprint.pformat(countyData)
print(countyData)

