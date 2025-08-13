# generators
def read(database):
    for file in database:
        yield file

database=['file1..100','file101..200','file201..300','file301..400']
write=read(database)
print("First 100 files:",next(write))
print("Next 100 files:",next(write))
print("Next 100 files:",next(write))
print("Next 100 files:",next(write))

'''
First 100 files: file1..100
Next 100 files: file101..200
Next 100 files: file201..300
Next 100 files: file301..400 '''

##
def simple_generators():
    print("Start")
    yield 1
    yield 2
    yield 3
    print("End")
gen = simple_generators()
print(next(gen))
print(next(gen))
print(next(gen))
'''Start
1
2
3'''