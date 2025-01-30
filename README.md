Sesli ve Metin Notları Dönüştürme Uygulaması
Proje Hakkında
Bu proje, kullanıcıların sesli notlarını metne dönüştürmelerini ve metinlerini sesli olarak dinlemelerini sağlayan bir uygulamadır. Python kullanılarak geliştirilmiştir ve kullanıcı dostu bir arayüze sahiptir. Uygulama sayesinde sesli notlarınızı metin dosyasına kaydedebilir ve metinlerinizi sesli olarak dinleyebilirsiniz.
###################################################################################################################3
Özellikler
Sesli Notları Metne Çevirme: Mikrofon aracılığıyla alınan sesli notları metne dönüştürür ve bir dosyaya kaydeder.

Metin Notlarını Sesli Çalma: Kullanıcının girdiği metni sesli olarak oynatır.
#####################################################################################################################
Kullanılan Teknolojiler
Python: Ana programlama dili olarak kullanılmıştır.

tkinter: Grafik kullanıcı arayüzü (GUI) tasarımı için kullanılmıştır.

speech_recognition: Sesli notları metne dönüştürme işlevselliği sağlar.

gTTS (Google Text-to-Speech): Metinleri sesli olarak çıktıya dönüştürmek için kullanılmıştır.

pygame: Ses dosyalarını oynatmak için kullanılmıştır.
##################################################################################################################
Gereksinimler
Python 3.13.0

Gerekli Python kütüphaneleri:

speech_recognition

gTTS

pygame

tkinter

simpledialog, messagebox
####################################################################################################################
Kullanım
Sesli Not Almak İçin: "Sesli not al" butonuna tıklayın ve konuşmaya başlayın. Konuşmanız metne dönüştürülüp notlar.txt dosyasına kaydedilecektir.

Metin Notu Girmek İçin: "Metin giriniz" butonuna tıklayın ve metninizi girin. Girdiğiniz metin sesli olarak oynatılacaktır.
####################################################################################################################
                                      #kodları açıklama
1. Sesli Notu Metine Çevirme
Buton: "Sesli not al"

İşlev: Kullanıcıdan alınan sesli notu metine çevirir ve notlar.txt dosyasına kaydeder. Ayrıca, çevirilen metni sesli olarak oynatır.

2. Metin Girişi ve Sesli Çalma
Buton: "Metin giriniz"

İşlev: Yeni bir pencere açar ve kullanıcıya metin girme olanağı tanır. Giriş yapılan metin sesli olarak çalınır.

Kod Açıklaması
sesli_notu_metine_cevir()
Bu fonksiyon, mikrofon üzerinden alınan sesli notları metine çevirir ve notlar.txt dosyasına kaydeder. Ardından, çevirilen metni sesli olarak oynatır.

metni_seslendir(metin)
Bu fonksiyon, verilen metni sesli hale çevirir ve pygame kullanarak ses dosyasını çalar.

metni_oku()
Bu fonksiyon, metin girme alanından alınan metni sesli hale çevirir ve pygame kullanarak ses dosyasını çalar.

metin_penceresi_ac()
Bu fonksiyon, kullanıcıdan metin girişi almak için yeni bir pencere açar ve girilen metni sesli olarak çalmak için bir buton ekler.

Yazar
Bu uygulama, [Emirhan Girgin] tarafından geliştirilmiştir.
