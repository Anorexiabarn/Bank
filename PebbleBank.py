# Start
print("Välkommen till Pebbles Bank") # Printar ut början av programmet
# Login Details
print("pinkoden = 1221") # printar pinkoden så du inte glömmer
pin = 1221 # En vaiabel som är pinkodet til programmet.
userPin = int(input("Skriv in din pinkod: ")) # Det här variabeln gör så man måste skriva in pin och om det är fel så stängs programmet av.
if pin != userPin: # detta gör så om man skriver fel pinkod så stängs programmet av.
    exit()

# Saldo
saldo = 0.0 # En variabel som visar start saldot

print("Detta KAN vara ditt hela saldo eller inte")
# sparar saldo till fil
file = open("money.txt", 'r+') # öppnar din txt fil och om det inte finns så skapar det än
money = file.read() # läser filen
file.close() # stänger ner fil
file = open("money.txt", "w") # öppnar filen och gör så man kan skriva in i det.
print(money) # skriver ut money
# Menu
menu = 0 # En variabel

menuList = ("Insättning(1), Uttag(2), Kommer snart(3), Avsluta(4) ") # En variabel som är en menylista och ordern man vill det ska vara.
# Menu 1 insättning
# Menu 2 uttag
# Menu 3 övrigt
# Menu 4 avsluta
while menu == 0:
    menu = int(input("Insättning [1], uttag [2], övrigt [3], avsluta [4]: ")) # Vad du vill göra närdu loggat in, skriver du något annat än ett heltal så går den tillbaka med hjälp av Else satsen längre ned
    if menu == 1: # Insättning
        insättning = float(input("Hur mycket vill du sätta in? ")) # Insättningen är en float, vilket gör att du kan skriva decimaltal
        saldo = saldo + insättning # plusar ihop ditt saldo med insättning
        print(saldo) # Skriver ut ditt saldo
        
        menu = 0 # går tillbaka så du kan välja meny

    elif menu == 2: # Uttag
        uttag = float(input("Hur mycket vill du ta ut? "))
        saldo = saldo - uttag # tar ditt saldo - de du vill ta ut.

        if saldo < 0: # Om du har negativt saldo får du en varning om att pengarna är slut
            print("Yikes due fattig") # printar ut detta om du försöker ta ut mer än vad du har.
            menu = 0
        print(saldo) # printar ut saldo
        menu = 0
    
    elif menu == 3: # Inte gjort något här än men här kan fler funktioner läggas in
        print("Coming soon.. så testa någon annan meny")
        menu = 0 # går tillbaka till menyn

    elif menu == 4: # Stänger av
        print("Hejdå, vi synes nästa gång du ska på snabbare.com")
        file.write(str(saldo)) # Det skriver in ditt saldo i filen
        exit() # stänger av programet

    else:
        menu = 0 #Går tillbaka till menyn om du har skrivit fel eller något liknande
