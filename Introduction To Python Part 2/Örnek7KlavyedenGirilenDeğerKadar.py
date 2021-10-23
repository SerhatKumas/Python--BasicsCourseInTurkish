#Klavyeden 0 girilene kadar sayıların toplamını bulan Program Python
#siz 0 girene kadar girdiğiniz sayıları toplar siz 0 girince toplamı yaza
sum=0
while True:
    number = float(input("Bir sayı girin: "))
    if number ==0:
        break
    sum+=number
print("Girdiğiniz sayıları toplamı: ",sum)