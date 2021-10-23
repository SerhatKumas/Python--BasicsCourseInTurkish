#*************************************** Koşul İfadeleri  *************************************************************

#if, koşul belirtme ifadesidir .
# Bu yüzden if in içerisinde True , false veya bunları veren karşılaştırma denklemleri kurulur
if 300 > 200 :
    print("İf bloğu true döndü")

#Eğer if koşulu gerçekleşmezse else girer
userName = "Serhat"
if userName == "Sabri":
    print("İf bloğu çalıştı")
else:
    print("Else bloğu çalıştı")

#2 den fazla durum varsa eğer bu durumda elif kullanarız
if userName == "Anıl":
    print("İf bloğu çalıştı")
elif userName == "Serhat" :
    print("Elif bloğu çalıştı")
else:
    print("Else bloğu çalıştı")

#İç İçe if Kullanımı genellikle birden fazla koşul kontrolünde kullanılır
number = 30
if number > 10 :
    print("Sayı 10'dan büyüktür")
    if number < 20 :
        print("Sayı 20 ile 20 arasındadır")
    else:
        print("Sayı 20'den büyüktür")

#Pass Deyimi : if kullanıldığı zaman boş bırakılamaz ve mutlaka kod yazılması istenir fakat biz bir durum gerçekleştiğinde bir şey yapılmasınız istemiyorsak pass komutunu kullanırız
if "ser" in "serhat" :
    pass
else :
    print("Giriş Hatası")