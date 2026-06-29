# Функція, що обчислює факторіал числа n рекурсивно
# Якщо n < 0 — повертає None
# Якщо n == 0 або n == 1 — повертає 1
def factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def main():
    print("Лабораторна робота №1")
    print(f"Факторіал 5: {factorial(5)}")
    print(f"Факторіал 0: {factorial(0)}")
    print(f"Факторіал -1: {factorial(-1)}")

if __name__ == "__main__":
    main()