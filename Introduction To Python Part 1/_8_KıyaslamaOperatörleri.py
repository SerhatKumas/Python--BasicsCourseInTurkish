#************************************  KIYASLAMA OPERATÖRLERİ  *******************************************************

#Kıyaslama Operatörleri : İki değer arasında kıyaslama yapmak için kullanılır

# == Eşittir operatörünün iki tarafındaki veri aynı ise True herhangi biri farklı ise False döner .
print("veri" == "veri") #T
print("veri" == "Veri") #F

# != Eşit değildir operatörü iki tarafındaki veri aynı ise False herhangi biri farklı ise True döner
print("veri" != "veri") #F
print("veri" != "Veri") #T

# >	Büyüktür operatörü
print(5 > 6) #F
print(12 > 10) #T

# <	Küçüktür operatörü
print(5 < 6) #T
print(12 < 10) #F

# >= Büyük ya da eşittir operatörü
print(6 >= 6) #T
print(9 >= 6) #T

# <= Küçük ya da eşittir operatörü
print(6 <= 6) #T
print(10 <= 12) #T

#***************************************  MANTIKSAL OPERATÖRLER   **********************************************

#Ve (and), veya (or), değilse (not) gibi ifadelerle koşulların gerçekleşme durumlarını kontrol eder.

# and Operatörü
print(True and True)    #T and T = T
print(True and False)   #T and T = T
print(False and True)   #T and T = T
print(False and False)  #T and T = T

# or Operatörü
print(True or True)     #T or T = T
print(True or False)    #T or F = T
print(False or True)    #F or T = T
print(False or False)   #F or F = F

# not Operatörü
print(not True)     #not T = F
print(not False)    #not F = T


#**********************************  Ait Olma Operatörleri   ********************************************************

#in opertörü : Seri belirtilen değeri içeriyorsa doğrudur
print("ser" in "serhat") #T
print("can" in "serhat") #F

#not in	operatörü : Seri belirtilen değeri içermiyorsa doğrudur
print("ser" not in "serhat") #F
print("can" not in "serhat") #T