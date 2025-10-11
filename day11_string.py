
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


def solve(s):
    s=str(s)
    listylist=s.split(' ')
    lengthofname=len(listylist)
    i=0
    newname=[]
    for words in listylist:
        i=i+1
        newwords=words.capitalize()
        newname.append(newwords)
        if i==lengthofname:
            break
    newname=' '.join(newname)
    return str(newname)

print(__name__)
if __name__ == "__main__":
 a = "apple alpha"
 p = solve(a)

 print(p)
 print(__name__)