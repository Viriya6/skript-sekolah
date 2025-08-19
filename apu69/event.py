import random
import time
import os

image = ["7️⃣", "🍎", "🐵", "🎉", "🎱"]
lose_streak = 0
win_streak = 0

def petraspin(n: int):
    hasil = n
    a = random.randint(20, 30)
    for i in range(0, a):
        sone = random.choice(image)
        stwo = random.choice(image)
        sthree = random.choice(image)
        print(f"{sone} {stwo} {sthree}")
        time.sleep(0.1)
        os.system('clear||cls')
    
    sone = random.choice(image)
    stwo = random.choice(image)
    sthree = random.choice(image)
    print(f"{sone} {stwo} {sthree}")
    
    if(sone == stwo and stwo == sthree):
        hasil *= 2
        print(f"Anda Menang Rp {hasil}")
        return hasil
    elif(sone == stwo and stwo != sthree):
        hasil *= 0.5
        hasil = round(hasil)
        print(f"Anda Menang Rp {hasil}")
        return hasil
    elif(stwo == sthree and sone != stwo):
        hasil *= 0.5
        hasil = round(hasil)
        print(f"Anda Menang Rp {hasil}")
        return hasil
    elif(sone == sthree and sone != stwo):
        hasil *= 0.5
        hasil = round(hasil)
        print(f"Anda Menang Rp {hasil}")
        return hasil
    else:
        print(f"Anda kalah Rp {hasil}")
        hasil *= -1
        return hasil