class Recursion():

    x = 3

    def __init__(self):
        pass

    def tailrecursion(self, n: int):
        if n > 0:
            print(f"{n}")
            self.tailrecursion(n - 1)

    def headrecursion(self, n: int):
        if n > 0:
            self.headrecursion(n - 1)
            print(f"{n}")

    def staticvariable(self, n: int):
        if n > 0:
            lectureCode.x += 1
            return self.staticvariable(n - 1) + lectureCode.x
        else:
            return 0

    def treerecusion(self, n: int):
        if n > 0:
            print(f"{n}")
            self.treerecusion(n - 1)
            self.treerecusion(n - 1)

    def headrecursionfactorial(self, n: int):
        if n > 1:
            return n * self.headrecursionfactorial(n - 1)
        else:
            return 1

    def tailrecursionfactorial(self, n: int, a: int = 1):
        if n > 1:
            return self.tailrecursionfactorial(n - 1, n * a)
        else:
            return a

    def headrecursionsumnumbers(self, n: int):
        if n == 0:
            return 0
        else:
            return n + self.headrecursionsumnumbers(n - 1)

    def tailrecursionsumnumbers(self, n: int, a=0):
        if n == 0:
            print(f"n:{n} -> a:{a} ")
            return a
        else:
            print(f"n:{n} -> a:{a} ")
            return self.tailrecursionsumnumbers(n - 1, n + a)

    # m=base
    # n=power
    def tailrecursionPower(self, power: int, base: int, a: int = 1):
        if power == 0:
            print(f"n:{power} -> a:{a} ")
            return a
        else:
            print(f"n:{power} -> a:{a} ")
            return self.tailrecursionPower(power - 1, base, base * a)

    def headrecursionPower(self, power: int, base: int):
        if power == 0:
            print(f"n:{power} ")
            return 1
        else:
            print(f"n:{power} ")
            return base * self.headrecursionPower(power - 1, base)

    def fastpower(self, power: int, base: int):
        if power == 0:
            print(f"n:{power} ")
            return 1
        if power % 2 == 0:
            print(f"n:{power} ")
            return self.headrecursionPower(power / 2, base * base)
        elif power % 2 != 0:
            print(f"n:{power} ")
            return base * self.headrecursionPower((power - 1) / 2, base * base)


if __name__ == "__main__":
    t1 = Recursion()
    # t1.tailrecursion(n)
    # t1.headrecursion(3)
    # print(self.staticvariable(3))
    # t1.treerecusion(3)
    print(t1.headrecursionfactorial(5))
    print(t1.tailrecursionfactorial(5))
    # print(t1.headrecursionsumnumbers(100))
    # print(t1.tailrecursionsumnumbers(5))
    # print(t1.tailrecursionPower(3, 4))
    # print(t1.headrecursionPower(3, 4))
    # print(t1.fastpower(3, 4))
"""
Tail Recursion -> If all the operations are performed 
inside a recursive method at calling time then it is
called as tail recursion ,any operation happening at 
return time will not be counted uner tail recursion 

Note : Tail Recursion can be directly converted to 
loops and

Head Recursion -> If all the operations are performed 
inside a recursive method at returning time ,then 
it is called head recursion 
"""