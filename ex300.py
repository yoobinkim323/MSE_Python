per = ["10.31", "", "8.00"] #문자열로 된 per 생성

for i in per: #for문 3번 반복
    try: 
        print(float(i)) #실수로 바꿔 출력-에러 발생(공백)
    except: #예외가 발생한다면
        print(0) #0을 출력
    else:  #예외가 발생하지 않는다면
        print("clean data") #clean data 출력
    finally: #예외가 발생하던지 안하던지
        print("변환 완료") #변환 완료 출력

