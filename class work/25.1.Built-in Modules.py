## creating a new directory

import os
if not os.path.exists('Batch-31'):
    os.mkdir('Batch-31')

## Removing a new directory

import os
if not os.path.exists('Batch-31'):
    os.rmdir('Batch-31')

## floder with in floder

import os
os.makedirs('Batch-31\subchild')

## removing directory that has some content

import os
import shutil
shutil.rmtree('Batch-31')

## current directory which your are working for

import os
print(os.getcwd())

## if you want to change one floder to another(change directory)

import os
print(os.getcwd())
os.chdir('123')
print(os.getcwd())

## current files what are there in a floder

import os
print(os.getcwd())
print(os.listdir('.'))

## create a new file inside my floder

import os
filepath=os.path.join('1415','demo.txt')
with open(filepath,'w+') as f:
    f.write("Hello world")
    f.seek(0)
    print(f.read())

## remove file

import os
filepath=os.path.join('1415','demo.txt')
os.remove(filepath())