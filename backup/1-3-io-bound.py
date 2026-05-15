import requests


def io_bound_func():
    result = requests.get("https://www.icqa.or.kr")

    return result


if __name__ == "__main__":
    result = io_bound_func()
    print(result)
