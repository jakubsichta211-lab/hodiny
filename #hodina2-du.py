#hodina2-du.py
heslo=input("Zadaj heslo:")
cisla=0
velke_pismena=0
spec_znaky=0
for i in heslo:
    if i.isdigit():
        cisla+=1
    if i.isupper():
        velke_pismena+=1
    if i.isascii() and not(i.isdigit) and not(i.isalpha) and ord(i)>32:
        spec_znaky+=1
if len(heslo)>=8 and cisla>=1 and velke_pismena>=1 and spec_znaky>=1:
    print("dobre heslo")


    