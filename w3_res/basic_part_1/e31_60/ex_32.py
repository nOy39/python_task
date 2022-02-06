
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def mcd(num1, num2):
    return (n / gcd(n, m)) * m


n = 15
m = 17
print(int(mcd(n, m)))
