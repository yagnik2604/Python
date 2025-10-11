
# info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info)


# # accessing single values
# print(info['name'])
# print(info.get('age'))

# # accessing multiple values
# print(info.values())

# # accessing keys
# print(info.keys())

# # accessing key-value pairs
# print(info.items())


ep = {122:45, 123:89, 567:69, 670:69}
ep2 = {222:67, 566:90}

# ep.update(ep2)

# ep.clear()

# ep.pop(122)

ep.popitem()  #remove last pair values

# del ep[122] # delete selected values
# del ep    # delete whole dictionary

print(ep)
