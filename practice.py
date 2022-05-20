print("\t멋사 커피 자판기")

# 1. 메뉴 선택
print("\t  - 메  뉴 -")
print("\t1 : 아메리카노 1,800원")
print("\t2 : 카페라떼 2,700원")
print("\t3 : 초코라떼 2,300원")
print("\n========================================")

# 2. 가격 변수 선언
price = 0

# 3. 출력값 각각 설정
def hi(htype):
    if htype == ""
hi_hot = '''
         S    S 
      S    S    S
'''

whip_o = '''
           @@@
        @@@   @@
     @@@@      @@ 
    @            @  
'''

ame = '''
    **************  
    **         ** ****
      **Coffee**  *** 
        ****** 
'''

lat = '''
    **************  
    ***        *** 
    ****Coffee****  
      ****  ****
        ******  
'''

cho = '''
    **************
  ***     *  *   *
  * *      **    * 
  * **   Choco  ** 
  ** **        ** 
      **********
'''

# 4. 메뉴 입력
order = input("커피 종류를 선택하세요. 번호 입력 : ")
order_name = {1: "아메리카노", 2: "카페라떼", 3: "초코라떼"}
if order == "1":
    price = 1800
elif order == "2":
    price = 2700
elif order == "3":
    price = 2300
else:
    print("존재하지 않는 메뉴입니다.")

# 5. 추가 조건
whip = input("휘핑크림 추가해드릴까요? (Y/N) : ").upper()
hi = input("hot / ice 를 선택하세요. (hot/ice) : ").upper()

number = int(input("몇 잔 드릴까요? : "))
total = price * number


# 6. 출력값 설정
def combi():
    if hi == "hot":
        print(hi_hot)
    if whip == "y":
        print(whip_o)
    if order == "1":
        print(ame)
    elif order == "2":
        print(lat)
    else:
        print(cho)


# 7. 계산
count = 3
answer = int(input('총 금액은 ' + str(total) + '원 입니다. 돈을 투입해주세요. : '))
while count >= 1:
    if answer >= total:
        print(str(answer) + '원을 받았습니다. 거스름돈은 ' + str(answer - total) + '원입니다.')
        print('주문하신 {order_name[order]} 나왔습니다.')
        for i in range(number):
            combi()
        break
    else:
        if answer < total:
            add = int(input(str(total - answer) + '원이 부족합니다. 돈을 추가로 투입해주세요. : '))
            total -= add
            count -= 1
        if answer == total:
            print('주문하신 {order_name[order]} 나왔습니다.')
            for i in range(number):
                combi()
        elif count == 0:
            print("금액이 부족합니다. 주문이 취소되었습니다.")
            break