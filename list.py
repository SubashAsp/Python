print("List\n")
#creating list
a = [1, 2, 3]
print(a)

#having different different datatypes
b = [1, "subash", True]
print(b)

#list length
print(len(b))

#allow duplicates
c = [1, 2, 3, 1]
print(c)

#indexing
print(c[1:3])

#negative indexing
print(c[-3:-1])

#list constructor
d = list(("subash", 22, "Erode"))
print(d)
print(type(d))

#checking if the item exits
if "subash" in d:
    print("Yes, item exits.")

#change list items
print("\nChanging list items.")

#change item value / replacing
e = [1, 2, 3, 5]
e[3] = 4
print(e)

#concat two strings
print("concat two strings : ", e + [6, 7, 8, 9])

#change a range of items
e[1:3] = 5, 6
print(e)

#inserting for than replace
e[1:2] = 7, 8
print(e)

#adding to list / append
f = [1, 8, 27]
print(f)
f.append(64)
f.append(5 ** 3)
print(f)

#extend
f.extend([9, 10])
print(f)
f.extend

#insert
f.insert(-1, 11)
print(f)
f.insert(3, 100)
print(f)

#remove
g = f
g.remove(100)
print(g)
"""
g.remove(100,64)
print(g)
can pass only one argument
"""
#pop
h = [1, 2, 3, 4, 5]
h.pop(1)
print(h)

#clear
h.clear()
print(h)

#index
i = [1, 2, 3, 4, 5]
print("index value : ", i.index(5))
#--index for string
j = "Subash"
print(j.index("u"))
