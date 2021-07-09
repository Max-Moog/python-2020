filePath= '/src/filelinecounter.py'
"""with open(filePath, 'r') as reader:
   print(reader.read())"""

"""with open(filePath, 'r') as reader:
   lst = reader.readlines()
   print("Zeile 4: " + lst[4])
"""

"""lineNr = 1
with open(filePath, 'r') as reader:
   line = reader.readline()
   while line != '':  # The EOF char is an empty string
      print(str(lineNr) + "\t" + line)
      line = reader.readline()
      lineNr +=1
"""

"""msg = print("well done")
with open(filePath, 'w') as writer:
    writer.write(msg)
"""

"""msg = print("well done:(")
with open(filePath, 'a') as a_writer:
    a_writer.write('\nmsg')
"""


