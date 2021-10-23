#********************************  KULLANICIDAN BİLGİ ALMAK   ******************************************************

#Pythondaki hazır bulunan input fonksiyonu : Kullanıcıdan bilgi almak(girdi , input) için kullanılır

#İsmini bahşeder misiniz ?
name = input("İsminizi yazınız : ")
print(name)

#Bir de uğurlu sayınızı alabilirsem ?
luckyNumber = input("Uğurlu sayınızı giriniz : ")
print(luckyNumber)

#Bir toplama işlemi yapabilir misin ?
number1 = input("1.sayıyı giriniz : ")
number2 = input("2.sayıyı giriniz : ")
print(number1+number2)

#Niye sonuç böyle oldu ki bir type fonksiyonu ile kontrol et istersen
print(type(number1))
print(type(number2))
#Haaa , demek ki input fonksiyonunun aldığı değer bize str(string , metinsel veri) olarak aktarılı

