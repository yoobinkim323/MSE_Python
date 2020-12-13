def print_max(a, b, c) : #함수 정의
    if a > b and a > c: #a가 b보다 크고 c보다 크면
        print(a) #a를 출력하세요
    elif b > c and b > a: #그렇지 않고 b가 c보다 크고 a보다 크면
        print(b) #b를 출력하세요
    else: #그렇지 않다면 
        print(c) #c를 출력하세요
        
print_max(10,20,30) #print_max 함수 실행