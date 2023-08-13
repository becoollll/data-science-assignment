n = int(input())
for i in range(1, n+1): 
    temp = i
    for j in range(1, i+1):
        if i < 10:
            print("...", i, end="", sep="")
        elif i >= 10 and i < 100:
            print("..", i, end="", sep="")
        elif i >= 100 and i < 1000:
            print(".", i, end="", sep="")
        i += temp
    if i < n+1:
        print("\n")