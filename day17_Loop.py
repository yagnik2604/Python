

# name= "Abhikesh"

# for i in name:
#     print(i, end=",")


# color = ["green", "blue", "red", "yellow"]

# for i in color:
#     print(i)


# # if we want to use for loop for specific number 

# for k in range(5):
#     print(k)

# for k in range(4,8):
#     print(k)

# three parameter of range
# for i in range(0, 10, 2):   # start, stop, step 
#     print(i)

# for i in range(10, 0, -2):
#     print(i)

colors = ["grenn", "red", "blue", "yellow"]

for col in colors:
    print(col)
    if col == "blue":
        break
else:
    print("nothing")
# Note: The else block will NOT be executed if the loop is stopped by a break statement.    

i=0
while i < 5:
    print(i)
    i +=1
else:
    print(f"i is more then or equal to 5 {i}")