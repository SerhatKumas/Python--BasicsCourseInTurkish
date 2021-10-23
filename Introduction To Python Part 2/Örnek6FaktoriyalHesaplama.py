#Kullanıcının girdiği sayının faktöriyelini hesaplayan kodu yazınız.
#İpucu : recursive kullanılabilir sanki

number = int(input("Faktöriyelini Hesaplamak için sayı giriniz:"))
value = 1
for i in range(number):
    value = value * (i + 1)

print("Faktoriyel : ", value)

