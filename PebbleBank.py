# Start
print("Välkommen till Pebbles Bank") # Printar ut början av programmet
# Login Details
pin = 1221 # En vaiabel som är pinkodet til programmet.
userPin = int(input("Skriv in din pinkod: ")) # Det här variabeln gör så man måste skriva in pin och om det är fel så stängs programmet av.
if pin != userPin:
    exit()

# Saldo
saldo = 0.0 # En variabel som visar start saldot

# skapa en text fil som sparar saldo

file = open("money.txt", 'r')
money = file.readline()
file.close()

# Menu
menu = 0 # En variabel

menuList = ("1.insättning 2.uttag 3. logga ut 4. valuta: ") # En variabel som är en menylista och ordern man vill det ska vara.
print(menuList) # printar ut menuList
# Menu 1 insättning
# Menu 2 uttag
# Menu 3 valuta
# Menu 4 logga ut
while menu != 3: # Detta gör så att sålänge man inte skriver 3 så loopar programmet om och om igen
    menu = int(input("Skriv ditt val: "))
    if menu == 1: # Detta variabeln är en if och det är "om" så om menu == 1 så går den till insättning till saldot.
        insättning = float(input("Hur mycket vill du lägga in?: ")) # Detta har en float som är för heltal+decimaler och så ska man skriva in de tal man vill lägga in.
        saldo = saldo + insättning # En variabel som är saldot + de insättning man lägger till.
        print(saldo) # printar saldot.

        open("file", "w")
        file.write(str(saldo))
        file.close()
        
    elif menu == 2: # Detta variabel har en elif som är "else/if" och då går programmet till menu 2
        uttag = float(input("Hur mycket vill du ta ut? ")) # Detta variabel uttag gör så att du ska skriva hur mycket du vill ta ut.
        saldo = saldo - uttag # En variabel som visar saldo - uttaget man gör
        print(saldo) # printar ut saldot
        if saldo <= 0: # Detta if sats gör så om man ska ta ut pengar och tar ut så man har mindre en 0 så går det inte.
            print("Saik! due fattig") # printar ut detta om man försöker ta ut mer än vad man har.
    elif menu == 3: # Det stänger av och breakar loopen.
        print("loggar ut") # printar ut detta om man "loggar ut"
        break # breakar loopen
    elif menu == 4: # Det printar ut de saldot du har på kontot
        print(saldo) # printar saldot.

    else: # Detta gör så om man inte väljer något av de menyvalerna så händer detta.
        print("Fel/avsluta") # printar ut om man skriver in fel meny
        break # breakar loopen


#f = open("money.txt", 'a')
#f.write(str(saldo))
#f.close()
