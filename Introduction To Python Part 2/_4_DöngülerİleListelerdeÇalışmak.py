#While ile liste içinde dolanmak
numbers = [1,2,3,4,5,6,7,8,9]
#For ile liste içinde dolanmak / hem range - hem in ile

#Eğer indeks üzerinden işlem döndürmek isterseniz ;
length = len(numbers)
for i in range(0,length):
    print(numbers[i])

print("**********************")

#Daha kısa yol olarak bunu kulanmanız daha iyi olur
for i in numbers :
    print(i)

#for döngüsü ile liste öğlerin ortalamasını hesaplayın.
sum=0
for i in numbers :
    sum+=i # sum = sum + i

print(sum/length)
