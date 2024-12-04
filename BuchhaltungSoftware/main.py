import csv


def csvImport(source):
    with open(source, mode = 'r') as file:
        csvFile = csv.reader(file)
        for lines in csvFile:
            print(lines)