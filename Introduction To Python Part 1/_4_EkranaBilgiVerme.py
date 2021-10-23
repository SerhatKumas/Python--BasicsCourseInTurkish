#****************************************   EKRANA BİLGİ VERME   ****************************************************

#Pythondaki hazır bulunan print fonksiyonu : Ekrana bilgi vermek(çıktı , output) vermek için kullandığımız fonksiyondur
print("Hello world")

#' ' tırnak ile değer yazdırma
print('Hello world')

#" " tırnak ile değer yazdırma
print("Hello world")

#""" """ tırnak ile değer yazdırma
print("""Hello world""")

#!!! PEKİ NEDEN 3 TANE YAZMA ŞEKLİ VAR , 1 TANE YAPSALAR OLMAZ MIYDI ?
print("""Ali'nin arkadaşı "Yarın partye beraber gidelim" dedi""")

#END PARAMETRESİ : print() fonksiyonu ile ekrana verdiğimiz değerin sonunda hangi işlemi yapacağımızı belirtiyoruz ;
print("Bunun sonunda hiçbir şey yok",end="")
print("bunun önünde hiçbir şey yok\n")

#Birde virgül mü denesek ?
print("Bunun sonunda virgül var",end=",")
print("bunun önünde virgül var\n")

#Bu olmadı ya bence araya bir tab mesafesi boşluk bırakmayı mı denesek ?
print("Bunun sonunda bir tab kadar boşluk var",end="\t") #\t : bir tab boşluğu ifade eder
print("bunun önünde bir tab kadar boşluk var\n")

#Yada alt alta yazsak daha iyi olurmuş sanki ama end fonkdiyonunu kullanarak yazalım bence
print("Bir alt satıra geçti",end="\n") #\n : bir alt satıra geçmei ifade eder (new line)
print("Bir alt satıra geçti\n")

#SEP PARAMETRESİ : değerlerin arasında farklı işlemleri yapmamızı sağlar
print("www","unibloger","com\n",sep=".") #Bu internet adresinde noktalar eksik sanki , buna bir nokta ekleyelim

#* Parametresi : Aynı değişken üzerinde harf aralarında işlem yapmamızda yardımcı olur
print(*"Parametre")

