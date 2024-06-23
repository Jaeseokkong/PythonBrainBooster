# 사양

# 독스트링 추가
def find_root(x, power, epsilon): #값, 제곱수, 오차범위
    """x와 epsilon은 int 또는 float이고, power는 정수이며,
            epsilonㅇ > 0 & power >= 1라고 가정한다.
        x에서 epsilon 이내에 y**power가 있다면 y를 반환한다.
        만족하는 float가 없다면 None을 반환한다.
    """
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
