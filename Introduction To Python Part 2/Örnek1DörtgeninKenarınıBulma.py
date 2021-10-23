#Kullanıcıdan alınan dört kenarın bilgisine göre şeklin kare, dikdörtgen veya diğer dörtgenlerden olduğunu belirten kodu yazınız.
#Diğer dörgen özelliğini else ile kontrol edebilirsiniz

edge1 = int(input("1. Kenarı Giriniz:"))
edge2 = int(input("2. Kenarı Giriniz:"))
edge3 = int(input("3. Kenarı Giriniz:"))
edge4 = int(input("4. Kenarı Giriniz:"))

if (edge1 == edge2 == edge3 == edge4):
    print("Kare!!")
elif (edge1 == edge3 and edge2 == edge4 or edge1 == edge2 and edge3 == edge4):
    print("Dikdörtgen!!")