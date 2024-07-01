# 계산 복잡도에 관한 고찰
## 선형 알고리즘
def linear_search(L, x):
    for e in L:
        if e == x:
            return True
    return False

#linear_search(L, 3) 일때, (L의 길이는 1000000)
# 첫 원소가 3이면 바로 True(최상의 실행 시간), 없다면 1000000 검사 후 False 반환(최악의 실행 시간)

## 팩토리얼 함수의 재귀 구현
def fact(n):
    """n은 양의 정수라고 가정한다.
        n!을 반환한다."""
    answer = 1 #1스텝
    while n > 1: #1스텝
        answer *= n #2스텝(할당&연산)
        n -= 1 #2스텝(할당&연산)
    return answer #1스텝
#이 프로그램 스텝 수 1+1+5n ex) n = 1000, 5002스텝 실행

