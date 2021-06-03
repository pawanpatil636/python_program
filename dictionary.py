'''z={"name":"pawan","age":23,"salary":500000}
print(z)'''

'''z=dict(name="patil",age=34)
for i,j in z.items():
    print(i,j)'''

'''z=dict(name="patil",age=34)
x={"name":"pawan","age":23,}
y=(z,x)
a=dict(y)
w=a.popitem()
print(w)'''

'''z={"name":"patil","age":34}
x=[1,2,"python"]
w=(34,76,"java")
e={w:"dsf"}
print(e)'''


'''z={"name":"patil","age":34}
x={"name2":"pawan","1age":4}
w=[z,x]
s=w[0]
s["name"]="asqwas"
print(s)'''

'''z={"name":"patil","age":34}
x={"name2":"pawan","iage":4}
z=zip(z,x)
q=dict(z)
print(q)'''

#general statement for for else
'''z=[1,2,3,4,5]
for i in z:
    print(i)
else:
    print("notpresnt")'''

'''z={"name":"patil","age":34}
print(z.pop("name"))'''

#copy
'''z={"name":"patil","age":34}
x={"name2":"pawan","iage":4}
e=z.copy()
e.update({'name1':"gagan"})
print(e)

w=["asdf",34,True,False,101]'''

# def gd(  **kwargs):
#     for i in kwargs.keys():
#         print(i)
# gd(name="gagandeep",age="33")

# name=("gagan","pawan","dilip") 
# def fun(*name):
#     for i in name:
#         print(i)
# fun(*name)

l=[1,2,3,4,5,6,7]
k=[]
for i in range(1,8):
    if i==1:
        print(i)
    else:
        k.append(i)
print(k)
print(l[6])

   
# for i in l:
    # print(i)


