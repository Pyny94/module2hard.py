import random

n = list(range(3,20))
x = random.choice(n)
result = ''
print(x)
for i in range(1,x):
    for j in range(i+1,x):
        if x % (int(i) + int(j)) == 0  and i < j:
            result.append(i)
            result.append(j)

print(result)

