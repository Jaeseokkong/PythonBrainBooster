# 다음 함수들이 점근 복잡도는 각각 얼마인가?
def g(L, e):
    """L은 정수 리스트이고
        e는 정수이다."""
    for i in range(100):
        for e1 in L:
            if e1 == e:
                return True
    return False
# O(len(L))

def h(L, e):
    """L은 정수 리스트이고
        e는 정수이다."""
    for i in range(e):
        for e1 in L:
            if e1 == e:
                return True
    return False

# O(e*Len(L))