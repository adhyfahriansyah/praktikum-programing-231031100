
print('\n')
biodata = { 'nama'  : 'Muhammad Adhi Fahriansyah Ahmad',
'nim'   : '231031100',
'kelas' : 'S123D',
'tempat,tanggal lahir' : 'parepare,07 maret 2004',
'jenis kelamin' : 'laki-laki',
'agama' : 'islam',
'alamat': 'jalan agussalim no.40',
'email' : 'adhyfahriansyah123@gmail.com'
}

print(biodata.keys())
print(biodata.values())

print()
selected_biodata = dict(list(biodata.items())[:3])
print(selected_biodata)





