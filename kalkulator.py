print("-----Kalkulator-----")
print("********************")
def add(x, y):
   return x + y

def subtract(x, y):
   return x - y

def multiply(x, y):
   return x * y

def divide(x, y):
   return x / y

print('''Pilihan  Operasi
1. Penjumlahan
2. Pengurangan
3. Perkalian
4. Pembagian''')

pilihan = input("Masukkan pilihan Operasi : ")

a = int(input("Masukkan angka ke (1): "))
b = int(input("Masukkan angka ke (2): "))


if pilihan == '1':
   print ( a, "+",b,"=", add(a,b))

elif pilihan == '2':
   print(a,"-",b,"=", subtract(a,b))

elif pilihan == '3':
   print(a,"*",b,"=", multiply(a,b))

elif pilihan == '4':
   print(a,"/",b,"=", divide(a,b))

else:
    print("  ")