def login(user, passw):
    username = input("username : ")
    password = input("password : ")
    Mikro = True
    while Mikro: 
        if username == user and password == passw:
            break
        username = input("username : ")
        password = input("password : ")
    print("Password Benar")
print(login("ahmad", "miftahu5678"))
