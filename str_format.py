#formatting a string
name="p1"
age=34
salary=23423423
print(f"my name is {name} and salary {salary}, my age is {age}")


#or 

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))


x = "apple", "banana", "cherry",
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)