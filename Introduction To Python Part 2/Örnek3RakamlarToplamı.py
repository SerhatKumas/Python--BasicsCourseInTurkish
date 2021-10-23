#Kullanıcının girdiği sayının rakamlarını toplayan python örneği
number = input("Bir sayı girin: ")  # str formatında giriş yapar
sum = 0
for digit in number:
    sum += int(digit)

print("sayının rakamları toplamı:", sum)