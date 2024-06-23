# sum 함수를 사용해 숫자로 이루어진 튜플의 평균 계산하는 함수
t = range(0, 10)
def eval_sum (t):
    return sum(t) / len(t)

print(eval_sum(t))