import re
import os
import datetime

now = datetime.datetime.now()



file="primer.txt"
wordList="replaceWith.txt"
path = r'C:\Users'


def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
          if name.endswith('.txt'):
            return os.path.join(root, name)

pathToFileFull=find(file,path)
pathToFile=os.path.dirname(pathToFileFull)
#ovaj naziv za folder ne valja, ali smislicu nesto drugo
pathToWrite = os.path.join(pathToFile,"Generated Files "+now.strftime("%Y%m%d %H%M"))

pathToWordList=find(wordList,path)


if not os.path.exists(pathToWrite):
    os.makedirs(pathToWrite)



inputWordList=open(pathToWordList, "rt")


words = [line.rstrip() for line in inputWordList]

for word in words:

  outputName=str(word)
  print(outputName)
  inputFile = open(pathToFileFull, "rt")
  output = open(os.path.join(pathToWrite,outputName + '.txt'), "wt")

  for line in inputFile:
    
    # replace the strings and write to output file
    output.write(re.sub(r'\bdiv\b', outputName , str(line)))
    
  inputFile.close()
  output.close()

# close input and output files

inputWordList.close()
