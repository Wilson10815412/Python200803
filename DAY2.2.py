number=input('輸入一個數字:')
x=2
if int(number)<2:
    print('它不是質數也不是合數')
else:
    while int(number)%int(x)!=0:
        x=int(x)+1
    if int(x)==int(number):
        print('它是質數')
    else:
        print('它是合數')
    