def fibonacci(n):
    assert n >= 0 and int(n) == n, "Fibonacci number cant be negative or non integer"
    if n in [0, 1]:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(4)) 


# fibonacci(4)
# ├── fibonacci(3)
# │   ├── fibonacci(2)
# │   │   ├── fibonacci(1)
# │   │   └── fibonacci(0)
# │   └── fibonacci(1)
# └── fibonacci(2)
#     ├── fibonacci(1)
#     └── fibonacci(0)