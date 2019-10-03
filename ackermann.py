def ack(m, n):
    if m == 0:
        return n + 1
    elif m > 0:
        if n == 0:
            return ack(m - 1, 1)
        elif n > 0:
            return ack(m - 1, ack(m, n - 1))
    return None

if __name__ == "__main__":
    print(ack(3, 4))