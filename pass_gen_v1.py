import string
import secrets

def menu_main():
    while True:
        print(" - [PASSWORD GENERATOR]")
        print(" - [1] Go to password menu")
        print(" - [2] End program ")
        
        select_m = input("\n - Select a option: ")
        if select_m == '1':
            menu_2()
        elif select_m == '3':
            print("Program closed")
            break
        else:
            print("ERROR! Invalid option.")

def menu_2():
    while True:
        print("[PASSWORD GEN MENU]")
        print("[1] - Start a generation")
        print("[2] - Return")

        select_r = input("\n - Select a option: ")

        if select_r == '1':
            max = int(input("Place a maximum caracters you need in your password: "))
            pass_Generator = ''.join(secrets.SystemRandom().choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(max)) # '' = Separador -- ascii metodo -- Letras, numeros e symbolos
            print(pass_Generator)
        elif select_r == '2':
            print("Program closed")
            return
        else:
            print("ERROR! Invalid option.")
menu_main()