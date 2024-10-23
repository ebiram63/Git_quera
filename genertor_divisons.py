def print_divs(n):
    list_divs = list(divs(n))
    print(list_divs)

def divs(n):
    #return list(i for i in range(1, n + 1) if n % i == 0)
    for i in range(1, n+1):
        if n % i == 0:
            yield i
            

            
               
list(divs(4))