"""n! означает n × (n − 1) × ... × 3 × 2 × 1
Например, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
и сумма цифр в числе 10! равна 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
Найдите сумму цифр в числе 100!."""

n = 100
n_factorial = 1
result = 0

for i in range(1, n + 1):
    n_factorial *= i
for i in str(n_factorial):
    result += int(i)

print(result)
