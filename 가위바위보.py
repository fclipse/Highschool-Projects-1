from random import *

while(1):
    user = int(input('입력 : 가위(1), 바위(2), 보(3)'))
    com = randint(1, 3)
    print(com)
    
    if user == com:
        print('비김')
    elif (user + com == 4):
        if user > com:
            print('짐')
        else:
            print('이김')
    elif user > com:
        print('이김')
    else:
        print('짐')
