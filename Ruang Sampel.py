#Author : PRINAFSIKA (21081010278)

import fractions
import pyfiglet
import os

intro = pyfiglet.figlet_format("Probabilitas", font = "standard")
intronama = pyfiglet.figlet_format("By : Kelompok 5", font = "standard")

print(intro)
print(intronama)
print('|----------------------------------------------------|')
print('| Rumus Peluang Kejadian adalah : P(K) = n(K) / n(S) |')
print('|----------------------------------------------------|')
print('        ---Menu---       ')
print('1. Menghitung Kartu Hitam')
print('2. Menghitung Kartu Merah')
print('3. Menghitung Kartu Jack, Queen, King')
print('4. Menghitung Custom')

pilihan = int(input('Masukkan Pilihan : '))

if pilihan == 1:
    k = 26
    s = 52
    kitem = (k/s)
    f = fractions.Fraction(kitem)

    print(k, ' = Terdiri dari 13 kartu Kriting dan 13 kartu Sekop')
    print(s, ' = Total Kartu')
    print(k, 'Dibagi', s)
    print('Peluang terambilnya kartu hitam adalah : ', kitem, '| ', f)

elif pilihan == 2:
    k = 26
    s = 52
    kmerah = (k/s)
    f = fractions.Fraction(kmerah)

    print(k, ' = Terdiri dari 13 kartu Hati dan 13 kartu Wajik')
    print(s, ' = Total Kartu')
    print(k, 'Dibagi', s)
    print('Peluang terambilnya kartu merah adalah : ', kmerah, '| ', f)

elif pilihan == 3:
    k = 12
    s = 52
    kjqk = (k/s)
    f = fractions.Fraction(kjqk)

    print(k, ' = Terdiri dari 6 kartu Merah dan 6 kartu Hitam')
    print(s, ' = Total Kartu')
    print(k, 'Dibagi', s)
    print('Peluang terambilnya kartu Jack, Queen, King adalah : ', kjqk, '| ', f)

elif pilihan == 4:
    os.system('cls')
    print('')
    print('----MENU----')
    print('1. Menghitung Kartu AS')
    print('2. Menghitung Kartu Wajik')
    print('3. Menghitung Kartu Hati')
    print('4. Menghitung Kartu Sekop')
    print('5. Menghitung Kartu Keriting')
    print('6. Menghitung Seluruh Kartu Dengan JOKER')
    print('7. Custom')
    print('0. Exit')
    print('')
    custom = int(input('Masukkan Pilihan : '))

    if custom == 1:
        k = 4
        s = 52
        kAs = (k/s)
        f = fractions.Fraction(kAs)

        print(k, ' = Terdiri dari', k, 'Kartu AS')
        print(s, ' = Total Kartu')
        print(k, 'Dibagi', s)
        print('Peluang terambilnya kartu AS adalah : ', kAs, '| ', f)

    elif custom == 2:
        k = 13
        s = 52
        kwajik = (k/s)
        f = fractions.Fraction(kwajik)

        print(k, ' = Terdiri dari', k, 'Kartu WAJIK')
        print(s, ' = Total Kartu')
        print(k, 'Dibagi', s)
        print('Peluang terambilnya kartu WAJIK adalah : ', kwajik, '| ', f) 

    elif custom == 3:
        k = 13
        s = 52
        khati = (k/s)
        f = fractions.Fraction(khati)

        print(k, ' = Terdiri dari', k, 'Kartu HATI')
        print(s, ' = Total Kartu')
        print(k, 'Dibagi', s)
        print('Peluang terambilnya kartu HATI adalah : ', khati, '| ', f)

    elif custom == 4:
        k = 13
        s = 52
        ksekop = (k/s)
        f = fractions.Fraction(ksekop)

        print(k, ' = Terdiri dari', k, 'Kartu SEKOP')
        print(s, ' = Total Kartu')
        print(k, 'Dibagi', s)
        print('Peluang terambilnya kartu SEKOP adalah : ', ksekop, '| ', f)    

    elif custom == 5:
        k = 13
        s = 52
        kkeriting = (k/s)
        f = fractions.Fraction(kkeriting)

        print(k, ' = Terdiri dari', k, 'Kartu KERITING')
        print(s, ' = Total Kartu')
        print(k, 'Dibagi', s)
        print('Peluang terambilnya kartu KERITING adalah : ', kkeriting, '| ', f)   

    elif custom == 6:
        user = int(input('Masukkan Ruang Sampel / Jumlah Kartu : '))
        s = 54
        kjoker = (user/s)
        f = fractions.Fraction(kjoker)

        print(user, ' = Kartu yang ingin dicari')
        print(s, ' = Total Kartu + JOKER')
        print(user, 'Dibagi', s)
        print('Peluang terambilnya kartu  adalah : ', kjoker, '| ', f)

    elif custom == 7:
        ruangsampel = int(input('Masukkan Ruang Sampel / Jumlah Kartu : '))
        semesta = int(input('Masukan Jumlah Semesta / Jumlah Seluruh Kartu : '))
        h = ruangsampel / semesta 
        f = fractions.Fraction(h)

        print('Peluangnya adalah : ', h)
        print('Jawaban dalam bentuk pecahan', f)
    else:
        exit()
else:
  print('Silahkan masukan ulang')
