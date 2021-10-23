#**********************************  String İle Çalışmak *************************************************************
#Daha önce de konuştuğumuz gibi stringler """ """ / " " / ' '  işaretleri arasına tanımlanabilir.
userName = 'serhatkumass'
userName1 = "serhatkumass"
userName2 = """serhatkumass"""

#String aslında harflerden oluşan bir topluluktur => ilk değerlerin index'i 0 dan başlar
microsoft = "Microsoft Learn Student Ambassador "
print(microsoft[10])

#Eğer belirli bir alanı istiyorsak [0:8] yaparız .
print(microsoft[0:9]) #İlk değer başlangıç , ikinci değer ise son index değeridir. Fakat son index değeri dahil değildir .

#len() fonksiyonu ile bir string değerinin kaç karakterden oluştuğunu elde edebiliriz => len(x)
print(len(microsoft))

# Metin içeren iki veriyi birleştirmek için artı (+) kullanılır
Microsoft = "Microsoft Learn "
Ambassador = "Student Ambassador"
print(Microsoft+Ambassador)

#upper() fonksiyonu bütün harfleri büyük harf yapar
küçükKulüp = "istanbul üniverstesi roket ve uzay klübü"
print(küçükKulüp.upper())

#lower() fonksiyonu bütün harfleri küçük harf yapar
büyükKulüp = "İSTANBUL ÜNIVERSTESI ROKET VE UZAY KLÜBÜ"
print(küçükKulüp.lower())
