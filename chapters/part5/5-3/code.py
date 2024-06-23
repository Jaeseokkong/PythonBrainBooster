# 리스트와 가변성
L1 = [1, 2, 3]
L2 = L1[::-1]
for i in range(len(L1)):
    print(L1[i]*L2[i])


# 리스트 비교
Techs = ['MIT', 'Caltech']
Ivys = ['Harvard',  'Yale', 'Brown']
Univs = [Techs, Ivys]
Univs1 = [['MIT', 'Caltech'], ['Harvard',  'Yale', 'Brown']]

print(Univs == Univs1)
print(id(Univs) == id(Univs1))
print(Univs is Univs1)

Techs.append('RPI')
print('Univs =',Univs)
print('Univs1 =',Univs1)

L1 = [[]]*2
L2 = [[], []]
for i in range(len(L1)):
    L1[i].append(i)
    L2[i].append(i)
print('L1 =', L1, '/', 'L2 =', L2)


def append_val(val, list_1 = []):
    list_1.append(val)
    print(list_1)

append_val(3)
append_val(4)

L1 = [1,2,3]
L2 = [4,5,6]
L3 = L1 + L2
print('L3 = ', L3)
L1.extend(L2)
print('L1 =', L1)
L1.append(L2)
print('L1 =', L1)

## 복제
def remove_dups(L1, L2):
    """L1과 L2를 리스트로 가정한다.
        L2에도 등장하는 L1의 원소를 삭제한다."""
    for e1 in L1:
        if e1 in L2:
            L1.remove(e1)
L1 = [1,2,3,4]
L2 = [1,2,5,6]
remove_dups(L1, L2)
print('L1 =', L1) #L1 = [2, 3, 4]

## 리스트 내포
def f(expr, old_list, test = lambda x : True):
    new_list = []
    for e in iterable:
        if test(e):
            new_list.append(expr(e))
    return new_list

print([e**2 for e in range(6)])

[x for x in range(2, 100) if all(x % y != 0 for y in range(2, x))]