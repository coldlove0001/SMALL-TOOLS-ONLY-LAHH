# If you need to merge specific data in one box row by row
# TRY TO USE THIS
# EXAMPLE ---> https://docs.google.com/spreadsheets/d/1edr-9uJ9Midz9WSeiLM_npn9CdI9coHzrNCRT58RGcU/edit?usp=sharing


### 有開預購商品種多的話可以用這個Program跑一下，
# 輸入 1： 你的商品從哪一個ROW開始（A,B,C,D....ZZ）
# 輸入 2： 你的商品到哪一個ROW結束（A,B,C,D....ZZ）
# 最後，把輸出的結果直接貼去你的google sheet就能用了


def Total_len_Count(Alpabet):
    Back_Second = int(ord(Alpabet[-1])) - 64 # A[G] OR [G] = 7
    
    if len(Alpabet) > 1:
        First_One = (int(ord(Alpabet[0])) - 64) * 26 # [A]G = 1*26=26, [B]G = 2*26
        return First_One, Back_Second
    
    else:
        return None, Back_Second #Only one Alpabet
    
def main():
    FROM = input("FROM:  Where to Start? 從哪裏開始呢？......(EXAMPLE: B)  ")
    TO_WHERE = input("END:   Where it End? 到哪裏結束呢？......(EXAMPLE: GZ)  ")
    Front_From, Back_From = (Total_len_Count(FROM))   # B = 2
    Front_TO, Back_TO = (Total_len_Count(TO_WHERE))      # A =[1]*26, G = 7, TOTAL 33, G=33-FRONT
    # Front_TO, Back_TO = (Total_len_Count("BG"))      # B =[2]*26, G = 7, TOTAL 59
    
    # From-To List Creating
    from_To_List = ""
    if Front_From is None:
        From = Back_From  # From = 2
    else:
        From = Front_From + Back_From
        
    if Front_TO is None:
        To = Back_TO
    else:
        To = Front_TO + Back_TO  # TO = 33 
    
    # List Creating....
    Privious_Front_Alpabet =""
    Front_Alpabet = ""
    tmp = ""
    for i in range (From, To+1):
        Z_Special = 0
        tmp = ""
        if i <= 26: #A~Z
            tmp =  chr(i+64)
        
        elif (i > 26):
            # # A-Z = 1~26
            # # AA-AZ = 27~52  
            # # BA~BZ = 53~79
            Check = i//26
            if TO_WHERE[-1] == "Z" or i%26 == 0:
                Front_Alpabet = Privious_Front_Alpabet
                Z_Special += 26
            else:    
                Front_Alpabet = chr(64+Check)
                
            tmp = Front_Alpabet + chr((i-(Check*26))+Z_Special+64)    #z=26, Az=26+26=52 #BG=2*26+7
        Privious_Front_Alpabet = tmp[0]
            
        from_To_List += tmp + ","
    from_To_List = (from_To_List[:-1]).split(",")
    
    # Script for arrange the item 
    #'IF(${0}2="","",CONCATENATE(${0}$1," *",${0}2))'.format(i) +","
    tmp = ""
    for i in from_To_List:
        tmp += 'IF(${0}2="","",CONCATENATE(${0}$1," *",${0}2))'.format(i) +","
    tmp = tmp[:-1]
    Final = '=TEXTJOIN(CHAR(10),"true",{})'.format(tmp)
    print (Final)

main()
