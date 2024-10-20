import re
def check_registration_rules(**kwargs):
    usernames = []
    for username, password in kwargs.items():
        flag = 0
        while True:
            if (len(password) < 6):
                flag = -1
                break
            elif (len(username) <=  4):
                flag = -1
                break
            elif (username == "quera"):
                flag = -1
                break
            elif (username == "codecup"):
                flag = -1
                break
            elif (password.isnumeric()):
                flag = -1
                break
            else:
                flag = 0
                #print("Valid Password")
                break

        if flag == 0:
            
            usernames.append(username)
    return(usernames)
check_registration_rules(username='password', sadegh='He3@lsa')
