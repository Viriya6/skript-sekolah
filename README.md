# skript-sekolah
kumpulan script-script yang dibuat untuk kepentingan sekolah 🧑🏻‍💻🏫 

## katale 🔡
Katale adalah game yang terbuat dari bahasa pemrograman python yang dibuat seperti [Wordle](https://en.m.wikipedia.org/wiki/Wordle) yang dimana seseorang harus menebak sebuah kata yang terdiri dari 5 huruf

- Cara Kerja
1. emoji blok ⬛`#000000` menunjukan bahwa tidak ada huruf didalam kata tersebut
2. emoji blok 🟨`#ffff00` menunjukan bahwa terdapat huruf didalam kata tersebut tetapi hanya salah penempatan
3. emoji blok 🟩`#008000` menunjukan bahwa terdapat huruf didalam kata tersebut dan penempatannya benar atau tepat

semisal kata rahasia adalah `rumah`

apabila anda berhasil menebak maka akan keluar
```🎉 Selamat! kamu menebak kata rumah dengan benar!```

```
Tebakan ke-1: sebar
Hasil: ⬛⬛⬛🟩🟨
Tebakan ke-2: kamar
Hasil: ⬛⬛🟩🟩🟨
Tebakan ke-3: gubuh
Hasil: ⬛🟩⬛⬛🟩
Tebakan ke-4: rumah
Hasil: 🟩🟩🟩🟩🟩
🎉 Selamat! kamu menebak kata rumah dengan benar!
```

apabila tebakan anda salah sebanyak 10 kali maka akan keluar
```😢 Kamu gagal menebak. Kata yang benar adalah: rumah```

```
Tebakan ke-1: sopir
Hasil: ⬛⬛⬛⬛🟨
Tebakan ke-2: sumur
Hasil: ⬛⬛🟩⬛🟨
...
Tebakan ke-10: remah
Hasil: 🟩⬛🟩🟩🟩
😢 Kamu gagal menebak. Kata yang benar adalah: rumah
```

## apu69
Apu69 adalah sebuah game yang mempertaruhkan sebuah mata uang Rp alias Rapih bukan rupiah ya, kalo rupiah mah D**. Pada game ini terdapat banyak sekali permainan.

• Petraspin
Petraspin adalah game yang dimana kita mempertaruhkan mata uang untuk mencocokan  3 gambar/emoji (7️⃣🍎🐵🎉🎱)

Awalnya kita akan input uang yang ingin kita taruh(taruhan), dan anda dikasih Uang awal sebesar satu juta Rapih (Rp 1.000.000)
```
Uangmu: Rp 1000000
Rp ...
```

Selanjutnya mesin Petraspin/Slut akan berputar dengan cara ```random.choice()```
```
7️⃣🍎🐵
```
sebanyak 20-30 kali, lalu jika:
1. 3 emoji yang dikeluarkan sama maka uang yang kita taruhkan akan dikali sebesar 2x. ```🎱🎱🎱```
2. 2 emoji yang dikeluarkan sama maka uang yang kita taruhkan akan dikali sebesar 0.5x. ```7️⃣🍎🍎```