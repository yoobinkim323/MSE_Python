import random #random 모듈 불러오기


class Account: #클래스 생성
    account_count = 0 #초기값=0

    def __init__(self, name, balance): #생성자 생성
        self.deposit_count = 0 #입금 횟수 0
        self.deposit_log = [] #리스트 만들기
        self.withdraw_log = [] #리스트 만들기

        self.name = name #예금주
        self.balance = balance #잔액
        self.bank = "SC은행" #은행이름

        num1 = random.randint(0, 999) #0과 999까지의 수 중 랜덤으로
        num2 = random.randint(0, 99) #0과 99까지의 수 중 랜덤으로
        num3 = random.randint(0, 999999) #0과 999999까지의 수 중 랜덤으로

        num1 = str(num1).zfill(3)  #3자리로 변경 ('1'->'001')
        num2 = str(num2).zfill(2)  #2자리로 변경 ('1'->'01')
        num3 = str(num3).zfill(6)  #6자리로 변경 ('1'->'000001')
        self.account_number = num1 + '-' + num2 + '-' + num3  #계좌번호 3자리-2자리-6자리
        Account.account_count += 1 #계좌 개수
        
    @classmethod
    def get_account_num(cls): #생성된 계좌의 개수를 출력
        print(cls.account_count)  #Account.account_count

    def deposit(self, amount): #method 추가
        if amount >= 1: #입금이 1원 이상이라면
            self.deposit_log.append(amount) #입금 내역 리스트로 저장
            self.balance += amount #잔고+입금 금액

            self.deposit_count += 1 #입금 횟수 1증가
            if self.deposit_count % 5 == 0: #입금 횟수가 5의 배수이면
                self.balance = (self.balance * 1.01) #1% 이자 지급


    def withdraw(self, amount): #method 추가(출금)
        if self.balance >= amount: #잔고가 출금 요청액 이상이면
            self.withdraw_log.append(amount) #출금 내역 리스트로 저장
            self.balance -= amount #잔고-출금 요청액

    def display_info(self): #method 추가
        print("은행이름: ", self.bank) #은행이름 출력
        print("예금주: ", self.name) #예금주 출력
        print("계좌번호: ", self.account_number) #계좌번호 출력
        print("잔고: ", self.balance) #잔고 출력

    def withdraw_history(self): #method 추가
        for amount in self.withdraw_log: #입금 내역
            print(amount) #입금 내역 출력

    def deposit_history(self): #method 추가
        for amount in self.deposit_log: #출금 내역
            print(amount) #출금 내역 출력


k = Account("Kim", 1000) #처음에 1000원
k.deposit(100) #100원 입금
k.deposit(200) #200원 입금
k.deposit(300) #300원 입금
k.deposit_history() #입금 내역 출력

k.withdraw(100) #100원 출금
k.withdraw(200) #200원 출금
k.withdraw_history() #출금 내역 출력

