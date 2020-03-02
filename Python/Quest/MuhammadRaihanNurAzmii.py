passwordnya = "RaihanTamvan"
usernamnya = "Raihan"
input_password = ""
input_password2 = ""
password_coba = 1
password_terkunci = False

while input_password != passwordnya and not(password_terkunci) and input_password2 != usernamnya:
    if password_coba <= 3:
        input_password2 = input("Lebetkeun A Usernamena : ")
        input_password = input("Lebetkeun A passwordna : ")
    else: 
        password_terkunci = True
    password_coba = password_coba + 1

if password_terkunci :
    print("Password kakonci slurd kusabab anjeun parantos salah 3 kali")
else :
    print ("Anjayy benar")


# # username = "Muhammad Raihan Nur Azmii"
# password = "Azmii"
# input_password = ""
# # input_username = ""

# while input_password is not password  :
#     input_password = input("Lebetkan A Password na : ")
#     # input_username - input("Lebetkan A Username na : ")

# print ("Benerrrrr")

