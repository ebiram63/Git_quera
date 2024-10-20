def calc(a: list) -> tuple:
    len_a = len(a)
    #print(len_a)
    max_a = max(a)
    j = 0
    for i in a:
        #print(i)
        j += i
    #average
    j = j / len_a
    #print(j)
    middle = float(len(a))/2
    if middle % 2 != 0:
        min = a[int(middle - .5)]
    else:
        min = (a[int(middle)] + a[int(middle-1)]) / 2
    return(j, min , max_a)
print(calc([2, 20, 30, 29]))