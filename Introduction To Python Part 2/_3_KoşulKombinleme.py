#Kıyaslama operatörlerinin kullanımı
#Kullanıcı site giriş veri kontorlü

#Databasedeki bilgilerimiz
nameDb="Name"
phoneDb=123456
passwordDb ="password"

userInfo=input("Telefon numarız veya kullancı isminizi yazınız : ")
userPassword = input("Şifrenizi giriniz : ")
if(userInfo == nameDb or userInfo == str(phoneDb)) and userPassword == passwordDb :
    print("Siteye hoş geldin",nameDb)
else :
    print("Girdiğiniz veriler yanlıştır lütfen tekrar kontorl edip deneyiniz")
