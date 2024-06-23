# 이분 검색을 사용한 x의 제곱근의 근삿값 찾기
x1 = 25
epsilon = 0.01

#x1 제곱근의 근삿값 찾기
if x1 < 0:
    print('제곱근이 존재하지 않습니다.')
else:
    low = 0
    high = max(1, x1)
    ans = (high + low)/2
    while abs(ans**2 - x1) >= epsilon:
        print(f'low : {low} // high : {high} // ans : {ans}')
        if ans**2 < x1:
            low = ans
        else:
            high = ans
        ans = (high + low)/2

x1_root = ans
x2 = -8

#x2의 세제곱근을 찾기
if x2 < 0:
    is_pos = False
    x2 = -x2
else:
    is_pos = True

low = 0
high = max(1, x2)
ans = (high + low)/2
while abs(ans**3 - x2) >= epsilon:
    if ans**3 > x2:
        high = ans
    else:
        low = ans
    ans = (high + low)/2

if is_pos:
    x2_root = ans
else:
    x2_root = -ans
    x2 = -x2

print(x1, '의 제곱근과 ', x2, '의 세제곱근의 합은', x1_root + x2_root, '입니다.')


# 근 찾기 함수
def find_root(x, power, epsilon): #값, 제곱수, 오차범위
    #답이 포함된 범위를 찾는다.
    if x < 0 and power%2 == 0:
        return None #음수는 짝수 제곱근이 없다.
    low = min(-1, x)
    high = max(1, x)
    #이분 검색
    ans = (high + low) / 2
    while abs(ans**power - x) >= epsilon:
        if ans**power > x:
            high = ans
        else:
            low = ans
        ans = (high + low)/2
    return ans

# find_root 테스트 함수
def test_find_root(x_vals, powers_vals, epsilon_vals):
    for x in x_vals:
        for p in powers_vals:
            for e in epsilon_vals:
                result = find_root(x, p, e)
                if(result == None):
                    val = '근이 존재하지 않습니다.'               
                else:
                    val = '통과'
                    if abs(result**p - x) > e:
                        val = '실패'
                    print(f'x = {x}, power = {p}, epsilon = {e}: {val}')

x_vals = (0.25, 8, -8)
power_vals = (1, 2, 3)
epsilons = (0.1, 0.001, 1)
test_find_root(x_vals, power_vals, epsilons)


# 가변 인자 함수
def mean(*args):
    tot = 0
    for a in args:
        tot += a
    return tot/len(args)

print(mean(1, 2))
print(mean(-4, 0, 1))

# 유효범위 확인
def f(x):
    y = 1
    x = x + y #지역변수의 x
    print('x = ', x)
    return x

x = 3 #전역 변수의 x
y = 2
z = f(x)
print('z = ', z)
print('x = ', x)
print('y = ', y)

print('================================')

#중첩된 유효범위
def f(x):
    def g():
        x = 'abc'
        print('x = ', x)
    def h():
        z = x
        print('z = ', z)
    x = x + 1
    print('x = ', x)
    h()
    g()
    print('x = ', x)
    return g

x = 3
z = f(x)
print('x = ', x)
print('z = ', z)
z()

# x = 4
# z = 4
# x = abc
# x = 4
# x = 3
# z = funtion

def f():
    print(x)

def g():
    print(x)
    x = 1

x = 3
f()
x = 3
g()