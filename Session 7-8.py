for i in range(1,10,2):
    print(i)

s=0
for i in range(1,11):
    s += i
    s=int(s)

print("")
print(s)

s=0
i=1

while i <= 10:
    s += i
    i += 1
    print(s)

print("")
s="Hello"
print(s)

print("")

print(",.'\"")

s="hello!"
print(s[2],s[4],s[-1])

s1="hello"
s2="world"

print(s1+' '+s2)

print(3*(s2+' '))

print(int((10/2))*s1)

print((10//2)*s1)

print(len(s1))

print(3*len(s1))

print("")

for c in s2:
    print(c)

for c in s1:
    print(c*4)

for c in s1:
    print(c*4, end=" ")

new_string =""
for c in s2:
    new_string += c*4
print(new_string)

print("h" in s1)
print("d" in s2)
print("x" in s1)
print("Wor" in s2)

print(s[1:4],s[6:9])
print(s[:4])