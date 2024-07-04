# 검색 알고리즘
## 선형 검색과 간접 참조로 원소에 접근하기
# for i in range(len(L)):
#     if L[i] == e:
#         return True
# return False
# 파이썬에서는 리스트 원소를 이렇게 파악한다.
# e가 리스트에 없을 경우 O(len(L))번 수행


## 이진 검색과 가정 활용
### 정렬된 리스트의 선형 검색
def search(L, e):
    """L은 리스트로 가정한다.
        e가 L에 있으면 True 그렇지 않으면 False르 반환한다."""
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False
# 평균 실행 시간이 개선(최악일 때 L의 모든 원소를 검사해야 하므로 복잡도 변동없음)

## 재귀를 사용한 이진 검색 구현
def search(L, e): #래퍼 함수
    """L은 리스트로 가정한다.
        e가 L에 있으면 True 그렇지 않으면 False르 반환한다."""
    
    def bin_search(L, e, low, high): #헬퍼 함수
        #high - low를 줄인다.
        if high == low:
            return L[low] == e
        mid = (low + high)//2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: #찾을 수 없음
                return False
            else:
                return bin_search(L, e, low, mid-1)
        else:
            return bin_search(L, e, mid+1, high) # mid+1인 이유 mid번째를 이미 봤으므로L[mid] > e 맞지 안으므로 그다음 번째를 low로 넘김
    
    if len(L) == 0:
        return False
    else:
        return bin_search(L, e, 0, len(L) - 1)
# 래퍼 함수 : 클라이언트 코드용 인터페이스 제공
# bin_search 복잡도는 재귀 호출의 횟수에 따라 다름
# 감소 함수 => high-low(감소 함수의 값이 0에 도달하면 재귀 종료)
# high-low == 0이 되기 최대 log2(high-low)번 연산
# search의 복잡도는 O(log(len(L)))
