# 람다 표현식 작성
# 두 번째 인수가 0이면 None, 그렇지 않으면 첫 번째 인수를 두 번째 인수로 나눈 값을 반환
f = lambda i, j : None if j == 0 else i / j
print(f(4,0), f(4,2))