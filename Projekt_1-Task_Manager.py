# Projekt: Task Manager

# Seznam úkolů (globální proměnná)
ukoly = []

def pridat_ukol():
    """Funkce pro přidání nového úkolu do seznamu."""
    while True:
        nazev = input("Zadejte název úkolu: ").strip()
        if not nazev:
            print(" Chyba: Název úkolu nesmí být prázdný. Zkuste to znovu.\n")
            continue
        popis = input("Zadejte popis úkolu: ").strip()
        if not popis:
            print(" Chyba: Popis úkolu nesmí být prázdný. Zkuste to znovu.\n")
            continue
        ukoly.append({"název": nazev, "popis": popis})
        print(f" Úkol '{nazev}' byl úspěšně přidán.\n")
        break


def zobrazit_ukoly():
    """Funkce pro zobrazení všech uložených úkolů."""
    if not ukoly:
        print(" Seznam úkolů je prázdný.\n")
    else:
        print(" Seznam úkolů:")
        for i, ukol in enumerate(ukoly, start=1):
            print(f"{i}. {ukol['název']} – {ukol['popis']}")
        print()


def odstranit_ukol():
    """Funkce pro odstranění vybraného úkolu."""
    if not ukoly:
        print(" Není co odstraňovat – seznam úkolů je prázdný.\n")
        return

    zobrazit_ukoly()
    while True:
        try:
            cislo = int(input("Zadejte číslo úkolu, který chcete odstranit: "))
            if 1 <= cislo <= len(ukoly):
                odstraneny = ukoly.pop(cislo - 1)
                print(f" Úkol '{odstraneny['název']}' byl odstraněn.\n")
                break
            else:
                print(" Neplatné číslo úkolu. Zadejte číslo znovu.\n")
        except ValueError:
            print(" Chyba: Zadejte platné číslo.\n")


def hlavni_menu():
    """Hlavní menu programu Task Manager."""
    while True:
        print("Správce úkolů - Hlavní menu")
        print("1 – Přidat nový úkol")
        print("2 – Zobrazit všechny úkoly")
        print("3 – Odstranit úkol")
        print("4 – Konec programu")
       

        volba = input("Vyberte možnost (1–4): ").strip()

        if volba == "1":
            pridat_ukol()
        elif volba == "2":
            zobrazit_ukoly()
        elif volba == "3":
            odstranit_ukol()
        elif volba == "4":
            print(" Konec programu.")
            break
        else:
            print(" Neplatná volba. Zadejte prosím číslo 1–4.\n")


# Spuštění programu
if __name__ == "__main__":
    hlavni_menu()





