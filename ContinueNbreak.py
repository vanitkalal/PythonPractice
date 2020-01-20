
while True:
    print('Plese enter your name')
    name = input()
    if name != 'Joey':
        continue
    print("Hey Joey what is the password ? Is it a fish")
    password = input()
    if password == 'swordfish':
        break
print("access granted")
