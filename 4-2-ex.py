# cook_ramen(customer, cook_time)
import time
import asyncio


async def cook_ramen(customer, cook_time):
    print(f"손님 {customer} 주문 접수")
    print(f"손님 {customer}라면 끊이는 중...")

    await asyncio.sleep(cook_time)

    print(f"{customer} 라면 완성! ({cook_time}초)")
    print(f"{customer}에게 라면 제공 완료")
    print()


async def main():
    await asyncio.gather(cook_ramen("A", 5), cook_ramen("B", 3), cook_ramen("C", 4))


start = time.time()

asyncio.run(main())

end = time.time()

print(f"전체 걸린 시간: {end - start:.2f}초")
