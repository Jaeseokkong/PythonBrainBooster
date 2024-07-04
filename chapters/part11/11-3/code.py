# 중요한 몇 가지 복잡도 종류
## 로그 복잡도
### 이진 검색은 탐색 대상 리스트의 길이에 대해 로그 복잡도를 가진다.

def int_to_str(i):
    """i는 0보다 큰 정수라고 가정한다.
        i의 문자열 표현을 반환한다."""
    digits = '0123456789'
    if i == 0:
        return '0'
    result = ''
    while i > 0:
        result = digits[i%10] + result
        i = i//10 #몫
        print(result , i)
    return result
# 복잡도 (O(log(i)))

def add_digits(n):
    """n이 0보다 큰 정수라고 가정한다.
        n에 있는 숫자의 합을 반환한다."""
    string_rep = int_to_str(n)
    val = 0
    for c in string_rep:
        val += int(c)
    return val

# 복잡도 (O(log(n)))

## 선형 복잡도
def factorial(x):
    """x는 양의 정수라고 가정한다.
        x!를 반환한다."""
    if x == 1:
        return 1
    else:
        return x*factorial(x-1)
# 재귀 호출의 길이가 함수의 복잡도
# 공간 복잡도는 O(x)

## 로그 선형 복잡도
# O(n*log(n)) 합병 정렬

## 다항 복잡도
# 가장 널리 사용하는 알고리즘의 다항 복잡도는 2차이다.
# 입력의 크기의 제곱에 비례
### 부분집합 테스트 함수
def is_subset(L1, L2):
    """L1과 L2는 리스트로 가정한다.
        L1의 모든 원소가 L2에도 있으면 True, 그렇지 않으면 False를 반환한다."""
    for e1 in L1:
        matched = False
        for e2 in L2:
            if e1 == e2:
                matched = True
                break
        if not matched:
            return False
    return True
# 안쪽 루프는 매번 len(L2) 만큼 실행
# 바깥쪽 루프는 len(L1)번 실행
# 그러므로 안쪽 루프는 len(L1)*len(L2)

### 두 리스트의 교집합 구하기
def intersect(L1, L2):
    """가정: L1과 L2는 리스트이다.
        L1과 L2의 교집합을 반환한다."""
    #공통 원소를 담은 리스트 만들기
    tmp = []
    for e1 in L1:
        for e2 in L2:
            if e1 == e2:
                tmp.append(e1)
            break
    #중복이 없는 리스트 만들기
    result = []
    for e in tmp:
        if e not in result:
            result.append(e)
    return result
# result에 있는 모든 원소를 살펴봐야한다.
# len(result)
# len(tmp)*len(result)
# 그렇지만 L1과 L2중 짧은 길이보다 짧고 복잡도에서 덧셈항은 무시하므로
# len(L1)*len(L2)

## 지수 복잡도
### 멱집합 생성하기
def get_binary_rep(n, num_digits):
    """n과 num_digits는 음수가 아닌 정수로 가정한다.
        n의 이진 표현을 num_digits 길이의 문자열로 반환한다."""
    result = ''
    while n > 0:
        result = str(n%2) + result
        n = n//2
    if len(result) > num_digits:
        raise ValueError('num_digits가 부족합니다.')
    for i in range(num_digits - len(result)):
        result = '0' + result
    return result

def gen_powerset(L):
    """L은 리스트로 가정한다.
        L에 있는 원소로 가능한 모든 조합을 담은 리스트의 리스트를 반환한다.
        예를 들어 L이 [1,2]이면 원소가 [], [1], [2], [1,2]인 리스트를 반환한다."""
    powerset = []
    for i in range(0, 2**len(L)):
        bin_str = get_binary_rep(i, len(L))
        subset = []
        for j in range(len(L)):
            if bin_str[j] == '1':
                subset.append(L[j])
        powerset.append(subset)
    return powerset
# 첫 단계에서 이 알고리즘은 이진 숫자를 2^len(L)개 생성 
