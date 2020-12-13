class Stock: #클래스 정의
    def __init__(self, name, code, per, pbr, 배당수익률): #생성자 정의
        self.name = name
        self.code = code
        self.per = per
        self.pbr = pbr
        self.배당수익률 = 배당수익률

종목 = [] #리스트 생성

삼성 = Stock("삼성전자", "005930", 15.79, 1.33, 2.83) #객체 생성
현대차 = Stock("현대차", "005380", 8.70, 0.35, 4.27) #객체 생성
LG전자 = Stock("LG전자", "066570", 317.34, 0.69, 1.37) #객체 생성

종목.append(삼성) #리스트에 추가
종목.append(현대차) #리스트에 추가
종목.append(LG전자) #리스트에 추가

for i in 종목: #i=삼성,현대차,LG전자
    print(i.code, i.per) #각 종목의 종목코드와 per 출력