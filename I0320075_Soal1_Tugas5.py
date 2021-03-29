print('=======Program menyapa pengunjung=======')
name = input('siapa nama anda: ')
gender = input('apa jenis kelamin anda (L/P): ')
Greeting = 'Selamat datang'
if gender == 'L':
    print(Greeting+','+' '+'Mas'+' '+name+'!')
if gender == 'P':
    print(Greeting+','+' '+'Mbak'+' '+name+'!')
else:
    print()

