def fibonacci(n: int) -> int:
    if n == 0: 
        return 0

    l = 0
    r = 1
    for i in range(1, n):
        temp = r 
        r = l + r 
        l = temp
    return r


if __name__ == "__main__":
    for i in range(0, 11):
        print(i, ":", fibonacci(i))