# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 10:44:47 2019

@author: yavuz
"""

"""

Soru 1: Elemanları interger olan bir array içerisinde birbirine komşu olmayan elemanlarından oluşan alt kümeler oluşturularak bu alt kümeler arasındak toplamı en büyük olan alt kümeyi bulunuz.



Örnek olarak verilen array şu şekilde olsun arr=[-2,1,3,-4,5] alt kümeleri aşağıdaki gibi olacaktır



AltKüme      Toplam

[-2, 3, 5]   6

[-2, 3]      1

[-2, -4]    -6

[-2, 5]      3

[1, -4]     -3

[1, 5]       6

[3, 5]       8



En büyük toplam 8 olur.



"""


arr = [-2,-12,-3,-4,-5]

def altKumedeEnBuyukToplamBul(arr=[-2,-1,-3,-4,-5]):
    #tanımlanan elemanların hepsinin negatif olduğu
    eskiToplam = 0
    baslangic=1
    simdikitoplam=arr[0]
    #eğer bütün elemanlar negatif değilse
    if len([i for i in arr if i>0])>0:
        simdikitoplam=0
        baslangic=0
        
    #array i 
    for i in range(baslangic,len(arr)):
      temp = simdikitoplam
      simdikitoplam = max(eskiToplam + arr[i], simdikitoplam)
      eskiToplam = temp
      
    print(simdikitoplam)
    
altKumedeEnBuyukToplamBul(arr)




"""
Soru 2: a'den b'ye kadar olan sayılardan, x'e tam bölünenlerin toplamını veren bir fonksiyon yazınız.
"""
def bolunenBul(a=2,b=20,x=5):
    sumx=0
    for i in range(a,b):
        if i%x==0:
            sumx+=i

    
    return sumx


