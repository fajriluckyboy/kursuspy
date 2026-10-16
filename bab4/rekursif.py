def faktorial(n):
    """
    Menghitung faktorial secara rekursif.
    Base case: n == 1
    Recursive case: n * faktorial(n - 1)
    """
    if n == 1:
        return 1
    return n * faktorial(n - 1)


def fibonacci(n):
    """
    Menghitung bilangan fibonacci ke-n.
    Base case: n == 0 atau n == 1
    Recursive case: fib(n-1) + fib(n-2)
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print("=== Faktorial ===")
for i in range(1, 8):
    print(f"{i}! = {faktorial(i)}")

print("=== Fibonacci ===")
for i in range(10):
    print(f"fib({i}) = {fibonacci(i)}")
