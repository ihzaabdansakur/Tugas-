print('seleksi BUMN')
nama= str(input('masukan nama:'))
umur= int(input('masukan umur:'))
pendidikanterakhir= str(input('pendidikanterakhir(minimal sma):'))
nilai= int(input('nilai(minimal 75): '))
kesehatan= str(input('kesehatan(sehat atau tidak): '))
pendidikan=['sma','smk','diploma','sarjana']
if umur >= 18 and pendidikanterakhir in pendidikan and nilai >= 75 and kesehatan=='sehat':
    print('anda dinyatakan lulus')
else:
    print('maaf anda tidak lulus')