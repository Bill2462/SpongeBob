import csv


#export all data
def exportData(values, outputFile):
    outFile = open(outputFile, 'w') 
    writer = csv.DictWriter(outFile, values[0].keys())
    writer.writeheader()
    for row in values:
        writer.writerow(row)
