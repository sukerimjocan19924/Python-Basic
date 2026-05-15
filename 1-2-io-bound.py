import time


def io_bound_func():
    time.sleep(2)

    return "I/O 작업 완료"


if __name__ == "__main__":

    start = time.time()

    result = io_bound_func()

    end = time.time()

    print(result)

    print(f"실행시간: {end-start: .4f}")
