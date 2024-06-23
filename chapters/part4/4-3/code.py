# 함수를 사용해 코드를 모듈화하기
# 기존 find_root
# def find_root(x, power, epsilon): #값, 제곱수, 오차범위
#     """x와 epsilon은 int 또는 float이고, power는 정수이며,
#             epsilonㅇ > 0 & power >= 1라고 가정한다.
#         x에서 epsilon 이내에 y**power가 있다면 y를 반환한다.
#         만족하는 float가 없다면 None을 반환한다.
#     """
#     #답이 포함된 범위를 찾는다.
#     if x < 0 and power%2 == 0:
#         return None #음수는 짝수 제곱근이 없다.
#     low = min(-1, x)
#     high = max(1, x)
#     #이분 검색
#     ans = (high + low) / 2
#     while abs(ans**power - x) >= epsilon:
#         if ans**power > x:
#             high = ans
#         else:
#             low = ans
#         ans = (high + low)/2
#     return ans

def find_root_bouds(x, power):
    """x는 float, power는 양의 정수이다.
        low**power <= x이고 high**power >= x인 low, high를 반환한다.
    """
    low = min(-1, x)
    high = max(1, x)
    return low, high

def bisection_solve(x, power, epsilon, low, high):
    """x, epsilon, low, high는 float, epsilon >0 , low <= high이고
        x에서 epsilon 이내에 ans**power를 만족시키는
        low와 high 사이의 값 ans가 있다.
        x에서 epsilon 이내에 ans**power를 만족시키는 ans를 반환한다.
    """
    ans = (high + low) /2
    while abs(ans**power - x) > epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2
    return ans

def find_root(x, power, epsilon):
    """x와 epsilon은 int 또는 float, power는 int,
        epsilon > 0 & power >= 1 이라고 가정한다.
        x에서 epsilon 이내에 y**power가 있다면 y를 반환한다.
        만족하는 float 값이 존재하지 않는다면 None을 반환한다.
    """
    if x < 0 and power%2 == 0:
        return None
    low, high = find_root_bouds(x, power)
    return bisection_solve(x, power, epsilon, low, high)