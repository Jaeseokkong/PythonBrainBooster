# 추상 데이터 타입과 클래스
## 클래스 정의 예시
class Toy(object): # object의 서브클래스
    def __init__(self):
        self._elems = []
    def add(self, new_elems):
        """new_elems는 리스트이다."""
        self._elems += new_elems
    def size(self):
        return len(self._elems)

# 이 클래스에 연관된 속성은 __init__, add, size 이다

print(type(Toy))
print(type(Toy.__init__), type(Toy.add), type(Toy.size)) #모두 function 타입의 객체
# 매직메서드 : 특수한 함수 이름의 시작과 끝에 두 개의 밑줄 문자를 사용한다.

## 인스턴스 생성
s = Toy()
# __init__이 실행되고 _elems를 만든다. (_elems는 Toy 인스턴스의 데이터 속성이다.)

t1 = Toy()
print(type(t1))
print(type(t1.add)) # method
t2 = Toy()
print(t1 is t2) # False


t1 = Toy()
t2 = Toy()
t1.add([3,4])
t2.add([4])
print(t1.size() + t2.size()) # 3


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
    
s = IntSet()
s.insert(3)
print(s.member(3)) # True
s.insert(4)
print(str(s))
print('s의 값:', s)