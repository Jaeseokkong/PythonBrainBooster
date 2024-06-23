# 딕셔너리
month_numbers = {'Jan': 1, 'Feb': 2, 'Mar': 3, 'Apr': 4, 'May': 5, 
                 1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May'}
print(month_numbers)
print('세 번째 달: ' + month_numbers[3])
dist = month_numbers['Apr'] - month_numbers['Jan']
print('Apr와(과) Jan은(는)', dist, '달만큼 떨어져 있습니다.')

## 텍스트 번역하기
EtoF = {'bread':'pain', 'wine':'vin', 'with':'avec', 'I':'Je',
        'eat':'mange', 'drink':'bois', 'John':'Jean',
        'friends':'amis', 'and': 'et', 'of':'du','red':'rouge'}
FtoE = {'pain':'bread', 'vin':'wine', 'avec':'with', 'Je':'I',
        'mange':'eat', 'bois':'drink', 'Jean':'John',
        'amis':'friends', 'et':'and', 'du':'of', 'rouge':'red'}
dicts = {'English to French':EtoF, 'French to English':FtoE}

def translate_word(word, dictionary):
    if word in dictionary:
        return dictionary[word]
    elif word != '':
        return '"' + word + '"'
    return word

def translate(phrase, dicts, direction):
    UC_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LC_letters = 'abcdefghijklmnopqrstuvwxyz'
    punctuation = '.,;:?'
    letters = UC_letters + LC_letters
    dictionary = dicts[direction]
    translation = ''
    word = ''
    for c in phrase:
        if c in letters:
            word = word + c
        elif word != '':
            if c in punctuation:
                c = c +' '
            translation = (translation +
                           translate_word(word, dictionary) + c)
            word = ''
    return f'{translation} {translate_word(word, dictionary)}'

print(translate('I drink good red wine, and eat bread.',
                dicts,'English to French'))
print(translate('Je bois du vin rouge.',
                dicts, 'French to English'))

# 키를 사용해 값을 찾아주는 함수
def key_search(L, k):
    for elem in L:
        if elem[0] == k:
            return elem[1]
    return None

capitals = {'France': 'Paris', 'Italy': 'Rome', 'Japan': 'Kyoto'}
# 키 추출
for key in capitals:
    print(key, '의 수도는', capitals[key], '입니다.')
# 값 순회
cities = []
for val in capitals.values():
    cities.append(val)
print(cities, '은(는) 수도입니다.')
# 키/값 쌍으로 순회
for key, val in capitals.items():
    print(val, '은(는)', key, '의 수도입니다.')
