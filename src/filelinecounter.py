import os

path = 'C:\\Users\\Elitebook\\PycharmProjects\\MyProjects\\src'
lst = os.listdir(path)

for f in lst:
    #print(f)
    if f != '__pycache__':
        lineNr = 0
        with open(path + "\\" + f, 'r') as reader:
           line = reader.readline()
           while line != '':
              #print(str(lineNr) + "\t" + line)
              line = reader.readline()
              lineNr +=1
        print('Dateiname: ' + f + ', Anzahl der Zeilen: ' + str(lineNr))
