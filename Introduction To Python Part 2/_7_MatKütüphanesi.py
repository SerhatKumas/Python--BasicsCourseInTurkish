#************************************** MAth Kütüphanesi **************************************************************

#Python'da dahili birçok matematik fonksiyonu bulunur. Bunun dışında math modülü de birçok matematiksel işlemi gerçekleştirmenize olanak tanır.

#min() ve max() Fonksiyonları : Bir sayı dizisindeki en küçük ve en yüksek değeri yazdırır.
number = min(5, 10, 25)
number1 = max(5, 10, 25)

print(number)
print(number1)

#abs() Fonksiyonu : abs() fonksiyonu python'da mutlak değer elde edilmesini sağlar
number2 =abs(-7.25)

print(number2)

#pow(x, y) şeklinde kullanılan fonksiyon x üssü y'nin (x^y) değerini yazdırır.
number3 = pow(4, 3)

print(number3)

#Python ayrıca yukarıdaki temel fonksiyonlar dışında math modülü yoluyla çağırılan daha kapsamlı matematik fonksiyonlarına da sahiptir.
#Bunun için gelin ilk önce math kütüphanesini import edelim

import math

number4 = math.sqrt(64)

print(number4)

#math.ceil(), parantez içinde belirtilen ondalıklı sayıyı bir üst tam sayıya tamamlar. Yani 1.2 ise sonuç 2 olarak çıkar.
number5 = math.ceil(1.4)
print(number5)

#math.floor(1.4)h.floor(), parantez içinde belirtilen ondalıklı sayıyı ona en yakın küçük tam sayıya tamamlar. Yani 1.7 ise sonuç 1 olur.
number6 = math.floor(1.4)
print(number6)

#math.pi() Fonksiyonu : Pi sayısını yazdırır.
number7 = math.pi

print(number7)