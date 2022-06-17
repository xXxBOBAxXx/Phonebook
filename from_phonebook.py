import csv

pb = []

def from_pb(pb):
    with open("phonebook.csv", encoding = 'utf-8') as file:
        reader = csv.reader(file, delimiter = "|")
        for id in reader:
            pb.append(id)
        return pb

from_pb(pb)
