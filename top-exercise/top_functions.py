import csv

data = []
with open('top_output.txt') as fin:
    lines = fin.readlines()
    for line in lines:
        line = line.split()
        data.append(line)

fieldnames = data[11]

with open('top_output.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    count = 12
    while count < len(data):
        if len(data[count]) == 36:
            infoToPass = dict(zip(fieldnames, data[count]))
            writer.writerow(infoToPass)
        count += 1


def findAvgFaultsByPID(pid):
    faultsList = []
    with open('top_output.csv') as csvFile:
        reader = csv.DictReader(csvFile)
        for row in reader:
            if row['PID'] == pid:
                faultsList.append(row['FAULTS'].replace('+', ''))
    intFaultList = [int(x) for x in faultsList]
    avg = round(sum(intFaultList) / len(intFaultList), 2)
    print(intFaultList)
    return avg


print(findAvgFaultsByPID('6598'))
