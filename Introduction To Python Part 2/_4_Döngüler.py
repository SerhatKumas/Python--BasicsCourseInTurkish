# Python, iki temel döngü yapısına sahiptir while ve for döngüleri

#Döngüler bir işi TEKRAR TEKRAR yapmak istediğimiz zaman kullanılırlar
#Mesela 100 kere döngü yazdırmak


#WHİLE DÖNGÜSÜ
#Bir koşul gerçekleşene kadar while kod bloğundaki kodlar tekrar tekrar çalıştırır
i = 0
while i < 100 :
  print("Döngü")
  i += 1

#FOR DÖNGÜSÜ
#Belli sayıda tekrarlı bir döngü oluşturacaksak range(sayı) kodu kullanılabilir
for i in range(6) :
  print(i)
#Bir sayıdan başlamasını istersek range(başla, git) kullanılabilir
for i in range(6,20) :
  print(i)

#Ve ayrıca üçüncü parametrede artış miktarını belirtebiliriz
for i in range(6,21,2) :
  print(i)

#Python'da for döngüsü önceden bir değişken tanımlamayı veya dize sırası (index) belirtmeyi gerektirmez
names = ["A" , "B" ,"C"]
for i in names :
  print(i)

#Keza bu in komutu ile yazdığımız for döngüsünü stringler için kullanabiliriz
for i in "Döngü" :
  print(i)
#Döngü içinde döngü kullanabiliriz. Böyle ifadelerde içteki döngü, dıştaki döngü kadar tekrarlanır
clases = [1 , 2 , 3]
classNames = ["A" , "B" ,"C"]

for i in clases :
  for j in clases :
    print(i , j)

#for döngüsünden sonra mutlaka kod yazılmalıdır. Eğer bu döngü çalıştırıldıktan sonra hiçbir kod çalıştırılmaması gerekiyorsa pass yazılarak döngü geçilebilir.
for x in [0, 1, 2]:
  pass

#Break :  Break döngüyü sonlandırmak için kullandığımız ifadedir
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1


fruits = ["elma", "portakal", "mandalina"]
for x in fruits:
  print(x)
  if x == "portakal":
    break

#Continue : Bu ifadeyi kullandığımız an döngü başa dönecek ve bu koddan sonraki satırlar çalışmayacaktır
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

fruits = ["elma", "portakal", "mandalina"]
for x in fruits:
  if x == "portakal":
    continue
  print(x)


#Not : Döngülerde i , j , k ,x gibi ifadeler zorunlu değildir . Siz nasıl isterseniz adlandırabilirsiniz .
#Biz genelde i kullanırız çünkü i = index in baş harfidir .
