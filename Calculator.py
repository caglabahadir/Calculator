print("HESAP MAKİNESİ")
sayi1 = int(input("birinci sayiyi giriniz:"))
sayi2 = int(input("ikinci sayiyi giriniz:"))

islemturu =  input("yapmak istediginiz islemin sembolunu girin:")

if(islemturu == "+"):
  print(sayi1+sayi2)
elif(islemturu == "-"):
  print(sayi1-sayi2)
elif(islemturu == "*"):
  print(sayi1*sayi2)
elif(islemturu == "/"):
  if(sayi2>0):
    print(sayi1/sayi2)
  else:
    print("sifirdan buyuk bir deger yaziniz")
else:
  print("gecerli bir islem sembolu giriniz")