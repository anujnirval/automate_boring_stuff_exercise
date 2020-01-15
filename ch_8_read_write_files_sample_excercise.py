import os

print(os.path.join('usr','bin','spam'))

myFiles = ['accounts.txt','details.csv','invite.docx']
for filename in myFiles:
    print(os.path.join('/home/anujnirval',filename))

print(os.getcwd())

os.chdir('/python/AutomateTheBoringStuffwithPython/programs')
print(os.getcwd())

#os.makedirs('/python/AutomateTheBoringStuffwithPython/test')

print(os.path.abspath('.'))

print(os.path.abspath('./ch_8_read_write_files_sample_excercise.py'))

print(os.path.isabs('.'))
print(os.path.isabs(os.path.abspath('.')))

print(os.path.relpath('/python/AutomateTheBoringStuffwithPython/programs','/'))
print(os.path.relpath('/python/AutomateTheBoringStuffwithPython/programs','/python'))

########### Directory Name & Base Name
path = '/python/AutomateTheBoringStuffwithPython/programs'
print(os.path.basename(path))
print(os.path.dirname(path))

############# Directory and Base name together 

calcFilePath = '/python/AutomateTheBoringStuffwithPython/programs'
print(os.path.split(calcFilePath))

############# Seperating each folder name

print(calcFilePath.split(os.path.sep))

 
