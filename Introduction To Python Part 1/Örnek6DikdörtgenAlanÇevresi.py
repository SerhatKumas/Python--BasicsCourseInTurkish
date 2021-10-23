#Kullanıcıdan kısa ve uzun kenar bilgisini aldığı dikdörtgenin alan ve çevre hesaplamasını yapan kodu yazınız.

shortEdge = int(input("Kısa kenarı giriniz : "))
longEdge = int(input("Uzun kenarı giriniz : "))

perimeter = (shortEdge + longEdge) * 2
field = shortEdge * longEdge
print("Alan : "+str(field)  +" Çevre :"+str(perimeter))