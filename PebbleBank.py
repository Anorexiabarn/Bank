# Start
print("Välkommen till Pebbles Bank")
# Login Details
pin = 1221
userPin = int(input("Skriv in din pinkod: "))
if pin != userPin:
    exit()

# Saldo
saldo = 0.0


# Menu
menu = 0

menuList = ("1.insättning 2.uttag 3. logga ut 4. valuta: ")
print(menuList)
# Menu 1 insättning
# Menu 2 uttag
# Menu 3 valuta
# Menu 4 logga ut
while menu != 3:
    menu = int(input("Skriv ditt val: "))
    if menu == 1:
        insättning = float(input("Hur mycket vill du lägga in?: "))
        saldo = saldo + insättning
        print(saldo)
    elif menu == 2:
        uttag = float(input("Hur mycket vill du ta ut? "))
        saldo = saldo - uttag
        print(saldo)
        if saldo <= 0:
            print("Saik! due fattig")
    elif menu == 3:
        print("loggar ut")
        break
    elif menu == 4:
        print(saldo)

    else:
        print("Fel/avsluta")

# skapa en text fil som sparar saldo

file = open("money.txt", 'r+')
money = file.read()
file.write(str(saldo))
print(money)
file.close()

#f = open("money.txt", 'a')
#f.write(str(saldo))
#f.close()
