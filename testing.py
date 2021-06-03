# import threading
class Rr:
    def __init__(self,bot):
        self.bot=bot
    def display(self):
        print(self.bot)
obj= Rr("myname")
obj.display()


class Rext:
    def __init__(self,rob):
        self.rob=rob
    def display(self):
        print(self.rob)
t=Rext("is pawan")
t.display()

if __name__=="__main__":
    t1=threading.Thread(target=__init__)
    t2=threading.Thread(target=__init__)
    t1.start()
    t2.start()
    t1.join()


