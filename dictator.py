import csv


def create_dict():
    dict={}
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if (row[0]=="Timestamp"):
                continue
            dict[row[1]]=row[2]
    return dict


create_dict()        