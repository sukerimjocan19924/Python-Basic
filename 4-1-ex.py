# cook_ramen(customer, cook_time)
import time


def cook_ramen(customer, cook_time):
    print(f"손님 {customer} 주문 접수")

    time.sleep(cook_time)
    print(f"손님 {customer}라면 끊이는 중...")
    print(f"{cook_time}초 대기")
    print(f"손님 {customer} 라면 완성!")


def main():
    cook_ramen("A", 5)
    cook_ramen("B", 3)
    cook_ramen("C", 4)


start = time.time()

main()

end = time.time()

print(f"전체 걸린 시간 : 약{end-start: .0f}초")
