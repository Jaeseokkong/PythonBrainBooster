# 테스트
def is_smaller(x, y):
    """x와 y는 int로 가정한다.
        x가 y보다 작으면 True, 그렇지 않으면 False를 반환한다."""
    if x < y:
        return True
    else:
        return False
    
## 블랙박스 테스트
### 블랙막스 테스트는 테스트할 코드를 보지 않고 구성한다.
def sqrt(x, epsilon):
    """x, epsilon은 float이고, x >= 0, epsilon > 0라고 가정한다.
        x-epsilon <= result*result <= x+epsilon인 result를 반환한다."""

def copy(L1, L2):
    """L1, L2는 리스트라고 가정한다.
        L2를 L1의 복사본으로 만든다."""
    while len(L2) > 0: #L2의 모든 원소를 삭제한다.
        L2.pop() #L2의 마지막 원소를 삭제한다.
    for e in L1: #L1의 원소를 L2에 추가한다.
        L2.append(e)

## 글라스박스 테스트
def is_prime(x): 
    """x는 음수가 아닌 정수로 가정합니다. 
       x가 소수이면 True, 그렇지 않으면 False를 반환합니다""" 
    if x <= 2: 
        return False 
    for i in range(2, x): 
        if x%i == 0: 
            return False 
    return True 
# 2인 경우 False

def abs(x): 
    """x는 int라고 가정합니다.
       x>=0이면 x를, 그렇지 않으면 –x를 반환합니다""" 
    if x < -1: 
        return -x 
    else: 
        return x
# -1인 경우 -1반환
