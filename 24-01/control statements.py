#break statement
print("Break statement")

for n in range(2, 10):
    for j in (2, n):
        if n % j == 0:
            print(n, j)
            break

# continue statement
for x in range(20):
    if x % 2 == 0:
        continue
    else:
        print(x)

# pass
if True:
    pass