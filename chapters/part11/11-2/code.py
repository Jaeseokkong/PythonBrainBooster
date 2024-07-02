# 점근 표기법
## 알고리즘의 실행 시간과 입력 크기 사잉의 관계
#점근 복잡도
def f(x):
    """x는 0보다 큰 정수라고 가정한다."""
    ans = 0
    #상수 시간이 걸리는 루프
    for i in range(1000):
        ans += 1
    print('지금까지 덧셈 횟수:', ans)
    #x 시간이 걸리는 루프
    for i in range(x):
        ans += 1
    print('지금까지 덧셈 횟수:', ans)
    #x**2 시간이 걸리는 중첩 루프
    for i in range(x):
        for j in range(x):
            ans += 1
            ans += 1
    print('지금까지 덧셈 횟수:', ans)
    return ans

f(10)
f(1000)
