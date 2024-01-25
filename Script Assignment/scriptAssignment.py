import os

# This is how to search through a directory for files with specific extensions

print(os.getcwd())


fileList = os.listdir('/Users/adam/Desktop/GitHub/Python-Course/Script Assignment')
print(fileList)


files = []
for i in os.listdir('/Users/adam/Desktop/GitHub/Python-Course/Script Assignment'):
    fileNames = os.fsdecode(i)
    if fileNames.endswith('.txt'):
        files.append(fileNames)


print('\nThese are all the files that end with the .txt extension')
print(files)