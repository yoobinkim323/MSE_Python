date = ['09/05', '09/06', '09/07', '09/08', '09/09'] #리스트 생성
close_price = [10500, 10300, 10100, 10800, 11000] #리스트 생성
close_table = dict(zip(date, close_price)) #두 개의 리스트를 합쳐 딕셔너리 생성
print(close_table) #close_table 값 출력
