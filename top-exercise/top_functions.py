import csv

data = []
with open('top_output.txt') as fin:
  lines =  fin.readlines()
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
