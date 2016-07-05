# Uses python2


def get_change(n):
    change = 0
    while (n != 0):
        if (n > 10):
            n -= 10
            change += 1
        elif (n > 3):
            n -= 3
            change += 1
        else:
            n -= 1
            change += 1
    return change


n = int(raw_input())
print get_change(n)
