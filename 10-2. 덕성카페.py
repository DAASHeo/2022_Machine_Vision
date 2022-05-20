#########################프로그램####################################

# 커피 종류(cType)를 받아서 그에 따른 가격을 리턴

def Coffee(cType):
    
    m = 0            # 가격은 0 으로 초기화
    
    if cType == 'A': # 커피 종류가 A이면
        m = 3900     # 가격은 3900원
        
    elif cType == 'C':
        m = 4500
        
    elif cType == 'G':
        m = 5000

    elif cType == 'J':
        m = 5500
        
    else:
        m = 0
        
    return m

# 커피 사이즈(cSize)를 받아서 그에 따른 가격을 리턴

def Size(cSize):
    
    m = 0            # 가격 = 0 으로 초기화
    
    if cSize == 'G': # 사이즈가 G이면
        m = 1000     # 가격은 1000원
        
    elif cSize == 'R':
        m = 500
        
    else:
        m = 0
        
    return m

# 종류에 따른 가격(tm)과 사이즈에 따른 가격(sm)을 받아서 더한 총액을 리턴

def Price(tm,sm):
    return tm + sm


####################메인 프로그램############################

for i in range(5):  # 5명의 손님이 대기하고 있으므로 5번 반복

    print("덕성 카페에 오신 것을 환영합니다.^^")
    print("커피 종류와 사이즈를 선택해 주세요.")
    cType = input("A(아메리카노) / C(카페라떼) / G(그린티) / J(오렌지쥬스) :") # 커피 종류 입력
    cSize = input('G(Grande) / R(Reguar) / S(Short) :') # 커피 사이즈 입력
    print('총 금액은 %d 원 입니다.' % Price(Coffee(cType),Size(cSize))) #출력
    print("\n맛있게 드세요~~\n다음 손님 무엇을 도와드릴까요?")    
