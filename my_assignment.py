# 20241116 homework 
'''要檢查使用者輸入的格式,如果輸入錯誤,要求使用者重新輸入
-請將計算體重狀態,定義一個function'''

def get_status(bmi_kg_m2:float)->str:
    if bmi_kg_m2 >= 35 :
        bmi = '重度肥胖'
    elif bmi_kg_m2 >= 30 :
        bmi = '中度肥胖'
    elif bmi_kg_m2 >= 27 :
        bmi = '輕度肥胖'
    elif bmi_kg_m2 >= 24 :
        bmi = '過重'
    elif bmi_kg_m2 >= 18.5 :
        bmi = '正常範圍'
    else :
        bmi = '過輕' 
    return bmi

def cal_bmi(height_cm,weight_kg):
    return round(weight_kg/((height_cm/100)**2), 2)
    
while (True):
    try:
        height_cm = float(input("請輸入身高(公分):"))
        weight_kg = float(input("請輸入體重(公斤):"))
    except Exception:
        print('輸入格式錯誤，請重新輸入')   
        continue
    else:
        break
your_bmi=cal_bmi(height_cm,weight_kg)
print(f'Your BMI is {your_bmi}.')
your_bmi_comment=get_status(your_bmi)
print(f'根據計算您的BMI，結果是 "{your_bmi_comment}"')

print("程式結束")
