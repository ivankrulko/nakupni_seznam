def pridat_polozku(seznam):
    polozka = input("Zadej název položky k přidání:")
    seznam.append(polozka)
    print(f"Položka {polozka} byla přidána.")

def odebrat_polozku(seznam):
    polozka=input("Zadej nazev položky, kterou chceš vymazat:")
    if polozka in seznam:
        seznam.remove(polozka)
        print(f"Položka {polozka} byla smazána.")
    else:
        print(f"Položku {polozka} jsme v nenašli.")

def seradit_seznam(seznam):
    seznam.sort()
    print("Seznam je seřazen podle abecedy.")
    zobrazit_seznam(seznam)

def zobrazit_seznam(seznam):
    print("Aktualní seznam:")
    if len(seznam) > 0:
        for polozka in seznam:
            print(f"- {polozka}")
    else:
        print("Seznam je prázdný.")

def zobrazit_pocet_polozek(seznam):
    print(f"Aktuálně je v seznamu {len(seznam)} položek.")


def main():
    seznam = []
    while True:
        print("\n1. Přidat položku")
        print("2. Odebrat položku")
        print("3. Zobrazit seznam")
        print("4. Seřadit seznam")
        print("5. Zobrazit počet položek")
        print("6. Ukončit program")
        
        volba = input("Vyberte možnost: ")

        if volba == '1':
            pridat_polozku(seznam)
        elif volba == '2':
            odebrat_polozku(seznam)
        elif volba == '3':
            zobrazit_seznam(seznam)
        elif volba == '4':
            seradit_seznam(seznam)
        elif volba == '5':
            zobrazit_pocet_polozek(seznam)
        elif volba == '6':
            print("Ukončuji program.")
            break
        else:
            print("Nejde, zadej znova.")


if __name__ == "__main__":
    main()