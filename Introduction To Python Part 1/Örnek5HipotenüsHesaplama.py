#Dik üçgende dik açının karşısındaki kenara hipotenüs denir. Hipotenüs formülü : a^2 + b^2 = c^2
#hipotenüsü hesaplayan programı yazınız (kenarları kullanıcıdan alınız)

edge1 = int(input("1.kenar : "))
edge2 = int(input("2.kenar : "))
hipotenus = (edge1**2 + edge2**2)**0.5
print("Hipotenüs uzunluğu: "+str(hipotenus))