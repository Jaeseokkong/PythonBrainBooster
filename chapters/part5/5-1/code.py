#튜플
t1 = (1, 'two', 3)
t2 = (t1, 3.25)
print(t2)
print((t1 + t2))
print((t1 + t2)[3])
print((t1 + t2)[2:5])


def intersect(t1, t2):
    """t1과 t2를 튜플이라고 가정한다.
        t1과 t2에 모두 있는 원소를 담은 튜플을 반환한다."""
    result = ()
    for e in t1:
        if e in t2:
            result += (e, )
    return result

print(intersect((1, 'a', 2), ('b', 2, 'a')))

# 복수 할당
def find_extreme_divisors(n1, n2):
    """n1과 n2가 양의 정수라 가정한다.
        n1과 n2의 1보다 큰 가장 작은 공약수와 가장 큰 공약수를 담은 튜플을 반환한다.
        1보다 큰 공약수가 없으면 (None, None)을 반환한다."""
    min_val, max_val = None, None
    for i in range(2, min(n1, n2) + 1):
        if n1%i == 0 and n2%i == 0:
            if min_val == None:
                min_val = i
            max_val = i
    return min_val, max_val

min_divisor, max_divisor = find_extreme_divisors(100, 200)
print(min_divisor, max_divisor)

