"""
Çarpım tablosunu
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5
1 x 6 = 6
1 x 7 = 7
1 x 8 = 8
1 x 9 = 9

1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 lar dahil olmak üzere
şeklinde hepsini yazdırınız

"""
for i in range(1,10):
    print("*************************")
    for k in range(1,10):
        print(i,"x",k,"=",i*k)