# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 20:30:07 2019

@author: Ruhsuz Sirin
"""
import urllib.request
#https://www.crummy.com/software/BeautifulSoup/bs4/doc/#css-selectors
from bs4 import BeautifulSoup
import codecs

def sitedenBilgileriAl():    
    for i in range(1,68,1): #Sayfa bilgilerin çekilmesi
        url = "https://www.memrise.com/course/1075974/ingilizce-temel-kelimeler/"+str(i)
        fp = urllib.request.urlopen(url)
        mybytes = fp.read()
        html_doc = mybytes.decode("utf8")
        fp.close()
        soup = BeautifulSoup(html_doc, 'html.parser')
        col_a = soup.findAll("div", {"class": "col_a col text"})
        col_b = soup.findAll("div", {"class": "col_b col text"})
        kelimeBasligi = soup.findAll("h3", {"class": "progress-box-title"}) 
        kelimeBasligi = kelimeBasligi[0].get_text().strip()
        
        print(kelimeBasligi)
        f = codecs.open("kelimeler/"+kelimeBasligi+".txt","w+","utf-8")        
        for col_a_index in range(0,len(col_a),1): # Bilgilerin alınması ve texte yazdırılması.
            digerCevaplarTr = ""
            strEkle = ""
            enSoru = col_a[col_a_index].get_text()
            trCevap = col_b[col_a_index].get_text()
            trCvplarMi = trCevap.find(",") # fazladan Türkçe anlamı var mı kontrolü
            if(trCvplarMi != -1):
                trCevaplar = trCevap.split(",")
                trCevap = trCevaplar[0]
                for c in range(1,len(trCevaplar),1):
                    digerCevaplarTr += trCevaplar[c].strip()+ ","
            
                digerCevaplarTr = digerCevaplarTr.rstrip(",")
            
            trCevap = trCevap.strip()
            strEkle = enSoru + "\t"+trCevap+""
            if(digerCevaplarTr != ""):
                strEkle += "\t\t"+digerCevaplarTr
            
            f.write(strEkle + '\n')
            
            print(strEkle)    
        
        f.close()
    

def main(): 
    sitedenBilgileriAl()

if __name__ == '__main__':
    main()