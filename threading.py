'''import threading
import time
def printfun():
    for i in range(20):
        print(i)
        time.sleep(5)

# threads=[]
for k in range(5):
    t=threading.Thread(target=printfun)
    #threads.append(t)
    t.start()'''

'''
import threading
def cube(num):
    print(f"cube:{num*num*num}")    
    #or   
    # print(f"cube:{num*num*num}")
def square(num):
    print(f"square:{num*num}")

if __name__=="__main__":                  #used because this program should run from this file only
    t1=threading.Thread(target=cube,args=(10,))
    t2=threading.Thread(target=square,args=(10,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
'''


a = [3,1,0,4,5,7,10,54,78]
n=len(a)
print(n)
for i in range(n-1):
    for j in range(0,n-i-1):
        if a[j] > a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)