low_prices  = [100, 200, 400, 800, 1000] #리스트 생성
high_prices = [150, 300, 430, 880, 1000] #리스트 생성

volatility = [] #volatility 변수는 리스트
for i in range(len(low_prices)) : #i는 0,1,2,3,4-for문 5번 반복
    volatility.append(high_prices[i] - low_prices[i]) #(고가-저가)값을 volatility에 추가
print(volatility) #volatility 값 출력