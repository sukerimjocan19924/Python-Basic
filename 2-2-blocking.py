import time


def blocking_task(name, seconds):
    print(f"{name} 시작")
    time.sleep(seconds)
    print(f"{name} 끝")


print("=====Blocking 방식=====")

start = time.time()

blocking_task("작업 1", 3)
blocking_task("작업 2", 2)

end = time.time()

print(f"총 걸린 시간 : {end-start: .2f}초")
