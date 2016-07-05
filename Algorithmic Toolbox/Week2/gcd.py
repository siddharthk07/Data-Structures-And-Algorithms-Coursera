# uses python2
def gcd(a, b):
    while b:
        (a, b) = (b, a % b)
    return a


if __name__ == "__main__":
    a, b = map(int, raw_input().split())
    print gcd(a, b)
