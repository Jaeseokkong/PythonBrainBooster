# 매직 메서드와 해싱 가능 타입
## 매직 메서드 사용하기
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


class Toy(object):
    def __init__(self):
        self._elems = []

    def add(self, new_elems):
        """new_elems는 리스트이다."""
        self._elems += new_elems
    
    def __len__(self):
        return len(self._elems)

    def __add__(self, other):
        new_toy = Toy()
        new_toy._elems = self._elems + other._elems
        return new_toy
    
    def __eq__(self, other):
        return self._elems == other._elems
    
    def __str__(self):
        return str(self._elems)
    
    def __hash__(self):
        return id(self)

    
t1 = Toy()
t2 = Toy()
t1.add([1, 2])
t2.add([3, 4])
t3 = t1 + t2
print('t3의 값', t3)
print('t3의 길이', len(t3))
d = {t1: 'A', t2: 'B'}
print(d[t1], '은(는) 키 t1에 연관된 값이다.')