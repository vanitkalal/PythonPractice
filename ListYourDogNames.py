#This program take the name of dogs you have

dognames = []

while True:
    print('Enter the dog name ' + str(len(dognames) + 1) + ' Or enter nothing to stop')
    name = input()
    if name == '':
        break
    dognames = dognames + [name]

print(dognames)
