import asyncio


class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def compute(self, x):
        return self.a * x + self.b


class QuadraticEquation(Equation):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

    def compute(self, x):
        return self.a * x ** 2 + self.b * x + self.c


async def find_root_binary_search(equation, left, right, precision):
    middle = (left + right) / 2
    if ((middle - left) < precision or (right - middle) < precision):
        return middle

    while True:
        await asyncio.sleep(0.01)
        if (equation.compute(middle) > 0):
            print("Computing")
            right = middle
        else:
            left = middle
        middle = (left + right) / 2
        if (middle - left) < precision or (right - middle) < precision:
            print(middle)
            return middle


async def main():
    task1 = find_root_binary_search(Equation(2, -3), 0, 2, 0.001)
    task2 = find_root_binary_search(QuadraticEquation(1, 0, -4), -2, 4, 0.001)
    task3 = find_root_binary_search(QuadraticEquation(3, -2, -1), 0, 5, 0.001)
    await asyncio.gather(task1, task2, task3)

asyncio.run(main())
