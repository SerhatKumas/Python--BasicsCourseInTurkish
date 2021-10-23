#****************************************   DEĞİŞKENLER   ************************************************************

#Değişkenler, herhangi bir bilgi(veri) içeren ifadelerdir (Yapısı Değişken_İsmi = Değişken_Değeri)
variable = "Değiken değeri"
variable = 5

# Ayrıca pythonda değişkenler için bir tür belirtme zorunluluğu da yoktur. Değişkenin türü yeni atamalarla kolaylıkla değiştirilebilir
#java => int variableName = 5;
#javascript => var variableName= "Serhat" ;
variable2 = "Anıl"
variable2 = 16203435

#Metinsel değişkenler 3 tane çift tırnak ("), çift tırnak (") ve tek tırnak (') kullanılarak tanımlanabilirler
variable4 ="""Metinsel değişkenler"""
variable5 ="Metinsel değişkenler"
variable6 ='Metinsel değişkenler'
print(variable4) #variable4 , variable5 ve variable6 dene ve farkı olmadığını gör

#Pythonda birden fazla değişkene aynı anda değer atamak da mümkün ;
variable7 , variable8 = "Gökay", "Selin"
print(variable7)
print(variable8)

#Ayrıca değişkenlere aynı değer atamak da mümkün ;
variable9 = variable10 = "Serhat"
print(variable9)
print(variable10)

#********************************   DEĞİŞKEN İSİMLENDİRME KURALLARI  **************************************************

#Değişken ismi içinde :'”,<>/?|\()!@#$%^&*~-+ karakterleri kullanılamaz. (Sadece “_ “sembolü kullanılabilir)
?variable = "Jale"
!variable = "Melek"

#Değişken isimleri bir sayı veya aritmetik operatör ile başlayamaz
/variable = "Bilge"
1variable = "Bilgehan"

#Değişken ismi kelimelerden oluşuyorsa aralarında boşluk olamaz
user Name = "Su"

#Python da tanımlı anahtar kelimeler değişken ismi olarak kullanılamaz if else while for
if = "Ezra"

#***********************************  Değişken YAZIM ŞEKİLLERİ   *******************************************************

# camelCase => İlk kelimenin baş harfi küçük , geri kalan kelimelerin baş harfi büyük olarak yazdığımız yazım türüdür .
userName = ""
# PascalCase => Tüm kelimelerin baş harfi büyük olarak yazdığımız yazım türüdür .
UserName = ""

# snake_case => Her kelime arasına _ (Alttan tire )koyduğumuz yazım türüdür .
user_name = ""

# Not : Bunlar arasında en doğrusu diye bir şey yoktur . Kullanım alanlarına , çalıştığınız kurumun kurallarına göre değişiklik gösterir .