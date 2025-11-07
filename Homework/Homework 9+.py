def smth(data):
    list_2 = []

    if isinstance(data, dict):
        for k, v in data.items():
            list_2.extend(smth(k))
            list_2.extend(smth(v))
    elif isinstance(data, (list, tuple, set)):
        for i in data:
            list_2.extend(smth(i))
    else:
        list_2.append(data)

    return list_2

x = [45, 2.58, 39, True, (18.7, "text", 47, {11, 58, False}), {'title': 'The wolf', 'pages': 256}, 10.25, 45]

print(smth(x))