# # N1

# def zip_lists(list1, list2):
#     zipped_list = zip(list1, list2)
#     return [str(i) for i in zipped_list]

# list1 = [1, 2, 3]
# list2= ['a', 'b', 'c']
# zip_result = zip_lists(list1, list2)

# print(list(zip_result))

# # N2

# from functools import reduce

# def multiply_list_elements(list1):
#     try:
#         for item in list1:
#             if not isinstance(item, (int, float)):
#                 raise TypeError
            
#         return reduce(lambda x, y:x*y, list1)
#     except TypeError:
#         return "TypeError"
        
    
# num = multiply_list_elements([1, 2, 3, 4, 5])

# print(num)


# # N3

# list1 = [1, 2, 3, 4, 5, 6, 7]
# kent = lambda l1: list(filter(lambda x: x%2 !=0, l1))

# print(kent(list1))

# # N4

# def match_end(list1, str1):
#     try:
#         for item in list1:
#             if not isinstance(item, str):
#                 raise TypeError
#         return list(filter(lambda x: x.endswith(str1), list1))
#     except TypeError:
#         return "TypeError"
#     except Exception as e:
#         return f"{e}"
    
# print(match_end(['hello', 'world', 'coding', 'nod'], 'ing'))