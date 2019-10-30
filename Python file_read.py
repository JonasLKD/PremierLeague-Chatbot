import csv


def file_reader():
    with open('Football_Stats.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for line in csv_reader:
            print(line)







