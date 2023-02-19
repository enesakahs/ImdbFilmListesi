import requests
import json
import time
import re
import textwrap #cıktı(print) alanında yapacagımız degısıklıkler ıcın kullanılıyor

class Film:
    def __init__(self):
        self.dongu=True

    def program(self):
        secim=self.menu()
        if secim=="1":
            self.eniyi250()
        if secim=="2":
            self.enpopuler()
        if secim=="3":
            self.sinemalarda()
        if secim=="4":
            self.yakında()
        if secim=="5":
            self.filmara()
        if secim=="6":
            self.cıkıs()

    def menu(self):
        def control(secim):
            if re.search("[^1-6]",secim):
                raise Exception ("lutfen 1 ve 6 arasında gecerlı bır secım yapınız")
            elif len(secim)!=1: #girilen degerın uzunlugunu burda 1 diye belırtmezsek 14 veya 41 gibi girilen degerlerde sistem icinde 1 ve 4 oldugu ıcın hata vermez
                raise Exception ("lutfen 1 ve 6 arasında gecerlı bır secım yapınız")
        while True:
            try:
                secim=input("Merhabalar IMDB Sitesine Hosgeldiniz.\n\nLutfen yapmak ıstedıgınız ıslemı secınız..\n\n1-En İyi 250 Film\n2-En Popüler Filmler\n3-Sinemalarda Olan Filmler\n4-Yakında Cıkacak Filmler\n5-Film Ara\n6-Cıkıs Yap\n\n")
                control(secim)
            except Exception as hata:
                print(hata)
                time.sleep(3)
            else:
                break
        return secim 


    def eniyi250(self):#1
        print("En İyi 250 Film Listesine Ulasılıyor..\n\n")
        time.sleep(2)
        url=requests.get("https://imdb-api.com/en/API/Top250Movies/k_qarfijqk")
        sonuc=url.json()

        #ıtems yapısı üzerinden for dongusu ile herbirinin fullTitle'ını döndürdük
        for i in sonuc["items"]:
            print(i["fullTitle"])
        self.menudon()

    def enpopuler(self):
        print("En Popüler Film Listesine Ulasılıyor..\n\n")
        time.sleep(2)
        url=requests.get("https://imdb-api.com/en/API/MostPopularMovies/k_qarfijqk")
        sonuc=url.json()

        for i in sonuc["items"]:
            print(i["fullTitle"])
        self.menudon()

    def sinemalarda(self):
        print("Sinemalarda Olan Filmler Listesine Ulasılıyor..\n\n")
        time.sleep(2)
        url=requests.get("https://imdb-api.com/en/API/InTheaters/k_qarfijqk")
        sonuc=url.json()

        for i in sonuc["items"]:
            print(i["fullTitle"])
        self.menudon()

    def yakında(self):
        print("Yakında Vizyona Girecek Filmler Listesine Ulasılıyor..\n\n")
        time.sleep(2)
        url=requests.get("https://imdb-api.com/en/API/ComingSoon/k_qarfijqk")
        sonuc=url.json()

        #ıtems yapısı üzerinden for dongusu ile herbirinin fullTitle'ını döndürdük
        for i in sonuc["items"]:
            print(i["fullTitle"])
        self.menudon()

    def filmara(self):
        print("Arama Moturu Calıstırılıyor")
        time.sleep(2)
        film=input("Aramak İstediğiniz Film Adınız Giriniz: ")
        url=requests.get("https://imdb-api.com/en/API/Top250Movies/k_qarfijqk")
        sonuc=url.json()

        ID=list() #bos liste olusturduk
        for i in sonuc["items"]: #ıtems ustunden her bır ID yi listeye farklı bir eleman gibi ekledik
            ID.append(i["id"])

        AD=list() #bos liste olusturduk
        for i in sonuc["items"]: 
            AD.append(i["title"])
        
        #zip ile birlestirdik bos listeleri
        birlestir=zip(AD,ID) #Key,Value
        veri=dict(birlestir)
        key=veri.get(film) #get sözlükte girilen anahtar kelimeye karsı gelen degeri verecek

        url2=requests.get("https://imdb-api.com/tr/API/Wikipedia/k_qarfijqk/{}".format(key))
        sonuc2=url2.json()

        print(textwrap.fill(sonuc2["plotShort"]["plainText"]),200)
        #textwrap.fill ,200 film acıklamsını 200 karakterden bölüyor.
        self.menudon()

    def cıkıs(self):
        print("IMDB Sitesinten Cıkıs Yapılıyor")
        time.sleep(3)
        self.dongu=False
        exit()

    def menudon(self):
        while True:
            x=input(print("Ana menuye donmek ıcın 7, Cıkmak ıcın lutfen 6'e basınız.\n"))
            if x=="7":
                print("ana menuye dönüyorsunuz..")
                time.sleep(3)
                self.program()
                break
            elif x=="6":
                self.cıkıs()
                break
            else:
                print("gecerli bir deger giriniz.")

sistem=Film()
while sistem.dongu:
    sistem.program()


    