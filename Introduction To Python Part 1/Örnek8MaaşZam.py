#Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteren Python örneği
#Hem maaşi hem zam oranını isteyiniz
#Zam oranı % üzerinden isteyin(%30 %50 gibi)


salary = float(input("Maaşınızı giriniz : "))
riseRate = int(input("Zam oranını giriniz(%) : "))
risedSalary = salary + (salary*(riseRate/100))
print("Zamlı maaş : "+ str(risedSalary))
