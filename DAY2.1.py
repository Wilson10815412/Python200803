import random
ans=input('Enter your anser:')
number=random.randint(1,20)
time=4
while int(ans)!=int(number) and time>0:
    time=int(time)-1
    ans=input('Try again:')   
if int(ans)==int(number):
    print('You got it!')
else:
    print('You\'re loser!')
    