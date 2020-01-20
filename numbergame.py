print ('Enter a number of your choice')
x=input()

if float(x)%2 == 0 and float(x)%5 == 0:
    print('Elephant')
elif float(x)%2 == 0:
    print('Cat')
elif float(x)%5 == 0:
    print('Dog')
else:
    print('Tiger')
