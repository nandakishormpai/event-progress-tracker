import csv

def create_dict():
    diction={}
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if (row[0]=="Timestamp"):
                continue
            diction[row[1]]=row[2]
    return diction


create_dict()        