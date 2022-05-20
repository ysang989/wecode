def answer(num):
    for i in range(1,51):
        if num % 2 == 0:
            return print("짝수입니다")
        
        else:
            return print("홀수입니다")
            
num = int(input("1부터 50 사이의 자연4수를 입력하시오: "))
answer(num)