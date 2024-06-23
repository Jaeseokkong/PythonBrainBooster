# 다음 출력 예상
L = [1, 2, 3]
L.append(L)
print(L is L[-1]) # True

# 2와 100 사이의 소수가 아닌 정수를 생성하는 리스트 내포
x = [x for x in range(2, 100) if any(x % y == 0 for y in range(2, x)) == False]

print(x)
