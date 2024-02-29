class Problem:
    def __init__(self):
        self.k = int(input())
        self.a, self.b, self.c, self.d = map(int, input().split(" "))

    def solve(self):
        ax_b = self.a * self.k + self.b
        cx_d = self.c * self.k + self.d

        if ax_b == cx_d:
            print(f"Yes {ax_b}")
        else:
            print("No")
        
if __name__ == "__main__":
    problem = Problem()
    problem.solve()