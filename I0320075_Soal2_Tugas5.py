nama = input('masukkan nama: ')
nilai = int(input('masukkan nilai: '))
greeting = 'Halo,'+nama+'!'
info = 'Nilai anda adalah'
if nilai >= 85:
    print(greeting+' '+info+' '+'A (congrats)')
elif nilai >= 80:
    print(greeting+' '+info+' '+'A- (good job)')
elif nilai >= 75:
    print(greeting+' '+info+' '+'B+ (tingkatkan)')
elif nilai >= 70:
    print(greeting+' '+info+' '+'B- (tingkatkan)')
elif nilai >= 65:
    print(greeting+' '+info+' '+'C+ (belajar lagi)')
elif nilai >= 60:
    print(greeting+' '+info+' '+'C (belajar lagi)')
else:
    print(greeting+' '+info+' '+'E (semangat ngulang)')