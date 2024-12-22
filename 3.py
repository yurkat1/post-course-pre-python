

# number = int(input("case from 1-3: "))
# match number:
#     case 1:
#         print("aa")
#     case 2:
#         print("BB")
#     case 3:
#         print("rr")
#     case _:
#         print("wrong")

# i=1
# while i<=10 :
#     print(i, end=" ")
#     i += 1
#
# print("Test")

# i=1
# while True:
#          print(i)
#          i+=2

#
# i = 0
#
# while True:
#
#     if i == 5:
#         print("continue")
#         i += 1
#         continue
#
#     if i >= 10:
#         print("break")
#         break
#
#     print(i)
#     i += 1

#
# hw
#1. Користувач вводить із клавіатури номер дня тижня (1-7).
# Необхідно вивести на екран назви дня тижня. Наприклад, якщо 1, на екрані напис понеділок,
# 2 — вівторок тощо.
#
# try:
#     day_of_the_week = int(input("Enter number of the day of the week: "))
#
#     match day_of_the_week:
#         case 1:
#             print("Monday")
#         case 2:
#             print("Tuesday")
#         case 3:
#             print("Wednesday")
#         case 4:
#             print("Thursday")
#         case 5:
#             print("Friday")
#         case 6:
#             print("Saturday")
#         case 7:
#             print("Sunday")
#         case _:
#             print("Enter one of the numbers of the week")
#
# except Exception as e:
#     print(f"Error:{e}")
#

# 2. Користувач вводить два числа.
# Визначити, чи рівні ці числа, і, якщо ні, вивести їх на екран у порядку зростання
#
# try:
#
#     n1 = int(input("Enter 1st number: "))
#     n2 = int(input("Enter 2nd number: "))
#
#     if n1 == n2:
#         print("Equal numbers")
#     elif n1 != n2 and n1 > n2:
#         print(f"n1, n2 = {n1},{n2}")
#     else:
#         print(f"n2, n1 = {n2}, {n1}")
#
# except ValueError as e:
#     print("Enter numbers only")
# except TypeError as error:
#     print("only numbers")
# except Exception as e:
#     print("Try again")

# 3. Користувач вводить два числа та матем дію: + - * або /
#
# try:
#
#     n1 = int(input("Enter 1st number: "))
#     n2 = int(input("Enter 2nd number: "))
#     math_op = input("Enter math operation(+-*/): ")
#
#     if math_op == "+":
#         r1 = n1 + n2
#         print(f"r1= {r2}")
#     elif math_op == "-" and n1 > n2:
#         r2 = n1 - n2
#         print(f"r2= {r2}")
#     elif math_op == "*":
#         r3 = n1 * n2
#         print(f"r3 = {r3}")
#     elif math_op == "/" and n1 > n2:
#         r4 = n1 / n2
#         print(f"r4= {r4}")
#     else:
#         print("1st number must be the biggest number: ")
# except ValueError as e:
#     print("Enter numbers only")
# except Exception as e :
#     print(f"Mistake: {e}")



