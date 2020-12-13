ohlc = [["open", "high", "low", "close"],
        [100, 110, 70, 100],
        [200, 210, 180, 190],
        [300, 310, 300, 310]] #리스트 생성
profit = 0 #profit을 0으로 정의
for row in ohlc[1:]: #2번째 리스트부터 마지막 리스트까지
    profit += (row[3] - row[0]) #profit의 값에 (4번째 항목 값-1번째 항목 값)을 더하세요
print(profit) #profit의 값을 출력하세요