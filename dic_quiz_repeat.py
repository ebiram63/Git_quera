n = int(input())
dic_name = []
dic_familyname = []
if 1 <= n <= 100:
    for i in range(int(n)):
        name = input()
        dic_name.append(name.split( )[0])
        dic_familyname.append(name.split(" ")[1])
    print(dic_name,dic_familyname)