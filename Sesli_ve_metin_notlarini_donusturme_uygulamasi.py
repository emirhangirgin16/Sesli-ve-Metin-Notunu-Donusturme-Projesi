################################## Gerekli kütüphaneler ############################################################
import speech_recognition as sr #sesli notları metine çevirme
from gtts import gTTS #metni sesli hale getirme
import os #dosya sistemleri
import pygame #ses dosyalarını oynatmak için
import tkinter as tk
from tkinter import simpledialog, messagebox

################################### sesli notu metine çevir ########################################################
def sesli_notu_metine_cevir(): # sesli notu metine çevirecek fonksiyonu tanımladım
    recognizer = sr.Recognizer() #Ses tanıma için bir tanıyıcı oluşturur
    with sr.Microphone() as source: #Mikrofonu ses kaynağı olarak kullanır
        print("Lütfen not almak için konuşunuz:")
        audio = recognizer.listen(source) #Kullanıcıdan ses kaydı alır
    try:
        metin = recognizer.recognize_google(audio, language="tr-TR") #Google'ın ses tanıma hizmetini kullanarak sesi metine dönüştürür.
        print("söylediğiniz:", metin)
        with open("notlar.txt", "a", encoding="utf-8") as dosya: #Metni notlar.txt dosyasına ekler.
            dosya.write(metin + "\n")
        metni_seslendir("notunuz kaydedildi: " + metin) #Kaydedilen metni sesli olarak oynatır.
    except sr.UnknownValueError: #hata sistemi hata yapılırsa kullanıcıya fırlatmak için ekledim
        print("Hata", "Anlaşılamayan ses.")
    except sr.RequestError:
        print("Hata", "Servise erişilemiyor.")

def metni_seslendir(metin):  #Bu fonksiyon verilen metni sesli hale getirir ve oynatır.
    tts = gTTS(text=metin, lang='tr')  #metni sesli hale getirir.
    tts.save("output.mp3")  #Sesli metni output.mp3 dosyasına kaydeder.
    pygame.mixer.init()  #init ile pygame metodu başlar
    pygame.mixer.music.load("output.mp3")  #ses dosyasını yükler
    pygame.mixer.music.play()   #ses dosyasını oynatır
    while pygame.mixer.music.get_busy():  #Ses çalma işlemi bitene kadar bekler.
        continue  

def metni_oku(): #Bu fonksiyon metin giriş alanından alınan metni sesli hale getirir ve oynatır.
    metin = metin_girisi.get("1.0", "end-1c")
    tts = gTTS(text=metin, lang='tr')
    tts.save("metin.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("metin.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue

# Metin girme penceresi
def metin_penceresi_ac():#Bu fonksiyon  kullanıcıdan metin girişi almak için yeni bir pencere açar.
    metin_pencere = tk.Toplevel() #Ana pencerenin üstünde yeni bir pencere oluşturur.
    metin_pencere.title("Metin Giriniz") #Yeni pencereye başlık verir.
    global metin_girisi  # değişkenini global hale getirir, böylece diğer fonksiyonlar tarafından kullanılabilir.
    metin_girisi = tk.Text(metin_pencere, height=10, width=50)
    metin_girisi.pack()
    okuma_button = tk.Button(metin_pencere, text="Metni Sesli Çal", command=metni_oku)
    okuma_button.pack()

# Ana arayüz
app = tk.Tk() #ana uygulama penceresini oluşturur
app.title("Sesli ve Metin Notları Dönüştürme Uygulaması")# başlık
app.geometry("275x175")

sesli_notu_metine_cevir_buttonu = tk.Button(app, text="Sesli not al", command=sesli_notu_metine_cevir) #sesli notu metine çeviren buton
sesli_notu_metine_cevir_buttonu.pack(pady=10)#gözükmesi için paket haline getirdim

metin_notu_button = tk.Button(app, text="Metin giriniz", command=metin_penceresi_ac)#metini sese çeviren buton
metin_notu_button.pack(pady=10)#paket 

app.mainloop()#uygulamanın çalışmasını sağlar bu olmazsa olmaz

     


     


