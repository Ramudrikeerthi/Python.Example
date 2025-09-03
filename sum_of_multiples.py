import sys

def sum_mult(k, n):
    m = (n - 1) // k
    return k * m * (m + 1) // 2

it = iter(sys.stdin.read().strip().split())
t = int(next(it))
out = []
for _ in range(t):
    n = int(next(it))
    out.append(str(sum_mult(3, n) + sum_mult(5, n) - sum_mult(15, n)))
print("\n".join(out))
