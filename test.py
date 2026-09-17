import os
with open(os.sep.join(["slozka", "testhod2.txt"]), encoding="utf-8") as soubor:
    obsah = soubor.read()
    print(obsah)
print("Data byla úspěšně načtena")