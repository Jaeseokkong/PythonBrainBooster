# 예외 처리하기
##제어 흐름을 위해 예외 사용하기
def get_ratios(vect1, vect2): 
    """가정: vect1와 vect2은 동일 길이의 숫자 리스트입니다.
       반환: vect1[i]/vect2[i]의 값을 담은 리스트""" 
    ratios = [] 
    for index in range(len(vect1)): 
        try: 
            ratios.append(vect1[index]/vect2[index]) 
        except ZeroDivisionError: 
            ratios.append(float('nan')) #nan = Not a Number 
        except: 
            raise ValueError('잘못된 인수로 get_ratios가 호출되었습니다') 
    return ratios 

try: 
    print(get_ratios([1, 2, 7, 6], [1, 2, 0, 3])) 
    print(get_ratios([], [])) 
    print(get_ratios([1, 2], [3])) 
except ValueError as msg:
    print(msg) 


##try-except를 사용하지 않은 제어 흐름
def get_ratios(vect1, vect2): 
    """가정: vect1와 vect2은 동일 길이의 숫자 리스트입니다.
       반환: vect1[i]/vect2[i]의 값을 담은 리스트""" 
    ratios = [] 
    if len(vect1) != len(vect2): 
        raise ValueError('잘못된 인수로 get_ratios가 호출되었습니다') 
    for index in range(len(vect1)): 
        vect1_elem = vect1[index] 
        vect2_elem = vect2[index] 
        if (type(vect1_elem) not in (int, float)) \
            or (type(vect2_elem) not in (int, float)): 
            raise ValueError('잘못된 인수로 get_ratios가 호출되었습니다') 
        if vect2_elem == 0: 
            ratios.append(float('NaN')) #NaN = Not a Number 
        else: 
            ratios.append(vect1_elem/vect2_elem) 
    return ratios 

### 아래 코드 사용필요
#### 사용자에게 입력을 받고 에러가 나면 다시 입력 요청
while True:
    val = input('정수를 입력하세요: ')
    try:
        val = int(val)
        print('입력한 정수의 제곱:', val**2)
        break #while루프 벗어나기
    except ValueError:
        print(val, '은(는) 정수가 아닙니다.')
#### 코드의 수가 증가한다는 단점있음.

#### 코드 수를 줄임
def read_int():
    while True:
        val = input('정수를 입력하세요: ')
        try:
            return (int(val)) #반환하기 전에 str을 int로 바꾼다.
        except ValueError:
            print(val, '은(는) 정수가 아닙니다.')

## 어떤 타입의 입력도 요청할 수 있도록 함수를 일반화
def read_val(val_type, request_msg, error_msg):
    while True:
        val = input(request_msg + ' ')
        try:
            return(val_type(val)) #str을 val_type으로 바꿈
        except ValueError:
            print(val, error_msg)
    
