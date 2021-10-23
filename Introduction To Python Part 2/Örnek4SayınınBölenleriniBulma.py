#Kullanıcının girdiği sayının pozitif tam bölenlerini bulan kodu yazınız.
#Sadece ekrana bastırmanız yeterli ama isteyen listeye ekleyip sonra da yazdırabilir

def findDivider(number):
    dividerList = []
    for i in range(1,number+1):
        if (number % i == 0):
            dividerList.append(i)
    return dividerList

while True:
    number = input("Bölenlerini bulmak istediğiniz sayıyı giriniz (Çıkmak için 'q'):")
    if (number == "q"):
        print("Programdan Çıkılıyor...")
        break
    else:
        number = int(number)
        print(findDivider(number))