import time


def delivery(name, mealtime):
    print(f"{name}에게 배달 완료")

    time.sleep(mealtime)
    print(f"{name}식사 완료, {mealtime}초 소요")
    print(f"{name}에게 그릇 수거 완료")


def main():
    delivery("A", 5)
    delivery("B", 3)
    delivery("C", 4)


start = time.time()

main()

end = time.time()

print(f"전체 실행 시간 : {end-start: .2f}초")
