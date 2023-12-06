import random

print("Pasirinkite spėjamo skaičiaus ribas")
nuo = int(input("Nuo: "))
iki = int(input("Iki: "))

sugeneruotas = random.randint(nuo + 1, iki - 1)
print(sugeneruotas)
counter = 0

while True:
    print(f"Skaičiaus ribos: nuo {nuo} iki {iki}")
    spejamas = int(input("Spėjamas skaičius: "))
    if spejamas <= nuo or spejamas >= iki:
        print("Spėjimas iš ribų")
        continue
    counter += 1
    if spejamas > sugeneruotas:
        print("Mažiau")
        iki = spejamas
    if spejamas < sugeneruotas:
        print("Daugiau")
        nuo = spejamas
    if spejamas == sugeneruotas:
        print(f"Atspėjote! Spėjimų skaičius: {counter}")
        break
