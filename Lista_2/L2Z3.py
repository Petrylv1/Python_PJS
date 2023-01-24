import random

class TMacierz():
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.macierz = [[random.randint(0,100) for i in range(m)] for j in range(n)]
    
    def __str__(self):
        return '\n'.join('\t'.join(str(el) for el in row) for row in self.macierz)

    def __add__(self, other):
        result = TMacierz(self.n, self.m)
        for i in range(self.n):
            for j in range(self.m):
                result.macierz[i][j] = self.macierz[i][j] + other.macierz[i][j]
        return result

    def __sub__(self, other):
        result = TMacierz(self.n, self.m)
        for i in range(self.n):
            for j in range(self.m):
                result.macierz[i][j] = self.macierz[i][j] - other.macierz[i][j]
        return result

    def __mul__(self, other):
        result = TMacierz(self.n, self.m)
        for i in range(self.n):
            for j in range(self.m):
                result.macierz[i][j] = self.macierz[i][j] * other.macierz[i][j]
        return result


macierz1 = TMacierz(3,4)
macierz2 = TMacierz(3,4)
macierz3 = macierz1+macierz2
print(macierz3)