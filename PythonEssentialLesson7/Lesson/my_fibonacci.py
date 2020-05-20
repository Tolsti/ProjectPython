def fibonacci_sequence():
    first, second = 0, 1
    while True:
        yield second
        first, second = second, first + second


def fibonacci(limit):
    generator = fibonacci_sequence()
    for _ in range(limit):
        yield next(generator)


def nth_fibonacci(number):
    result = None
    for current in fibonacci(number):
        result = current
    return result


if __name__ == '__main__':
    print('Running Fibonacci tests...')
    assert nth_fibonacci(1) == 1
    assert nth_fibonacci(2) == 1
    assert nth_fibonacci(3) == 2
    assert nth_fibonacci(4) == 3
    print('End running tests')
