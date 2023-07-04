# report 1
print(
'''Pilih type rumah yang akan dibeli:
A. T45/84 harga 550.000.000
B. T55/112 harga 850.000.000
C. T60/120 harga 950.000.000''')
rumah = str(input('Pilih type rumah yang akan dibeli: '))

if rumah =='A':
    harga = 550000000
if rumah =='B':
    harga == 850000000
elif rumah =='C':
    harga = 950000000

uang_muka = int(harga * 0.1)
sisa = harga - uang_muka
tahun = 1
while tahun <= 30:
    cicilan = int(sisa/((12*tahun)-1))
    cicilanbg = int(cicilan*0.005)
    tdp = int(uang_muka +cicilanbg)
    print(
        f'''{tahun} tahun:
        DP\t\t\t\t= Rp{uang_muka}
        Besarnya hutang = Rp{sisa}
        Cicilan pokok bulanan\t\t= Rp{cicilanbg}
        Total cicilan setiap bulan\t= Rp{int(cicilan+cicilanbg)}
        TDP\t\t\t\t= Rp{int(uang_muka+(int(cicilan+cicilanbg)))}''')
    tahun += 1
    print()

# report 2
uangmuka = int(input("masukkan uang muka: "))
cicilan_bulan_pertama = int(input(cicilanbg))
biaya_notaris = 2000000

