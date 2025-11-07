# # N1

# int_list = [10,20,30,40]

# def x1(num1):
#     global int_list
#     int_list.append(num1)

# x1(50)
# print(int_list)



# # N2
# int_list = [100, 20, 30, 50, 5323, 3321, 22, 56, 700, 90, 10]
# def x2(list1):
#     num_sum = 0
#     for item in list1:
#         num_sum += item

#     return num_sum

# print(x2(int_list))


# # N3
# gl_str = "Global"

# def x3():
#     gl_str = "Local"
#     return gl_str

# print(x3())


#  # N4

# def recursive_sum(number):
#     if number < 10:
#         return number
#     else:
#         return (number % 10) + recursive_sum(number // 10)    

# print(recursive_sum(12345))

# # N5

# def recursive_reverse(str1):
#     if len(str1) == 1:
#         return str1
#     else:
#         return str1[-1] + recursive_reverse(str1[:-1])   
    
# print(recursive_reverse("Hello"))
