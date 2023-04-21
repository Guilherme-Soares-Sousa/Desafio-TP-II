def fila():
    password = 0
    listaSenha = []

    while True:
        menu = input("Digite 1 para pegar senha || Digite 2 para consultar || Digite S para sair\n").upper()
        if menu == "1":
            print("---MENU---")
            password += 1
            print(f"Senha impressa: {password}")
            listaSenha.append(password)

        if menu == "2":
            passwordOutput = listaSenha.pop(0)
            print(f"Senha chamada:{passwordOutput}")

        if menu == "S":
            break

    print(f"Número de senhas pós LOOP = {password}")

if __name__ == '__main__':
    fila()
