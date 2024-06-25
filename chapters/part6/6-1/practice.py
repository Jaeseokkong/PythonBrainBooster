# fib(5)를 계산할 때 fib(2)의 값은 몇번 계산되는가
def fib(n):
    """n은 정수이고 n >= 0이라고 가정한다.
        n의 피보나치수열 값을 반환한다."""
    if n == 2:
        print('fib(2) 계산')
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
fib(5)
# fib(5)
# = fib(4) + fib(3)
# = fib(3) + fib(2) + fib(2) + fib(1)
# = fib(2) + fib(1) + fib(1) + fib(0) + fib(1) + fib(0) + 1
# = fib(1) + fib(0) + 1 + 1 + 1 + 1 + 1 + 1
# = 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 8

# fib(2)의 값은 총 3번 계산