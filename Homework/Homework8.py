# N1

# def first(n):
#     num_1 = 0
#     num_2 = 1
#     for x in range(n):
#         print(num_1)
#         num_1, num_2 = num_2, num_1 + num_2


# first(5)





# N2

# def is_anagram(str1, str2):
#     str1_list = list(str1)
#     str2_list = list(str2)
#     str1_list.sort()
#     str2_list.sort()
#     print(str1_list, str2_list)
#     print(str1_list == str2_list)


# is_anagram("rob", "bro")



# N3

# def factorial(num):
#     mult = 1
#     for i in range(1, num + 1):
#         mult *= i
#     print(mult)

# factorial(3)



# N4

# def count_symbols(str1, symbol):
#     count = 0
#     for i in str1:
#         if i == symbol:
#             count +=1
#     print(count)
#     print(str1.count(symbol))

# count_symbols("hhhhhahhah", "a")