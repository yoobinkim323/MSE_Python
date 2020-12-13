import requests #다른 사람이 만든 모듈을 불러오는 것
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data'] #딕셔너리로 가져옴

변동폭 = float(btc['max_price']) - float(btc['min_price']) #최고가와 최저가의 차이를 변동폭으로 정의
시가 = float(btc['opening_price']) #opening_price를 시가로 정의
최고가 = float(btc['max_price']) #max_price를 최고가로 정의

if (시가+변동폭) > 최고가: #시가+변동폭의 값이 최고가의 값보다 크다면
    print("상승장") #상승장을 출력하세요.
else: #그렇지 않다면
    print("하락장") #하락장을 출력하세요.
