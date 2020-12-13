def message1(): #함수 정의
    print("A") #A를 출력

def message2(): #함수 정의
    print("B") #B를 출력

def message3(): #함수 정의
    for i in range (3) : #i는 0,1,2-for문 3번 반복
        message2() #message2() 함수 실행
        print("C") #C 출력
    message1() #message1() 함수 실행

message3() #message3() 함수 실행-message2()함수를 실행하므로 B 출력->C 출력->for문 반복->message1()함수를 실행하므로 A 출력
