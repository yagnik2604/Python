
# name = "yagnik"

# for character in name:  # character is variable & name is string container name 
#     print(character)



# fruit = "Mango"
# len1 = len(fruit)
# print("Mango is a", len1, "letter word.")


# pie = "Applepie"
# print(pie[:5])
# print(pie[5:])
# print(pie[2:6]) 



# a= "this is string"

# b = a.split(" ")

# print(b)

# c = '-'.join(b)

# print(c)


#  immutable string to mutable string 

# def mutate_string(string, position, character):
#     out = string[:position] + character + string[position+1:]
#     return out


# a = mutate_string("applepie" , 5,'z')

# print(a)




# def count_substring(string, sub_string):
   
#     count = 0
#     for i in range(len(string)):
#         if sub_string == string[i:len(sub_string) + i]:
#             count += 1
#     return count


# a = count_substring("ABCDCDC", "CDC")
# print(a)





s = "python"

# Indexes:   0  1  2  3  4  5
# Chars:     P  y  t  h  o  n
# Negative: -6 -5 -4 -3 -2 -1


# print(s[0:])
# print(s[2:])
# print(s[:4])
# print(s[:6])
# print(s[1:5])
# print(s[0:6:2]) # 'Pto'  (take every 2nd character from index 0 to 5)

#  reverse index


# Indexes:   0  1  2  3  4  5
# Chars:     P  y  t  h  o  n
# Negative: -6 -5 -4 -3 -2 -1


print(s[::])
print(s[:-1])
print(s[-3:]) #(last 3 chars)
print(s[::])  # means "take everything from start to end"
print(s[::2]) #Take every 2nd element from start to end
print(s[::-1]) #Take all elements in reverse
print(s[::-2]) #Take every 2nd element from end 
print(s[::-5])
