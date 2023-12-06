import random

print("Pasirinkite spėjamo skaičiaus ribas")
while True:
    try:
        nuo = int(input("Nuo: "))
        iki = int(input("Iki: "))
        if nuo > iki or nuo == iki:
            print("Skaičius nuo negali būti didesnis už iki. Jie negali būti lygūs")
            continue
        break
    except ValueError:
        print("Įvestas ne skaičius")

sugeneruotas = random.randint(nuo + 1, iki - 1)
print(sugeneruotas)
counter = 0

while True:
    print(f"Skaičiaus ribos: nuo {nuo} iki {iki}")
    while True:
        try:
            spejamas = int(input("Spėjamas skaičius: "))
            break
        except ValueError:
            print("Įvestas ne skaičius")
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
