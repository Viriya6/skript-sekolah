import random
from collections import Counter
from list_kata import pilihkata

kata_rahasia = pilihkata()

MAX_TEBakan = 6

def beri_umpan_balik(tebakan, target):
    hasil = ['⬛'] * 5
    target_counter = Counter(target)

    for i in range(5):
        if tebakan[i] == target[i]:
            hasil[i] = '🟩'
            target_counter[tebakan[i]] -= 1  # Kurangi jumlah huruf yang tersedia

    for i in range(5):
        if hasil[i] == '⬛' and tebakan[i] in target_counter and target_counter[tebakan[i]] > 0:
            hasil[i] = '🟨'
            target_counter[tebakan[i]] -= 1

    return ''.join(hasil)

print("======================KATALE======================")

for percobaan in range(MAX_TEBakan):
    tebakan = input(f"Tebakan ke-{percobaan + 1}: ").lower()

    if len(tebakan) != 5:
        print("❗ Kata harus terdiri dari 5 huruf.")
        continue

    umpan_balik = beri_umpan_balik(tebakan, kata_rahasia)
    print("Hasil:", umpan_balik)

    if tebakan == kata_rahasia:
        print(f"🎉 Selamat! Kamu menebak kata '{kata_rahasia}' dengan benar!")
        break
else:
    print(f"😢 Kamu gagal menebak. Kata yang benar adalah: {kata_rahasia}")
