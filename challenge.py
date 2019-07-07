"""
burada mülaktlarda karşılaştığım kod sorularına yer ayıracağım. Python ın özel fonksiyonları haricinde
daha ortak olan komutlar kullanılmaya çalışıldı örneğin set() gibi
1- özel komutlar kullanmadan bir listedeki sayılardan kaç tane olduğunu gösteren komut

"""
def howMany(liste=[1,12,85,1,5,85,4,12,85,1,1]):
    dic={}
    for i in liste:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    return dic


"""
2- bir dizi içinde 1,2,3,4,5 diye sayılar dizili bunu 5,4,3,2,1 diye sıralayan kod
"""

def returnList(liste=[1,2,3,4,5]):

    for i in range(len(liste)//2):
        liste[i],liste[(len(liste)-i-1)]    =   liste[(len(liste)-i-1)],liste[i]
    return liste

"""
3- elimizde şöyle bir dizi var [1,1,0,0,0,1,1,0,0,1,1,1,1,0,0,1,1,1,1]
bu dizi ilk 1 ile başlıyor sonra 0 ı geldiğinde en son 1 in ve bir lerin başlangıcının indisini tutsun
sonra 0 başlıyor nuda diğer 1 i görene kadar indisini tutsun yani
((0,1),(2,4),(5,6),(7,8),(9,12),(13,14),(15,18)) bu çıktıyı versin
(0,1) ilk karşımıza çıkan 1 in indisi sıfır sonra 0 a gelendğinde en son 1 .in indisi 1


"""

def findIndis(liste=[1,1,0,0,0,1,1,0,0,1,1,1,1,0,0,1,1,1,1]):
    pass

"""
4- verilen sayının basmaklarına ayıran ve toplamını veren fonksiyon
note for i in str(sayi): kullanmadan
"""

def DigitSum(sayi=4856):
    sum=0
    while sayi>1:
        kalan=sayi%10
        sayi=sayi-kalan
        sayi=sayi//10
        sum+=kalan
    return sum
