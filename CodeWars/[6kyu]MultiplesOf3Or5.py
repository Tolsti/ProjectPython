def solution(number):
    if number < 0:
        return 0
    return sum([r for r in range(number) if r % 3 == 0 or r % 5 == 0])
