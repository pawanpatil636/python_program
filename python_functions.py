                                    #FUNCTIONS_IN_PYTHON

#function must be defined and called to get output
'''def function():
    print("hello world")
function()  '''  

'''def func(name):
    print("my name is",name)
func("pawan")'''


'''def func(name,surname):  #parameters
    print("my name is",name,surname)
func("pawan","patil")'''  #giving the arguments for the parameters

'''def func(name,surname="patil"):
    print("my name is",name,surname)
func("pawan")
func("pawan","kulkarni")'''

'''def func(): #taking the input from the user
    a=int(input())
    b=int(input())
    print("addition of a and b is:",a+b)
func()'''

'''def func(a,b): #using conditional statements
    if a>b:
        print("true",a)
    else:
        print("false",b)
func(2,4)'''

'''def fun(*students):
    for i in students:
        print(i)
fun("pawan","patil")'''

'''def func(a,b):
    for i in range(a,b):
        if a>b:
            print("greater")
            break
        else:
            print("smaller")
func(20,10)'''

'''def my(*kids):
    print("the youngest child is" + kids[2] )
my("pradeep","nitin","harish")'''

'''def func(name3,name2,name1):
    print("my name is",name3)
func(name1="pawan",name2="patil",name3="gagan")'''

'''def func(**name):
    print("my name",name["id"])
func(myname="patil",id="sdfsdf") '''


'''a=(input().split())
def fun(food):
    for i in food:
        print(i)
fun(a)'''

'''def fun(par):

    return(int(list[0])+int(list[1]))
    print(fun(li))'''






