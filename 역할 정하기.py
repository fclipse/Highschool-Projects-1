# Project_역할정하기
from random import *
# list_b[0] 부터 list_b[i] 까지의 합을 구하는 함수
def plus_list(index):
    res = 0
    for i in range(index):
        res += list_b[i]
    return res
q1 = input('역할 정하기 프로그램(Enter를 누르세요)')
# list_a : 역할을 저장하는 리스트
list_a = ['밀걸레', '책상밀기', '빗자루', '특별구역', '칠판', '교탁/거울', '유리창']
# list_b : 역할당 인원수를 저장하는 리스트
list_b = [6, 4, 6, 8, 1, 1, 2]
# list_c : 반 전체의 번호를 저장하는 리스트
list_c = list(range(1, 29))
# list_c 를 랜덤하게 섞는 for문
for i in range(100000):
    al = randint(0, 27)
    be = randint(0, 27)
    temp = list_c[al]
    list_c[al] = list_c[be]
    list_c[be] = temp
# 역할별로 번호를 출력하는 for문
for i in range(7):
    print(list_a[i], ':', end = ' ')
    for j in range(list_b[i]):
        n1 = plus_list(i)
        print(list_c[n1 + j], end = '')
        if list_b[i] != j + 1:
            print(',', end = ' ')
    print(sep = ' ')
q2 = input('역할이 정해졌습니다!')
