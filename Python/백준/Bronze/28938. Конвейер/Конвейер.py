n = int(input())
arr = list(map(int, input().split()))
result = 0

for i in arr:
    result += i
    
if result > 0:
    print("Right")
elif result == 0:
    print("Stay")
else:
    print("Left")