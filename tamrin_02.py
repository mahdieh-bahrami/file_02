s = 0
c = 0
n = "tamrin_02f.txt"
file = open(n,"w")
for i in range(10):
    print(f"enter number {i+1} : ", end='')
    x = int(input())
    s += x
    c += 1
    file.write(str(x))
    file.write("\n")
file.write(str(c))
file.write("\n")
file.write(str(s))
file.close()
print(c)
print(s)