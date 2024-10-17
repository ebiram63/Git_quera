num = input()

dic = {}
numbers = []
numbers = num.split(" ")
if len(numbers) < 200:
    for i in range(len(numbers)):
        dic.update({i+1 : numbers[i]})
    #print(dic)
    for k,i in dic.items():
        if k%6 ==0 and int(i)%6==0:
            numbers = [k,i]
            print(sorted(*numbers))