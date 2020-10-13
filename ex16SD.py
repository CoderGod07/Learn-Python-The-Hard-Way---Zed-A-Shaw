from sys import argv

script, fileName = argv

data = open(fileName)
print(data.read())