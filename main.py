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

# x = 4
# if x < 2:
#     print("x is less than 2")
# elif x > 2:
#     print("x is greater than 2")
# d = {"Germany": 25, "France": 36}
# for b in d.items():
#     print(b)
# d = {"Germany": 25, "France": 36}
# for a in d.items():
#     print(a)
# d = {"Germany": 25, "France": 36}
# for b in d.values():
#     print(b)
