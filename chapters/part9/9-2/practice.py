# 다음 사양을 만족하는 함수
def find_an_even(L):
    """L은 정수 리스트로 가정한다.
        L에 있는 첫 번째 짝수를 반환한다.
        L에 짝수가 없으면 ValueError 예외를 발생시킨다."""
    for i in L:
        if i%2 == 0:
            return i
    # 예외를 지정
    raise ValueError('L에 짝수가 없다.')
  

print(find_an_even([1,2,4,5,6]))