# 객체로서의 함수

def find_root_bouds(x, power):
    """x는 float, power는 양의 정수이다.
        low**power <= x이고 high**power >= x인 low, high를 반환한다.
    """
    low = min(-1, x)
    high = max(1, x)
    return low, high


# bisection_solve 일반화하기
def bisection_solve(x, eval_ans, epsilon, low, high):
    """x, epsilon, low, high는 float, epsilon >0 , low <= high이고
        x에서 epsilon 이내에 ans**power를 만족시키는
        low와 high 사이의 값 ans가 있다.
        x에서 epsilon 이내에 ans**power를 만족시키는 ans를 반환한다.
    """
    ans = (high + low) /2
    while abs(eval_ans(ans) - x) > epsilon:
        if eval_ans(ans) < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    return ans

def square(ans):
    return ans**2

low, high = find_root_bouds(99, 2)
print(bisection_solve(99, square, 0.01, low, high))

# 람다 표현식
print(bisection_solve(99, lambda ans: ans**2, 0.01, low, high))

def create_eval_ans():
    power = input('양의 정수를 입력하세요:')
    return lambda ans: ans**int(power)

eval_ans = create_eval_ans()
print(bisection_solve(99, eval_ans, 0.01, low, high))

# bisection_solve를 사용해 로그의 근삿값 구하기
def log(x, base, epsilon):
    """x와 epsilon은 int 또는 float, base는 int,
        x > 1, epsilon > 0 & power >= 1이라 가정한다.
        x에서 epsilon 이내에 base**y를 만족시키는 float y를 반환한다.
    """
    def find_log_bounds(x, base):
        upper_bound = 0
        while base**upper_bound < x:
            upper_bound += 1
        return upper_bound - 1, upper_bound
    low, high = find_log_bounds(x, base)
    return bisection_solve(x, lambda ans: base**ans, epsilon, low, high)