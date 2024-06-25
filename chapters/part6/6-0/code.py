# 재귀
## 팩토리얼의 반복 구현과 재귀 구현
def fact_iter(n):
    """n은 0보다 큰 정수를 가정한다.
        n!을 반환한다."""
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def fact_rec(n):
    """n은 0보다 큰 정수로 가정한다.
        n!을 반환한다."""
    if n == 1:
        return n
    else:
        return n*fact_rec(n - 1)