# 1 Smallest of Three Numbers
#
# def smallest_number(a,b,c):
#     smallest = [a, b, c]
#     return min(smallest)
# num1, num2, num3 = int(input()), int(input()), int(input())
# print(smallest_number(num1,num2,num3))




# 2 Add and Subtract
#
#
# def sum_numbers(a, b):
#     return a+b
#
# def subtract(c):
#     return  sum_numbers(first, second) - c
#
#
# first , second , third = int(input()), int(input()), int(input())
# print(subtract(third))
#
# def add_and_subtract(a, b, c):
#     sum_of_first_two = sum_numbers(a,b)
#     return subtract(sum_of_first_two, c)
#
#
# def sum_numbers(a, b):
#     return a+b
#
#
# def subtract(sum_ot_two, c):
#     return  sum_ot_two - c
#
#
# first , second , third = int(input()), int(input()), int(input())
# print(add_and_subtract(first, second, third))



# 3 Characters in Range
#
# def characters_in_range(num1, num2):
#     for i in range(num1 +1, num2):
#         print(chr(i), end=" ")
#
#
# fist , second = input(), input()
# characters_in_range(ord(fist), ord(second))
#
#
#
# Just testing
# print(" ".join(list(map(lambda x: chr(x), range(ord(input()) +1, ord(input()))))))
#
#
# def characters_in_range(num1, num2):
#     news_list = list(map(lambda x: chr(x), range((ord(num1)) + 1, ord(num2))))
#     return news_list
#
#
# fist , second = input(), input()
# print(" ".join(characters_in_range(fist, second)))




# 4 Odd and Even Sum
#
# def odd_even_sum(number):
#     odd = 0
#     even = 0
#     for i in number:
#         if int(i) % 2 == 0:
#             even += int(i)
#         else:
#             odd += int(i)
#     return F"Odd sum = {odd}, Even sum = {even}"
#
#
# print(odd_even_sum(input()))
#
#
#
# def odd_even_sum(number):
#     odd = []
#     even = []
#     for i in number:
#         digit = int(i)
#         if digit % 2 == 0:
#             even.append(digit)
#         else:
#             odd.append(digit)
#     return F"Odd sum = {sum(odd)}, Even sum = {sum(even)}"
#
#
# print(odd_even_sum(input()))



# 5 Even Numbers
# def even_numbers(num):
#     return num % 2 == 0
#
#
# list_of_numbers = list(map(int, input().split()))
#
# print(list(filter(even_numbers, list_of_numbers)))
#
#
#
#list_of_numbers = list(map(int, input().split()))
#print(list(filter(lambda x: x % 2 == 0, list_of_numbers)))




# 6 Sort
#
#
# numbers = [int(x) for x in input().split()]
# print(sorted(numbers))
#
# def sorted_list(my_list):
#     return  sorted(my_list)
#
#
# numbers = list(map(int, input().split()))
# print(sorted_list(numbers))




# 7 Min Max and Sum
#
# def min_num(data):
#     return min(data)
#
#
# def max_num(data):
#     return max(data)
#
#
# def sum_of_nums(data):
#     return sum(data)
#
# def final_result(my_list):
#     print(F"The minimum number is {min_num(my_list)}")
#     print(F"The maximum number is {max_num(my_list)}")
#     print(F"The sum number is: {sum_of_nums(my_list)}")
#
#
# numbers = [int(x) for x in input().split()]
# final_result(numbers)




# 08 Palindrome Integers
# def palindrome(data):
#     for i in data:
#         if i == i[::-1]:
#             print("True")
#         else:
#             print("False")
#
#
# numbers = input().split(", ")
# palindrome(numbers)




# 9 Password Validator
#
# def characters_long(data):
#     if 5 < len(data) < 11:
#         return True
#     return False
#
#
# def letter_digit(data):
#     if data.isalnum():
#         return True
#     return False
#
#
# def two_digit(data):
#     digit = 0
#     for i in data:
#         if i.isdigit():
#             digit +=1
#     if digit >= 2:
#         return  True
#     else:
#         return False
#
#
# def check_password(data):
#     check_long = characters_long(data)
#     check_letter = letter_digit(data)
#     check_digit = two_digit(data)
#     if check_long and check_letter and check_digit:
#         print("Password is valid")
#     if not check_long:
#         print("Password must be between 6 and 10 characters")
#     if not  check_letter:
#         print("Password must consist only of letters and digits")
#     if not check_digit:
#         print("Password must have at least 2 digits")
#
#
# password = input()
# check_password(password)





# 10 Perfect Number

# def perfect_number(number):
#     sum_of_nums = 0
#     for i in range(1, number):
#         if number % i == 0:
#            sum_of_nums += i
#            if sum_of_nums == number:
#                return True
#
# num = int(input())
# result = perfect_number(num)
#
# if result:
#     print("We have a perfect number!")
# else:
#     print("It's not so perfect.")
#




# 11  Loading Bar


# def loading_bar(data):
#     if data == 100:
#         print("100% Complete!")
#         print("[%%%%%%%%%%]")
#         return
#     else:
#         percents = int((data / 10)) * "%"
#         dots = (10 - int((data / 10))) * "."
#         print(F"{data}% [{percents}{dots}]")
#         print("Still loading...")
#
#
# loading_bar(int(input()))
#



# 12 12. Factorial Division


def factorial(num):
    total = 1
    for i in range(num, 0, -1):
        total *= i
    return total


def factorial_division(num1, num2):
    return factorial(num1) / factorial(num2)



first, second = int(input()), int(input())

print(F"{factorial_division(first,second):.2f}")





