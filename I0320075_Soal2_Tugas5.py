nama = input('masukkan nama: ')
nilai = int(input('masukkan nilai: '))
greeting = 'Halo,'
info = 'Nilai anda setelah dikonversi adalah'
if nilai > 85:
    print(greeting+nama+'!'+' '+info+' '+'A')
elif nilai > 80:
    print(greeting+nama+'!'+' '+info+' '+'A-')
elif nilai > 75:
    print(greeting+nama+'!'+' '+info+' '+'B+')
elif nilai > 70:
    print(greeting+nama+'!'+' '+info+' '+'B-')
elif nilai > 65:
    print(greeting+nama+'!'+' '+info+' '+'C+')
elif nilai > 60:
    print(greeting+nama+'!'+' '+info+' '+'C')
else:
    print(greeting+nama+'!'+' '+info+' '+'E')