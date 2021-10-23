#Kullanıcıdan ne kadar tutarda yakıt aldığını isteyiniz . #Tam sayı tl cinsi
#Arabannın km başına kaç kuruş yaktığına isteyiniz ; #ondalık sayı tl cinsi 40 kuruş = 0.4 tl
#Aracın alınan yakıt ile kaç km gideceğini bulan bir program yazınız

fuelPrice = float(input("Ne kadar Yakıt aldınız (Tl cinsi) : "))
pricePerKM = float(input("Aracınız km basşı ne kadar yakmakta (Tl cinsi): "))

result = fuelPrice/pricePerKM

print("Aldığınız yakıt ile gideceğiniz menzil (km ): "+str(result))