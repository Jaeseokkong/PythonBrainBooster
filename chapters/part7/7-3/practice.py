# 피보나치수열에서 처음에 나오는 숫자 10개를 fib_file 파일에 저장하는 프로그램 작성 (각 숫자는 파일에 한 라인으로 지정)
def fib(n):
    """n은 정수이고 n >= 0이라고 가정한다.
        n의 피보나치수열 값을 반환한다."""
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
    
fib_handle = open('fib_file', 'w')

def test_fib(n):
    for i in range(n + 1):
        fib_handle.write(str(fib(i)) + '\n')

test_fib(10)

# 파일에 숫자를 읽어 출력
with open('fib_file') as fib_handle:
    for line in fib_handle:
        print(line[:-1])