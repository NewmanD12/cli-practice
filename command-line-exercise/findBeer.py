with open('allFiles.txt', 'r') as fn:
  data = fn.readlines()
  lineCount = 1
  listOfLinesFound = []
  for line in data:
    line = line.replace('-', ' ').replace(',', ' ').replace('y', ' ')
    line = line.split()
    for i in line:
      if i.lower() == 'beer':
        listOfLinesFound.append(lineCount)
    lineCount += 1
  print(f'"Beer" was found {len(listOfLinesFound)} times on lines {listOfLinesFound}')