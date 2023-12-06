import random

sugeneruotas = random.randint(1, 100)
# print(sugeneruotas)
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
