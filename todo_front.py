from todo_back import *
import os

class menu():
    def main():   
        #smyčka pro menu
        while True:
            #Vymazani konzole pro přehlednost
            os.system('cls')
            print("\nTo Do list aplikace")
            print("1. Pridani poznamky")
            print("2. Zobrazeni poznamek")
            print("3. Vymazat poznamku")
            print("4. Označit důležitou poznámku")
            print("5. Upravit stávající poznámku")
            print("6. Odejít")
            
            volba = int(input("Zadejte číslo volby: "))
            if volba == 1:
                pridani_poznamky()
            elif volba == 2:
                zobrazeni_poznamek()
            elif volba == 3:
                vymazat_poznamku()
            elif volba == 4:
                oznacit_dulezitost()
            elif volba == 5:
                upraveni_poznamky()
            elif volba == 6:
                break
            else:
                print("Špatně zadaná hodnota volby.")
    #spusti smyčku main - neboli menu teto aplikace
    main()