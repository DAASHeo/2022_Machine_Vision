from time import sleep

print("\t멋사 커피 자판기")

print("\t  - 메  뉴 -")
print("\t1 : 아메리카노 1,800원")
print("\t2 : 카페라떼 2,700원")
print("\t3 : 핫초코 2,300원")
print("\n========================================")


# 커피 그림  출력하는 함수
def coffeeArt(order, hot_ice, whipping):
    art = ""
    if hot_ice == "hot":
        art += '''
         S    S 
      S    S    S'''

    if whipping == "Y":
        art += '''
           @@@
        @@@   @@
     @@@@      @@ 
    @            @  '''

    if order == 1:
        art += '''
    **************  
    **         ** ****
      **Coffee**  *** 
        ****** 
    '''
    elif order == 2:
        art += '''
    **************  
    ***        *** 
    ****Coffee****  
      ****  ****
        ******  
    '''
    elif order == 3:
        art += '''
    **************
  ***     *  *   *
  * *      **    * 
  * **   Choco  ** 
  ** **        ** 
      **********
    '''
    return art


coffee_price = 0
whipping = "N"
menus = ['아메리카노', '카페라떼', '핫초코']

# 1. 메뉴 선택 
try:
    order = int(input("커피 종류를 선택하세요. 번호 입력 >>> "))
    if order == 1:
        coffee_price = 1800
    elif order == 2:
        coffee_price = 2700
        # 휘핑크림 추가 여부
        whipping = input("휘핑크림 추가해드릴까요? (Y/N) >>> ").upper()
        # y/n을 입력하지 않으면 주문 오류
        if (whipping != "Y" and whipping != "N"):
            quit()
    elif order == 3:
        coffee_price = 2300
        # 휘핑크림 추가 여부
        whipping = input("휘핑크림 추가해드릴까요? (Y/N) >>> ").upper()
        # y/n을 입력하지 않으면 주문 오류
        if (whipping != "Y" and whipping != "N"):
            quit()
    else:
        quit()

    # 핫/아이스 여부
    hot_ice = input("hot / ice를 선택하세요. (hot/ice) >>> ").lower()
    # hot/ice를 입력하지 않으면 주문 오류
    if (hot_ice != "hot" and hot_ice != "ice"):
        quit()

    # 잔 수 계산
    cups = int(input("몇 잔 드릴까요? >>> "))
    total_price = coffee_price * cups

except:
    print("입력 오류! 주문이 취소되었습니다.")
    quit()


# 주문 계산
def ordered_coffee(menu):
    print("\n========================================")
    sleep(1)  # 커피 만드는 시간 delay
    print("주문하신 " + menu + "나왔습니다.")
    print(coffeeArt(order, hot_ice, whipping))


# 총 금액 계산 + 금액 투입 후 잔돈 계산 알고리즘
print("총 금액은 " + str(total_price) + "원입니다. ")
received = int(input("돈을 투입해주세요 >>> "))
time = 3  # 기회는 3번

while (time > 0):
    if (received < total_price):  # 지불 받은 돈 < 커피 값
        balance = total_price - received  # 잔돈(돈을 적게 받아 남은 돈) = 커피 값 - 지불 받은 돈
        print("총" + str(received) + "원 투입하셨습니다. 남은 금액인 " + str(balance) + "원 더 투입하세요.")
        time = time - 1  # 돈을 적게 입력할 때 마다 기회 1번 차감
        print("남은 기회는 " + str(time) + "번 입니다.")

        if (time == 0):
            print("입력 시간 초과! 다시 주문해주세요.")  # 기회 3번 사용 시 입력 시간 초과
            break

        received = received + int(input("돈을 투입해주세요 >>> "))  # 지불 받은 돈은 누적되야함
        continue

    else:
        change = received - total_price  # 거스름돈(돈을 많이 받아 거슬러 줘야 하는 돈) = 지불 받은 돈 - 커피 값
        print(str(received) + "원 투입하셨습니다. 거스름 돈으로 " + str(change) + "원 드립니다.")
        ordered_coffee(menus[order - 1])  # 음료 제공
        break
