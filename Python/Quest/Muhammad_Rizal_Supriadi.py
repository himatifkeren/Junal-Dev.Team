def login(user,passw):
    username = input("username :")
    password = input("password :")
    logik = True
    while logik:
        if username == user and password == passw:
            break
        elif username !=user and password !=passw:
            print("Username dan password anda salah")
        elif username != user:
            print("Username anda salah")
        else:
            print("Password anda salah")
        username = input("username : ")
        password = input("password : ")
    print("Password Benar")
print(login('rizal','rizal123'))


