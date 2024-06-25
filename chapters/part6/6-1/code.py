# 피보나치수열
## 피보나치수열의 재귀 구현
def fib(n):
    """n은 정수이고 n >= 0이라고 가정한다.
        n의 피보나치수열 값을 반환한다."""
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
def test_fib(n):
    for i in range(n + 1):
        print(f'fib({i}) =', fib(i))

print(test_fib(7))