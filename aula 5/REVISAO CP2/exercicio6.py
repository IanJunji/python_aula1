user = input("Usuario: ")
senha = input("Senha: ")
while user == senha:
    print("A senha não pode ser igual o usuário. Por favor, tente novamente.")
    senha = input("Senha: ")
print("Usuário e senha cadastrados.")