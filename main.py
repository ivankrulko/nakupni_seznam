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

def zobrazit_seznam(seznam):
    if seznam:
        print("Aktualní eznam:")
        for polozka in seznam:
            print(f"- {polozka}")
        else:
            print("Seznam je prázdný.")

def zobrazit_pocet_polozek(seznam):
    print(f"Aktuálně je v seznamu {len(seznam)} položek.")