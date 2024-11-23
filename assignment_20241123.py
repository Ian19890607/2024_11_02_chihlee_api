class BMI():
    def __init__(self,name:str,height:float,weight:float):
        self.name = name #attribute
        self.height = height #attribute
        self.weight = weight #attribute

    def get_status(self,bmi:float)->str:
        '''
        docstring
        Parameter:
            bmi:bmi值可以整數或浮點數
        Return:str
            會傳出5個狀態
            - 正常範圍
            - 過重 
            - 輕度肥胖      
        '''
        if bmi >= 35 :
            bmi_str = '重度肥胖'
        elif bmi >= 30 :
            bmi_str = '中度肥胖'
        elif bmi >= 27 :
            bmi_str = '輕度肥胖'
        elif bmi >= 24 :
            bmi_str = '過重'
        elif bmi >= 18.5 :
            bmi_str = '正常範圍'
        else :
            bmi_str = '過輕' 
    return bmi_str

    def get_BMI():
        BMI_value= round(self.weight/((self.height/100)**2), 2)
    return BMI_value



while(True):
    try:
        height_cm = float(input("請輸入身高(公分):"))
        weight_kg = float(input("請輸入體重(公斤):"))
        bmi_value, bmi_str = BMI_math(height_cm, weight_kg)
        break
    except Exception:
        print('輸入格式錯誤,請重新輸入!')
    
print(f"您的BMI值是{bmi_value}\n您的體重{bmi_str}")
print("程式結束")