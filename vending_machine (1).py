print("\t멋사 커피 자판기")

# 1. 메뉴 선택
print("\t  - 메  뉴 -")
print("\t1 : 아메리카노 1,800원")
print("\t2 : 카페라떼 2,700원")
print("\t3 : 초코라떼 2,300원")
print("\n========================================")


# 2. 가격 변수 선언
price = 0


# 4. 메뉴 입력
order = input("커피 종류를 선택하세요. 번호 입력 : ")
# order_name = {1: "아메리카노", 2:"카페라떼", 3:"초코라떼"}
if order == "1":
    order_name = '아메리카노'
    price = 1800
elif order == "2":
    order_name = '카페라떼'
    price = 2700
elif order == "3":
    order_name = '초코라떼'
    price = 2300
else:
    print("존재하지 않는 메뉴입니다.")

# 5. 추가 조건
whip = input("휘핑크림 추가해드릴까요? (Y/N) : ").upper()
hi = input("hot / ice 를 선택하세요. (hot/ice) : ").upper()

number = int(input("몇 잔 드릴까요? : "))
total = price*number

# 6. 출력값 설정
def combi(order, hi, whip):
    art = ""
    if hi == "HOT":
        art += '''
             S    S 
          S    S    S'''

    if whip == "Y":
        art += '''
               @@@
            @@@   @@
         @@@@      @@ 
        @            @  '''

    if order == "1":
        art += '''
        **************  
        **         ** ****
          **Coffee**  *** 
            ****** 
        '''
    elif order == "2":
        art += '''
        **************  
        ***        *** 
        ****Coffee****  
          ****  ****
            ******  
        '''
    elif order == "3":
        art += '''
        **************
      ***     *  *   *
      * *      **    * 
      * **   Choco  ** 
      ** **        ** 
          **********
        '''
    return art

# 7. 계산
count = 3
answer = int(input('총 금액은 ' + str(total) + '원 입니다. 돈을 투입해주세요. : '))
while count >= 1:
    if answer >= total:
        print(str(answer) + '원을 받았습니다. 거스름돈은 ' + str(answer - total) + '원입니다.')
        print('주문하신 ' + order_name + ' 나왔습니다.')
        print(combi(order, hi, whip))
        break
    else: 
        if answer < total:
            add = int(input(str(total - answer) + '원이 부족합니다. 돈을 추가로 투입해주세요. : '))
            total -= add
            count -= 1
        if answer == total:
            print('주문하신 ' + order_name + ' 나왔습니다.')
            print(combi(order, hi, whip))
        elif count == 0:
            print("금액이 부족합니다. 주문이 취소되었습니다.")
            break