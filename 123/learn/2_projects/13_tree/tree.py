# create tree
print("tree")
i = 10

tree = "A"
# generate white space on left side
star =  " " * i + "*"
tree = " " * i + tree
trunk = "_" *i + "|| " + "_" * (i-1)

print("\n"+star)
while i >= 1:
    print(tree)
    tree = tree[1:]
    tree += "AA"
    i +=-1
print(trunk)
