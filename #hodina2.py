#hodina2.py
heslo=input("Zadaj heslo:")
pocet=0
cisla=0
velke_znaky=0
specialne_znaky=0
if len(heslo)<8:
    print("musi mat aspon 8 znakov")
else:
    for znak in heslo:
        if znak.isdigit():
            cisla+=1
    if cisla<1:
        print("nieje tam cislo")
    else:
        for znak in heslo:
            if znak.isupper():
                    velke_znaky+=1
            else:
                 print("nema velke pismeno")
        for znak in heslo:
            if znak.isascii() and not(znak.isdigit) and not(znak.isalpha) and ord(znak)>32:
                specialne_znaky+=1
            else:
                print("nemas specialny znak")