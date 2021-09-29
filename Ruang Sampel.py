import math
import fractions


ruangsampel = int(input('Masukkan Ruang Sampel : '))
semesta = int(input('Masukan Jumlah Semesta : '))


h = ruangsampel / semesta 
f = fractions.Fraction(h)
print('Peluangnya adalah : ', h)
print('Jawaban dalam bentuk pecahan', f)