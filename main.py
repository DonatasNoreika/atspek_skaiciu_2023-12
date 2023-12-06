import random

sugeneruotas = random.randint(1, 100)
print(sugeneruotas)

while True:
    spejamas = int(input("Spėjamas skaičius: "))
    if spejamas > sugeneruotas:
        print("Mažiau")
    if spejamas < sugeneruotas:
        print("Daugiau")
