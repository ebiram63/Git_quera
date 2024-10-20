n = int(input())
dic_name = {}
if 1 <= n <= 100:
    for i in range(int(n)):
        name = input()
        dic_name.update({name.split(" ")[1] : name.split(" ")[0]})
#print(dic_name)
dic_name_repeated = {}
for i in dic_name.values():
    #print(i)
    if i in dic_name_repeated:
        dic_name_repeated.update({i : int(dic_name_repeated[i]) + 1})
    else:
        dic_name_repeated.update({i : 1})
print(max(dic_name_repeated.values()))