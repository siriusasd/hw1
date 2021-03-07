# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '108033221.csv'
data = []
header = []

with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
      data.append(row)

#=======================================

# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

# Retrive ten data points from the beginning.
#target_data = data[:10]

#target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))
target_data1 = list(filter(lambda item: (item['TEMP'] != "-99" ) and (item['TEMP'] != "-999"), data))
target_data = list(filter(lambda item: (item['station_id'] == 'C0A880') or (item['station_id'] == 'C0F9A0') or (item['station_id'] == 'C0G640') or (item['station_id'] == 'C0R190') or (item['station_id'] == 'C0X260'), target_data1))

maxArray=[["C0A880", -1.0],["C0F9A0", -1.0],["C0G640", -1.0],["C0R190", -1.0],["C0X260", -1.0]]

for index in range(len(target_data)):
    #print(target_data[index]['station_id'], target_data[index]['TEMP'])

    if target_data[index]['station_id']=="C0A880" :
        if maxArray[0][1]<float(target_data[index]['TEMP']):
            maxArray[0][1]=float(target_data[index]['TEMP'])
    elif target_data[index]['station_id']=="C0F9A0" :
        if maxArray[1][1]<float(target_data[index]['TEMP']):
            maxArray[1][1]=float(target_data[index]['TEMP'])
    elif target_data[index]['station_id']=="C0G640" :
        if maxArray[2][1]<float(target_data[index]['TEMP']):
            maxArray[2][1]=float(target_data[index]['TEMP'])
    elif target_data[index]['station_id']=="C0R190" :
        if maxArray[3][1]<float(target_data[index]['TEMP']):
            maxArray[3][1]=float(target_data[index]['TEMP'])
    elif target_data[index]['station_id']=="C0X260" :
        if maxArray[4][1]<float(target_data[index]['TEMP']):
            maxArray[4][1]=float(target_data[index]['TEMP'])

for index in range(5):
    if maxArray[index][1]==-1.0:
        maxArray[index][1]="None"
#=======================================

# Part. 4
#=======================================
# Print result
print(maxArray)
#print(maxArray[1][0])
#print(len(target_data))
#========================================