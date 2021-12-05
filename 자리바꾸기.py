from random import *
while 1 :
    print(sep = ' ')
    n = int(input('인원 수 입력 : '))
    list_a = list(range(1, n + 1))
    #change = int(input('바꾸기 횟수 입력 : ')) #change 값을 입력할 수 있는 코드
    change = 100 * randint(10, 20)
    for i in range(change):
        b = randint(0, n - 1)
        c = randint(0, n - 1)
        #print(len(list(range(0, n))))          #range(0, n)의 크기 출력
        tp = list_a[b]
        list_a[b] = list_a[c]
        list_a[c] = tp
        
    #print(list_a)                              #list_a 리스트 출력

    if n % 6 == 0 :
        n2 = 0
    else :
        n2 = 1
    n3 = int(n / 6)
                                                #Ilovepython
    for i in range(n3 + n2):
        for j in range(3):
            for k in range(2):
                if n < (6*i + 2*j + k + 1) :
                    break
                else :
                    print('%02d'%(list_a[6*i + 2*j + k]), end = ' ' )
            print(end = '    ')
        print(sep = ' ')
