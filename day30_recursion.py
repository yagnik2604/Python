



def fibonaci(n):

    if n <= 1 :

        return n

    return fibonaci(n-2)+fibonaci(n-1)



c = fibonaci(4)
print(c)