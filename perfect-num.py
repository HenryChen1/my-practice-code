print('hello,world!')

#x = int(input('x = '))
#y = int(input('y = '))

print('完美数为：')

for x in range(3 , 1000 , 1):
    sum = 0
    for f in range(1 , x ,1):
        if   x % f == 0:
            sum += f
    if sum == x :
        print(x)

print('--------')
