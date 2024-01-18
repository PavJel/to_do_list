import json

#funkce nacist_poznamky() slouzi k nacteni souboru JSON file
def nacist_poznamky():
    try:
        with open('seznam_poznamek.json', 'r') as file:
            nactene_poznamky = json.load(file)
        return nactene_poznamky
    except FileNotFoundError:
        return []
#funkce ulozit_poznamky() slouzi k ulozeni hodnot zadané uživatelem
def ulozit_poznamky(poznamky):
    with open('seznam_poznamek.json', 'w') as file:
        json.dump(poznamky, file, indent=2)

#funkce pridani_poznamky() slouzi k pridani hodnoty do seznamu poznamky, ktery se nachazi v souboru JSON, ktere uzivatel zadal
def pridani_poznamky():
    poznamka = input("Zadej novou poznamku: ")
    poznamky = nacist_poznamky()
    #append - metoda pro přidání hodnoty
    poznamky.append(poznamka)
    ulozit_poznamky(poznamky)
    print("Poznamka byla uspešně přidána.")
    
    input("Stiskněte jakoukoliv klávesu pro návrat do menu.")

#funkce zobrazeni_poznamek() slouzi k zobrazeni poznamek v konzoli
def zobrazeni_poznamek():
    poznamky = nacist_poznamky()
    #len - délka objektu
    if len(poznamky) == 0:
        print("Nemáte žádné poznámky.")
    else:
        print("Seznam poznámek:")
        #enumerate - přiřadí číslo ke každému prvku.
        for i, poznamka in enumerate(poznamky):
            print(f"{i+1}.{poznamka}")
            
    input("Stiskněte jakoukoliv klávesu pro návrat do menu.")

#funkce vymazat_poznamku() slouzi k odstranění dané poznámky ze seznamu, kterou jsi uživatel vybral
def vymazat_poznamku():
    poznamky = nacist_poznamky()
    zobrazeni_poznamek()
    volba = int(input("Zadejte číslo poznámky, kterou chcete odstranit: "))
        
    if 0 < volba <= len(poznamky):
        #del - ddstraní objekt ze seznamu.
        del poznamky[volba-1]
        ulozit_poznamky(poznamky)
        print("Poznamka byla odstraněna")
    else:
        print("Špatně zvolená poznámka.")
        
    input("Stiskněte jakoukoliv klávesu pro návrat do menu.")

#funkce oznacit_dulezitost() pridává před poznámku do seznamu slovo dulezite, poznamku si uzivatel muze vybrat
def oznacit_dulezitost():
    poznamky = nacist_poznamky()
    volba = int(input("Zadejte číslo poznámky, kterou chcete označit jako důležitou: "))
    
    if 1 <= volba <= len(poznamky):
        if "DŮLEŽITÁ:" not in poznamky[volba-1]:
            poznamky[volba-1] = "DŮLEŽITÁ: " + poznamky[volba-1]
            ulozit_poznamky(poznamky)
            print("Poznámka byla označena jako důležitá.")
        else:
            print("Poznámka již byla označena jako důležitá.")
    else:
        print("Špatně zadaná volba")
        
    input("Stiskněte jakoukoliv klávesu pro návrat do menu.")

#funkce upraveni_poznamky() dovoluje uzivateli vybrat si jiz vytvorenou poznamku, kterou muze upravit
def upraveni_poznamky():
    poznamky = nacist_poznamky()
    volba = int(input("Zadejte číslo poznámky, kterou chcete upravit: "))
    
    if 1 <= volba <= len(poznamky):
        nova_poznamka = input("Zadejte úpravu poznámky: ")
        poznamky[volba-1] = nova_poznamka
        ulozit_poznamky(poznamky)
        print("Poznámka byla upravena.")
    else:
        print("Špatně zadaná volba")
        
    input("Stiskněte jakoukoliv klávesu pro návrat do menu.")