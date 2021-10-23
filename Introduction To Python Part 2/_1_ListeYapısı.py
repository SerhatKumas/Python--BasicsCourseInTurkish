"""
Python Programlama Dilinde 4 tür dize (array) bulunur. Bunlar;

List, sıralanabilir ve değiştirilebilir dizeler. Bu tarz dizelere aynı üyeler tekrar eklenebilir.
Tuple, sıralanabilir ancak değiştirilemez dizelerdir. Aynı üyeler birden fazla eklenebilir.
Set sıralanamaz ve aynı üyeleri kabul etmez.
Dictionary sıralanamaz ancak değiştirilebilir ve listelenebilir. Aynı üyeler eklenemez.

"""
# Diziler nasıl mı tanımlanır aşşağıdaki gibi işte ;
nameList = ["Serhat","Anıl","Damla"]
print(nameList)
idList = [101,204,123112,12,2]

# Dizideki herhangi bir elemana nasıl ulaşırız !! Arrayin başlangıç elemanının numarası(indeksi) 0 dan başlar
print(nameList[0])
print(nameList[1])
print(nameList[2])
print(idList[3])

# Bir dizenin belli elemanlarını aralık belirterek alabilirsiniz
thisList = ["elma", "muz", "kiraz", "portakal", "kivi", "karpuz", "mango"]
print(thisList[2:5])

# Eğer aralık belirtirken ilk sayıyı boş geçersek ilk elemandan belirtilen sayı kadar değeri dize haline dönüştürür
print(thisList[:5])

# Eğer ikinci parametre boş bırakılırsa bu durumda ilk belirtilen elemandan itibaren dizenin sonuna kadar değerler alınarak bir dize oluşturulur
print(thisList[:3])

#Dizedeki bir değeri değiştirmek ;
thisList[1] = "çilek"
print(thisList)

#Dizinin sonuna bir değer eklemek istediğimizde append() fonksiyonunu kullanırız
thisList.append("kivi")
print(thisList)

#Dize belli bir sıraya eleman eklemek için ise insert() fonksiyonu kullanılır
thisList.insert(2,"mandalina")
print(thisList)

#Dizeden istediğimiz bir değeri silmek için remove() fonksiyonunu kullanırız .
thisList.remove("çilek") # Parantex içinde silinmek istenen değer belirtilir

#Eğer dizinin blli bir sırasındaki eleman silineek ise pop() fonksiyon kullanılır
thisList.pop(2)
print(thisList)

#Listeleri kopyalamak için ise copy() methodu kullanılır
newThisList = thisList.copy()
print(thisList)
print(newThisList)

#Diziyi komple temizlemek için ise clear fonksiyou kullanılır
newThisList.clear()
print(newThisList)
#iki veya daha fazla listeyi birleştirmek için  (+) operatörünü kullanılır (Hatılarsanız string)
newestList = nameList+idList
print(newestList)

#Daha çok yöntemi var ama Canınız sıkılmasın daha geçelim ben aşağıya sayfaları bırakıyorum ordan daha ileri araştırmalar yapabilirsiniz
 # Türkçe : https://python.sitesi.web.tr/python-dizeler.html
 # Türkçe : https://www.mobilhanem.com/python-liste-ve-listenin-metotlari/
 #İngilizce : https://www.w3schools.com/python/python_lists.asp
