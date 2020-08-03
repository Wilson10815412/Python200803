H=input('請輸入身高(M):')
W=input('請輸入體重(KG):')
BMI=float(W)//float(H)**2
if float(BMI) <18.5:
    print('體重過輕')
elif float(BMI)<24:
    print('體重正常')
elif float(BMI)<27:
    print('體重過重')
elif float(BMI)<30:
    print('輕度肥胖')
elif float(BMI)<35:
    print('中度肥胖')
else:
    print('重度肥胖')
