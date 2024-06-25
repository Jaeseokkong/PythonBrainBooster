# 전역 변수
## fib 함수 호출 횟수 전역변수 지정
def fib(x):
    """x은 정수이고 x >= 0이라고 가정한다.
        x의 피보나치수열 값을 반환한다."""
    global num_fib_calls
    num_fib_calls += 1
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)
    
def test_fib(n):
    for i in range(n + 1):
        global num_fib_calls
        num_fib_calls = 0
        print(f'fib({i}) =', fib(i))
        print(f'fib 호출 횟수 : {num_fib_calls}번')

test_fib(10)