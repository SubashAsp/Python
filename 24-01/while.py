print()
print("While loop")
#while loop

# syntax
# while <expression>:
#       <statement(s)>

a = 5
while a > 0:
    print(a)
    a -= 1

b = ['subash', 'karthi', 'deepan']
while b:
    print(b.pop(-1))

"""
--> while <expr>:
|    <statement>
|    <statement>
|    break  >-------
|    <statement>   |
|    <statement>   | 
---< continue      |
    <statement>    |
    <statement>    |
                   |
<statement>  <-----
"""
print()
# break and continue statements in while
print('break')
c = 5
while c > 0:
    if c == 2:
        break
    print(c)
    c -= 1
print('loop ended.')

print('continue')

d = 10
while d > 0:
    d -= 1
    if d % 2 == 0:
        continue
    print(d)
print('loop ended')

# using else clause

#syntax
# while <expr>:
#   <statement(s)>
# else:
#   <additional statement(s)>

print('else clause')
e = 5
while e > 0:
    print(e)
    e -= 1

else:
    print("loop ended")

# adding additional statements before else clause
f = 5
while f > 0:
    f -= 1
    print(f)
    if f % 2 == 0:
        break

else:
    print('loop ended')

# to find a element in list
g = [1, 2, 3, 4, 5]
h = 3
i = 0
while i < len(g):
    if g[i] == h:
        print(f'index of {h} is {i}')
        break
    i += 1
else:
    print('loop completed.')

# infinite loop

# while True:
#     print('yes ')

#nested while

j = ['subash', 'karthi']
while len(j):
    print(j.pop(0))
    k = ['erode', 'Tamil Nadu']
    while len(k):
        print('>>',k.pop(0))

print('one line code')
# one line while code
l = 5
while l > 0: print(l); l -= 1
