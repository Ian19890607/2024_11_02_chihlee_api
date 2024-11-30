#============================================================================
#Name        : biglottery.py
#撰寫一個大樂透電腦自動選號程式，程式執行會以亂數的方式顯示1-49之間七個不重複的大樂透號碼。

#============================================================
import random

def main():
    number_list=[]
    while (len(number_list)<7):   #產生7個隨機亂數
        random_number = random.randint(1, 49)
        number_list.append(random_number)
        number_list_remove_duplicate=list(set(number_list))

        if len(number_list)<=6:  #非特別號，進行排序
            number_list_sorted=sorted(number_list_remove_duplicate, reverse=False)    #進行排序
            number_list=number_list_sorted[:]
    print(f"本期大樂透電腦選號號碼如下:\n")
    for ii in number_list:
        print(ii,end=' ')
    print("\n")      
    print(f"特別號:{number_list[-1]}")

if __name__ == '__main__':
    main()