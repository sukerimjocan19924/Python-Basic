import sys

sys.set_int_max_str_digits(0)


def cpu_bound_func(number: int):
    total = 1

    arrage = range(1, number + 1)

    for i in arrage:
        for j in arrage:
            for k in arrage:
                total *= i * j * k

    return total


if __name__ == "__main__":
    result = cpu_bound_func(10)

    print(result)
