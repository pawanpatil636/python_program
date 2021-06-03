# while True:
#     try:
#         num1=int(input())
#         num2=int(input())
#         res=num1+num2
#         print("the addition is:",res)
#     except:
#         print("please enter a valid number")
#     else:
#         print("thankyou")
#     finally:
#         print("thankyou for believing in us")
                         
#------------------------------------------------------------------------------


class BalanceException(Exception):
    pass
def Bank():
    amount=100
    withdraw=50
    balance=amount-withdraw
    try:
        if balance<30:
            raise BalanceException("minimum balance should be 30/")
        else:
            print("your balance is",balance)
    except BalanceException as e:
        print(e)
Bank()
                                              