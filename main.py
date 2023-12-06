import random

print("Pasirinkite spėjamo skaičiaus ribas")
nuo = int(input("Nuo: "))
iki = int(input("Iki: "))

sugeneruotas = random.randint(nuo, iki)
print(sugeneruotas)
counter = 0

while True:
    spejamas = int(input("Spėjamas skaičius: "))
    counter += 1
    if spejamas > sugeneruotas:
        print("Mažiau")
    if spejamas < sugeneruotas:
        print("Daugiau")
    if spejamas == sugeneruotas:
        print(f"Atspėjote! Spėjimų skaičius: {counter}")
        break
