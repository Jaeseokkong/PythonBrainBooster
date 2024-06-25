# 0보다 큰 정수의 조화급수(harmonic series)의 합 (1 + 1/2 + 1/3 + ... + 1/4)식을 계산하는 재귀함수
def fact_hs (n):
    """n은 0보다 큰 정수로 가정한다.
        1/n!을 반환한다."""
    if n == 1:
        return 1
    else:
        return (1/n) + fact_hs(n - 1)

print(fact_hs(10))