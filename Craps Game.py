print('Craps Game')

import random

craps_1 = int(random.randint(1,6))
craps_2 = int(random.randint(1,6))

n = 1
sum = craps_1 + craps_2
# print('first round sum is %d' % (sum))
if sum == 7 or sum == 11:
    print('you win!')
    print('%d' % (sum))
    n = 0
if  sum == 2 | 3 | 11:
    print('you lose!')
    print('%d' % (sum))
i = 1
while n :
    craps_a = int(random.randint(1, 6))
    craps_b = int(random.randint(1, 6))
    # print('%d and %d ' % (craps_a , craps_b))
    summary = craps_a + craps_b
    if summary == sum:
        print('you win!!')
        # print('%d in the %d times'%(summary,i))
        break
    if summary == 7:
        print('you lose!!')
        # print('%d in the %d times'%(summary,i))
        break
    i = i + 1


