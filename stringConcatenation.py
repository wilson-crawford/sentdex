names = ['Jeff', 'Gary', 'Jill', 'Samantha']

##for name in names:
##    print ('Hello there, ' + name)
##    print(' '.join(['Hello there,', name]))

#print(', '.join(names))

import os

location_of_files = 'H:\\TRAINING\\PROGRAMMING\\PYTHON\\sentdexPython'
file_name = 'example.txt'

print(location_of_files + '\\' + file_name)

with open(os.path.join(location_of_files, file_name)) as f:
    print(f.read())
