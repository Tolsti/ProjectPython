def fib(n):
    result, fib_1, fib_2 = 0, 0, 1
    for _ in range(n):
        result = fib_2
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    return result


def productFib(prod):
    result, prod_1, prod_2 = False, 0, 0
    for r in range(prod + 1):
        prod_1, prod_2 = fib(r), fib(r + 1)
        if prod_1 * prod_2 >= prod:
            if prod_1 * prod_2 == prod:
                result = True
            break
    return [prod_1, prod_2, result]
