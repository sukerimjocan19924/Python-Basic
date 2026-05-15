import asyncio
import time

start = time.time()


async def fetch_data(name, seconds):
    print(f"{name} 요청 시작")
    await asyncio.sleep(seconds)
    print(f"{name} 응답 완료")


async def main():
    await asyncio.gather(
        fetch_data("요청 1", 2), fetch_data("요청 2", 4), fetch_data("요청 3", 3)
    )
    end = time.time()
    print(f"총 걸린 시간 : {end-start: .2f}초")


asyncio.run(main())
