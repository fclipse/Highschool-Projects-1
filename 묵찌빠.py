from random import *

def 가위바위보(hand) :
    if hand == 1 :
        return '가위'
    elif hand == 2 :
        return '바위'
    else :
        return '보'
    
def 묵찌빠(hand) :
    if hand == 1 :
        return '찌'
    elif hand == 2 :
        return '묵'
    else :
        return '빠'
#가위바위보 승리/패배판정 함수 (1 : 승리, 0 : 비김, -1 : 패배)
def wol(a, b) :
    if a == b :
        return 0
    elif a + b == 4 :
        if a > b :
            return -1
        else :
            return 1
    elif a > b :
        return 1
    else :
        return -1
#user와 com 가위,바위,보 출력 함수
def rsp(a, b) :
    print('user : ', 가위바위보(a))
    print('com : ', 가위바위보(b))
            
print('묵찌빠 게임(1 : 가위, 2 : 바위, 3: 보)')
print(sep = ' ')

while 1 :
    user = int(input('가위바위보 : '))
    com = randint(1, 3)
    #가위바위보 출력
    rsp(user, com)
    #가위바위보 승패 판단
    win = wol(user, com)
    #승패가 났을 시 탈출
    if win != 0 :
        break

while 1 :
    pre_user = user
    user = int(input('묵찌빠 : '))
    com = randint(1, 3)
    #묵찌빠 출력
    print(묵찌빠(pre_user)*2, 묵찌빠(user))
    #가위바위보 출력
    rsp(user, com)
    #묵찌빠 승패 판단
    win = wol(user, com)
    #승패가 났을 시 탈출
    if win == 0 :
        break
i = randint(1, 100)
if win > 0 :
    print('당신은 알파고를 묵찌빠로 이겼습니다!!! (알파고 승률 : %d %%)'%(i))
else :
    print('당신은 알파고에게 묵찌빠로 졌습니다... (알파고 승률 : %d %%)'%(i))
