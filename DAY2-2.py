import random
ans=input('請輸入一個數字:')
number=random.randint(1,10)
while int(ans)!=int(number):
    ans=input('再猜一次:')   
else:
    print('猜對了!')