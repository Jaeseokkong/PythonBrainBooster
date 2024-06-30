# IntSet 클래스 아래에 다음 사양을 만족하는 메서드 추가

## IntSet 클래스
class IntSet(object):
    """IntSet은 정수 집합이다.
        #(추상이 아닌) 구현에 관한 정보:
        # 한 집합의 값은 정수 리스트 self._vals로 표현된다.
        # 집합에 속한 정수는 self.vals에 정확히 한 번만 등장한다"""
    
    def __init__(self):
        """빈 정수 집합을 만든다."""
        self._vals = []

    def insert(self, e):
        """e는 정수라고 가정하고 self에 추가한다."""
        if e not in self._vals:
            self._vals.append(e)

    def member(self, e):
        """e는 정수라고 가정한다.
            e가 self에 있으면 True, 아니면 False를 반환한다."""
        return e in self._vals
    
    def remove(self, e):
        """e는 정수라고 가정한다.
            e를 self에서 제거한다. e가 self에 없다면 ValueError가 발생한다."""
        try:
            self._vals.remove(e)
        except:
            raise ValueError(str(e) + '을(를) 찾기 못했습니다.')
    
    def get_members(self):
        """self._vals에 담긴 리스트를 반환한다.
            원소의 순서는 보장되지 않는다."""
        return self._vals[:]
    
    def __str__(self):
        """self의 문자열 표현을 반환한다."""
        if self._vals == []:
            return {}
        self._vals.sort()
        result = ''
        for e in self._vals:
            result = result + str(e) + ','
        return f'{{{result[:-1]}}}'
    
    # 추가 메서드
    def union(self, other):
        """other는 IntSet 객체이다.
            self와 other에 있는 원소를 포함하도록 self를 수정한다."""
        for e in other.get_members():
            self.insert(e)

s1 = IntSet() 
s1.insert(1) 
s1.insert(2)
s2 = IntSet() 
s2.insert(2) 
s2.insert(3) 
s1.union(s2)
print(s1) 
            