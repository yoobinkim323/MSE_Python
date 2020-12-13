def 함수0(num) : #함수 정의
    return num * 2 #num 값*2

def 함수1(num) : #함수 정의
    return 함수0(num + 2) #(num의 값+2)*2

def 함수2(num) : #함수 정의
    num = num + 10 #num의 값+10
    return 함수1(num) #함수1(num)실행

c = 함수2(2) #함수2 실행 num=2 ->2+10=num ->함수1 실행 (12+2)*2
print(c) #c의 값 출력
