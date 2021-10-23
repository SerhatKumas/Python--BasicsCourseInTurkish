"""
Soru: Permütasyon nesnelerin diziliş sayısını bulmamızı sağlar. 6 arkadaştan 4’ü masaya oturucaktır.
Bu 4 kişi kaç farklı şekilde masaya oturabilir sorusuna çözüm bulmak için permütasyon kullanırız.
Aldığı sayılara göre permütasyon hesabı yapan kodu yazınız.
"""
def factorial(i):
    if i == 1:
        return 1

    else:
        return i * factorial(i - 1)


def permutation(j, k):
    l = 0

    if k > j:
        l = l

    else:
        l = factorial(j) / factorial(j - k)
        return l


print("Permütasyon hesabı için lütfen sayıları giriniz.")

number1 = int(input("1. Sayı Giriniz: "))

number2 = int(input("2. Sayı Giriniz: "))

print("nSonuç:", permutation(number1, number2))