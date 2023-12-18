nama = 'MUHAMMAD ADHI FAHRIANSYAH AHMAD'
nim  = '231031100'
prodi = 'Sistem informasi D'
meet = 'Praktikum 3'
email = 'adhyfahriansyah123@gmail.com'

sp = 111

print('_'.center(sp, '_'))
print(nama.center(sp))
print(nim.center(sp))
print('\n' * 2)
print(meet.rjust(sp))
print(prodi.rjust(sp))
print(email.rjust(sp))

print('_'.center(sp, '_'))

paragraf = '''\tHalo, selamat datang perkenalkan nama saya {}
dengan NIM {} dari prodi {}. Ini adalah file {}.'''
p = paragraf.format(nama, nim, prodi, nim)

print(p)

x = int(input('Masukkan Nilai ---5+++9---='))
cek1 = x > 5
cek2 = x < 9
status = cek1 and cek2
print('Hasil adalah', status)

x = int(input('Masukkan Nilai +++5---9+++= '))
cek1 = x<5
cek2 = x>9
status = cek1 or cek2
print('Hasilnya adalah',status)

x = int(input('Masukkan Nilai +++5---9+++13---= '))
cek1 = x<5
cek2 = x>9
cek3 = x<13
status = cek1 or cek2 and cek3
print('Hasilnya adalah',status)


#Tugas 1
x = int(input('Masukkan Nilai ----5++++9------13+++++16-----='))
cek1 = x<5
cek2 = x>9
cek3 = x<13
cek4 = x>16
status = cek1 or cek2 and cek3 or cek4
print('Hasilnya adalah',status)

#Tugas 2
x = int(input('Masukkan Nilai ++++5----9++++13----16+++++='))
cek1 = x<5
cek2 = x>9
cek3 = x<13
cek4 = x>16
status = cek1 or cek2 and cek3 or cek4
print('Hasilnya adalah',status)

#Tugas 3
x = int(input('Masukkan Nilai ----5++++9------13++++16-----20+++++24----='))
cek1 = x>5
cek2 = x<9
cek3 = x>13
cek4 = x<16
cek5 = x>20
cek6 = x<24
status = cek1 and cek2 or cek3 and cek4 or cek5 and cek6
print('Hasilnya adalah',status)

#Tugas 4
x = int(input('Masukkan Nilai ++++5----9++++++13-----16+++++20-----24+++++='))
cek1 = x < 5
cek2 = x > 9
cek3 = x < 13
cek4 = x > 16
cek5 = x < 20
cek6 = x > 24
status = cek1 or cek2 and cek3 or cek4 and cek5 or cek6
print('Hasilnya adalah',status)



