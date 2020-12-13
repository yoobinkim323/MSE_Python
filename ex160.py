리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py'] #리스트 생성
for 변수 in 리스트: #리스트 안의 항목 개수만큼 for문 반복
  split = 변수.split(".") #변수를 .를 기준으로 쪼갠다-리스트로 담김
  if (split[1] == "h") or (split[1] == "c"): #2번째 항목이 h이거나 c라면
    print(변수) #변수 값 출력
