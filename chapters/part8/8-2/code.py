# 디버깅
def is_pal(x):
    """x는 리스트로 가정합니다.
       리스트가 팰린드롬이면 True, 그렇지 않으면 False를 반환합니다"""
    # temp = x
    # temp.reverse
    temp = x[:]
    temp.reverse()
    print(temp, x)
    return temp == x

def silly(n):
    """n은 정수이고 n > 0이라고 가정합니다.
       사용자에게 n 개의 입력을 받고, 입력 시퀀스가 팰린드롬이면 'Yes',
       그렇지 않으면 'No'를 출력합니다."""
    result = []
    for i in range(n):
        # result = []
        elem = input('문자를 입력하세요: ')
        result.append(elem)
    print(result)
    if is_pal(result):
        print('Yes')
    else:
        print('No')

silly(3)