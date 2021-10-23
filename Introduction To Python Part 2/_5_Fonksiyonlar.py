#********************************************   Fonksiyonlar   *********************************************************

#Fonksiyon yaratırken def komutunu kullanılır
def func():
    print("Hello Microsoft")

#İyi güzel fonksiyonu tanımladık ama nasıl çalıştırıyoruz  : Fonksiyonu çalıştırmak için fonksiyonun adını yazın, ardından parantez açıp kapatın
func()

#Fonksiyonlara bilgi parametreler vasıtasıyla iletilir
#Parametre, fonksiyon adından sonra parantez içinde belirtilir. Birden fazla parametre kullanılabilir. Bunlar virgül (,) ile ayrılır
def websiteWelcome(websiteName) :
    print(websiteName , "sitemize hoş geldin .")

websiteWelcome("Microsoft")

#Ya fonksiyon çağrılırken parametre girilmezse : o zaman varsayılan değer tanımlarız
def fromWhere(country = "Türkiye"):
    print("Nereden :",country )

fromWhere("Abd")
fromWhere("İngiltere")
fromWhere()

#Fonksiyonların çalıştıktan sonra bir değer döndürmesini return <deger> ifadesini kullanarak sağlayabiliriz
def transformHeight(x) :
    return (x/100)

print('Boyunuz :',transformHeight(178),"m")

#Fonksiyonlar boş bırakılmaz ama bir işlem yapmak istemezsek ki niye o zaman fonksiyon yazdık ama neyse. Bu durumda pass kelimesini kullanabilirsin ;
def nothing() :
    pass

#Fonksiyonlar kendisini çalıştırabilmesine recursion denir . Kendi kendini çağırır , çalıştırır Hadi bir örnek verelim ;
def factorial(n):
    if n==1 :
        return n
    else:
        return n*factorial(n-1)

print(factorial(5))
