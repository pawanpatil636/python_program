#tuple to list and then append
u="tuple","deep","git",
o=list(u)
print(o)
o.append(54)
print(o)
u=tuple(o)
print(u)

#tuple unpacking
t="pop",26,"gender",
name,age,gender=t
print(name)

num=(2,3,4,5,6,7)
a, *b, c = num
print(a)
print(b)
print(c)

#&
num=(2,3,4,5,6,7)
a, b, *c = num
print(a)
print(b)
print(c)

#checking index value
x=(1,2,3,4,5)
print(x.index(2))

#multiplication
num=(1,2,3,4,5)*3
print(num)

#tuple using loop 
y="rty",90,54,
for i in y:
    print(i)

##   
a=[1,2,3,4,5]
b=a
a[2]=4
print(b)

##with the use of built in function
Tuple1 = tuple('Geeks') 
print("\nTuple with the use of function: ") 
print(Tuple1)

#split function
name="xciencia technologies"
n=name.split()
print(n)

#split by taking input from user
name=input()
n=name.split()
print

#using join 
c="-".join(n)
print(c)