#Kullanıcıdan aldığı iki sayı ile toplama, çıkartma, çarpma ve bölme işlemlerini yapan basit bir hesap makinesi kodunu yazınız.
print("Yapmak istediğiniz işlemi seçiniz. ( '1' Toplama - '2' Çıkarma - '3' Çarpma - '4' Bölme ) ")

def Mult(x, y):
    return x * y


def Divide(x, y):
    return x / y


def Sum(x, y):
    return x + y


def Subs(x, y):
    return x - y


process = input("Seçim :")

number1 = int(input("1. Sayı Giriniz: "))

number2 = int(input("2. Sayı Giriniz: "))

if process == '1':

    print("n", number1, " + ", number2, " = ", Sum(number1, number2))

elif process == '2':

    print("n", number1, " - ", number2, " = ", Subs(number1, number2))

elif process == '3':

    print("n", number1, " * ", number2, " = ", Mult(number1, number2))

elif process == '4':

    print("n", number1, "/ ", number2, " = ", Divide(number1, number2))
else:
    print(" Lütfen işlem yapmak için 1-2-3-4 seçeneklerinden birini seçiniz. ")

