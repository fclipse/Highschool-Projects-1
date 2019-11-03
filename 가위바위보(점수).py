from random import *

u = 5
c = 5

def user_win() :        #FIXME_함수에서 print와 변수 대입을 모두 해야 할 방법 찾기
    print('이겼습니다!')
    u += 1
    c -+ 1
    return u, c
    
def com_win() :         #FIXME_함수에서 print와 변수 대입을 모두 해야 할 방법 찾기
    print('졌습니다...')
    u -= 1
    c += 1
    return u, c

def print_point(a, b) :
    print('user : %02d점 / com : %02d점'%(u, c))

print('가위바위보 게임(1 : 가위, 2 : 바위, 3: 보) : 각각 5점씩 주어지며 10점 달성시 승리합니다.')
print('점수를 다 잃을 시 패배합니다.')
print(sep = ' ')

while 1 :
    user = int(input('가위바위보 : '))
    com = randint(1, 3)

    if user == com :
        print('비겼습니다! 아깝네요')
    elif user + com == 4 :
        if user < com :
            #user_win()
            print('이겼습니다!')
            u += 1
            c -= 1
            print_point(u, c)
        else :
            #com_win()
            print('졌습니다...')
            u -= 1
            c += 1
            print_point(u, c)
    else :
        if user > com :
            #user_win()
            print('이겼습니다!')
            u += 1
            c -= 1
            print_point(u, c)
        else :
            #com_win()
            print('졌습니다...')
            u -= 1
            c += 1
            print_point(u, c)
            
    if u * c == 0 :
        break
alphago = randint(0, 1)
if c > u :
    if alphago == 1 :
        print('com : 인간 따위가 감히...미쳤습니까 휴먼?')
    else :
        print('com 승...다음 기회에 다시 도전하세요!')
else :
    print('user승!!! 축하합니다!')
