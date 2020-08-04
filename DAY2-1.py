import random
ans=input('請輸入一個數字:')
number=random.randint(1,10)
if int(ans)==int(number):
    print('猜對了!')
else:
    print('猜錯了!')
