import random
import os
from event import*
os.system('clear||cls')
money = 1000000

while True:
    print(f"Uangmu: Rp {money}")
    n = int(input("Rp "))
    if(money < n):
        print("Uang mu Tidak Cukup!")
    else:
        money -= n
        hasil = petraspin(n)
        money += hasil

    if(money <= 0):
        print("Yahahaha Anda Rungkad 🫵🤪")
        break