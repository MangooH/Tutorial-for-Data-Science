import math

n, m = map(int, input().split())

bundle, piece = 1001, 1001
for _ in range(m):
    b, p = map(int, input().split())
    if b < bundle:
        bundle = b
    if p < piece:
        piece = p


print(min(math.ceil(n / 6) * bundle, piece * n, (n // 6) * bundle + (n % 6) * piece))
