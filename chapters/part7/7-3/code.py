#파일
name_handle = open('kids', 'w') # kids 파일 생성, w(쓰기모드)
for i in range(2):
    name = input('이름을 입력하세요:')
    name_handle.write(name + '\n')
name_handle.close()

with open('kids', 'r') as name_handle:
    for line in name_handle:
        print(line)