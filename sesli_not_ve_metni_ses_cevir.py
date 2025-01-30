##################################### Gerekli kütüphaneler ########################################################
import speech_recognition as sr
from gtts import gTTS
import os
import pygame
import tkinter as tk
from tkinter import simpledialog
#################################### Sesli notu metine çeviren fonksiyon ##########################################
def sesli_notu_metine_cevir():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Konuşmanızı bekliyorum:")
        audio=recognizer.listen(source)
    try:
        metin=recognizer.recognize_google(audio,language="tr-TR")
        print("Söylediğiniz:", metin)
        with open ("notlar.txt","a",encoding="utf-8") as dosya:
            dosya.write(metin + "\n")
        metni_seslendir("Notunuz kaydedildi:")
    except sr.UnknownValueError:
        print("Dediğinizi anlayamadım, lütfen tekrar eder misiniz ?")
        metni_seslendir("Dediğinizi anlayamadım, lütfen tekrar eder misiniz ?")
    except sr.RequestError:
        print("Sesli tanıma hizmetine ulaşılamadı. Lütfen tekrar denenyin.")
        metni_seslendir("Sesli tanıma hizmetine ulaşılamadı. Lütfen tekrar denenyin.")
###################################### Metni seslendiren fonksiyon #################################################
def metni_seslendir(metin):
    tts=gTTS(text=metin,lang='tr')
    dosya_yolu=os.path.join(os.getcwd(),"cevap.mp3")
    if os.path.exists(dosya_yolu):
        os.remove(dosya_yolu)
    tts.save(dosya_yolu)
    pygame.mixer.init()
    pygame.mixer_music.load(dosya_yolu)
    pygame.mixer_music.play()
    while pygame.mixer_music.get_busy():
        continue
###################################### Metin girişini yapan ve bunu sese çevirmeye atayan fonksiyon###################
def metin_notu_al():
    metin = simpledialog.askstring("Lütfen metni giriniz", "Notunuzu yazın:")
    if metin:
        metni_seslendir(metin)
###################################### Tasarım kısmı ################################################################
app=tk.Tk()
app.title("Sesli ve Metin Notları Dönüştürme uygulaması")
app.geometry("400x350")

sesli_not_butonu= tk.Button(app,text="Sesli not al",command=sesli_notu_metine_cevir,padx=10,pady=10)
sesli_not_butonu.pack(pady=10)
metni_sese_cevir_butonu=tk.Button(app,text="Metin giriniz",command=metin_notu_al,padx=10,pady=10)
metni_sese_cevir_butonu.pack(pady=10)
app.mainloop()

