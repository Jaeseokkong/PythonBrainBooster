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

# 1. find_root 함수를 사용해 25의 제곱근, -8의 세제곱근, 16의 네제곱근에 대한 근삿값의 합을 출력(epsilon: 0.001)
epsilon = 0.001
x1_root = find_root(25, 2, epsilon)
x2_root = find_root(-8, 3, epsilon)
x3_root = find_root(16, 4, epsilon)
print(f'25의 제곱근({x1_root}), -8의 세제곱근({x2_root}), 16의 네제곱근({x3_root})의 합은 {x1_root + x2_root + x3_root}이다.')


# 2. 문자열 두 개를 인수로 받아 두 문자열 중 하나가 다른 하나에 등장한다면 True, 그렇지 않으면 False르 반환하는 is_in 함수 작성
def is_in (str1, str2):
    result = False
    if str1 in str2 or str2 in str1:
        result = True
    return result

# 3. is_in 함수를 테스트하는 함수 작성
def test_is_in(ss):
    for s in ss:
        s1 = s
        s2 = s[1:len(s)-1]
        if is_in(s1, s2) == True and is_in(s2, s1) == True:
            val = '통과'
        else:
            val = '실패'
        print(f's1 = {s1}, s2 = {s2}: {val}')
        s2 = s[1:len(s)-1:2]
        if is_in(s1, s2) == False and is_in(s2, s1) == False:
            val = '통과'
        else:
            val = '실패'
        print(f's1 = {s1}, s2 = {s2}: {val}')

test_is_in(('abcde', 'python'))


# 4. 하나 또는 두개의 int를 인수로 받는 mult 함수 작성
def mult(int1=None, int2 = None):
    if int1 != None and int2 != None:
        print(int1 * int2)
    elif int1 != None:
        print(int1)    
    elif int2 != Nono:
        print(int2)
    
mult(3, 2)
mult(1)
mult(int2=3)
mult()