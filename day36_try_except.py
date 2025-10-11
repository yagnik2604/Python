

# a = input("enter the number ")
# print(f"multiplication table of {a} is:")


# try:
#     for i in range(1,11):

#          print(f"{int(a)} X {i} = {int(a)*i}")

# except:
#      print("invalid number")

try:
    num = int(input("enter num "))
    a= [6,3]
    print(a[num])

except ValueError:
    print(" ...")