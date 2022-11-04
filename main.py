import signal
import time
from signal import SIGINT

# class GracefulKiller:
#     kill_now = False
#     def __init__(self):
#         signal.signal(signal.SIGINT, self.exit_gracefully)
#         signal.signal(signal.SIGTERM, self.exit_gracefully)
#
#     def exit_gracefully(self, **args):
#         self.kill_now = True
#
# if __name__ == '__main__':
#     killer = GracefulKiller()
#     while not killer.kill_now:
#         time.sleep(1)
#         print("Doing something")
#     print("End of the program")

# def fac(number):
#     result = 1
#     for i in range(2, number + 1):
#         result *= i
#     return result
#
# while True:
#     user_input = int(input("Enter a number: "))
#     print(fac(user_input))
#
# fac()
#


# def fac(number: int):
#     if number < 0:
#         return None
#     result = 1
#     for i in range(2, number+1):
#         result *= i
#     return result
# while True:
#     user_input = int(input("Enter a number: "))
#     result = fac(user_input)
#     if result is None:
#         print("Error during calculation")
#     else:
#         print(result)
# def my_sum(*parameters):
#     s = 0
#     for p in parameters:
#         s += p
#     return s
# x = my_sum(1,2,3,4,5,6,7,8,9)
# print(x)
# def function(a, b, **other):
#     print("Fixed parameters:", a, b)
#     print("Other parameters", other)
#
# function(1,2)
# function(1,2, johannes="ernesti", jackson="john")
# def function(*positional, **keyword):
#     print("Positional arguments are: ", positional)
#     print("Keyword arguments are: ", keyword)
#
# function(1,2,3,4,5, john="johnson", jack="jones")
# def f(a, b, *args, d, e, **kwargs):
#     print(a, b, args, d, e, kwargs)
#
# f('a','b',3,4,5,6, d=5, e=6, jet=6)

# def f(a, b, /, c, d):
#     print(a, b, c, d)
#
# f("help", "me", "get", "better")
# x = 1
# if x == 1:
#     print("x has value 1")
# if x == 2:
#     print("x has value 2")

# x = 4         // Loop examples
# if x < 2:
#     print("x is less than 2")
# elif x > 2:
#     print("x is greater than 2")
# d = {"Germany": 25, "France": 36}
# for b in d.items():
#     print(b)
# d = {"Germany": 25, "France": 36}
# for a in d.items():  // .items() retrieves the values of the dictionary objects
#     print(a)
# d = {"Germany": 25, "France": 36}
# for b in d.values():
#     print(b)
# translations = {
#     "Germany": "Deutschland",
#     "Spain": "Spanien",
#     "France": "Frankreich"
# }
# # print(len(translations.items()))
# translations["Bahamas"] = "Costa Rica"
# print(translations)
# print(translations["Germany"])
# print("Germany" in translations)
# print("Georgia" in translations)
# d = {}
# d |= {"France": "Spanien"} // | allows you to assign items to dictionary
# print(d)
# e = translations.copy() // using the .copy operator to copy values of dict to another dict
# print(e)
# lst = [1,2,3,4,5,9,13,26] /// list comprehensions
# x = [x**2 for x in lst]   // initializing variable to another list to perform operations on it.
# print(x)
# account = {
#     "owner": "Steve Miller",
#     "account_number": 567123,
#     "account_balance": 12350.0,
#     "max_daily_turnover": 1500,
#     "turnover_today": 10.0
# }
#
#
# def new_account(owner, account_number, account_balance,
#                 max_daily_turnover=1500):
#     return {
#         "owner": owner,
#         "account_number": account_number,
#         "account_balance": account_balance,
#         "max_daily_turnover": max_daily_turnover,
#         "turnover_today": 0
#     }
#
#
# # x = new_account("josh Nichols", 2353, 10000000000000, 1)
# # print(x)
# def money_transfer(source, destination, amount):
#     if (amount < 0 or
#             source["turnover_today"] + amount > source["max_daily_turnover"] or
#             destination["turnover_today"] + amount >
#             destination["max_daily_turnover"]):
#         return False
#     else:
#         source["account_balance"] == amount
#         source["turnover_today"] += amount
#         destination["account_balance"] += amount
#         destination["turnover_today"] += amount
#         return True
#
#
# # x = new_account("josh Nichols", 1234, 1234513215) // assigning x to new_account function
# # y = new_account("Steve Miller", 123456, 12221) // assigning y to new_account function
# # z = money_transfer(x,y,1501) // performing a money transfer between the source=x and dest=y
# # print(z)
# # def show_balance(account):  // creating a function for showing account balance for new_account funct
# #     print("Account of {}".format(account["owner"]))
# #     print("Balance of account is {:.2f} USD".format(account["account_balance"]))    // pay special attention to the formatting {:.2f} .format method for float that is 2 digits wide.
# #     print("(Today already {:.2f} of {} USD turned over)".format(account["turnover_today"], account["max_daily_turnover"]))
#
# x = new_account("Josh Nichols", 158967851, 123488531684)
# print(show_balance(x))
