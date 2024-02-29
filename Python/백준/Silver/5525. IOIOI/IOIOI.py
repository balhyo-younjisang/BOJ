class Problem:
    def __init__(self):
        self.n = int(input())
        self.m = int(input())
        self.s = input()

        self.p = "IOI" + "OI" * (self.n - 1)
        self.cnt = 0

    def solve(self):
        for idx in range(0, self.m):
            if self.s[idx] == "I" and self.check(idx):
                self.cnt += 1

    def check(self, idx):
        p_len = len(self.p)
        for i in range(0, p_len):
            if i + idx >= self.m:
                return False
            elif self.s[idx + i] != self.p[i]:
                return False
        
        return True

    def output(self):
        print(self.cnt)
    

if __name__ == "__main__":
    problem = Problem() 
    problem.solve()
    problem.output()