# 리스트의 고차 연산
def apply_to_each(L, f):
    """L은 리스트이고 f는 함수로 가정한다.
        L의 각 원소 e를 f(e)로 변경한다."""
    for i in range(len(L)):
        L[i] = f(L[i])

L = [1, -2, 3.33]
print('L =', L)
apply_to_each(L, abs) # 절대값
print('L =', L)
apply_to_each(L, int) # int
print('L =', L)
apply_to_each(L, lambda x : x**2) # 제곱
print('L =', L)

# map 사용
for i in map(lambda x : x**2, [2, 6, 4]):
    print(i)

L1 = [1, 28, 36]
L2 = [2, 57, 9]
for i in map(min, L1, L2):
    print(i)