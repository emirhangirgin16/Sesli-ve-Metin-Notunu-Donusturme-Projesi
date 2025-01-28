################################# GEREKLİ KÜTÜPHANELER #############################################################
import tkinter as tk
from tkinter import filedialog # dosya yolunu kullanmak için gerekli 
import pyqrcode
from pyqrcode import QRCode # QR kod oluşturmak için gerekli 'QRcode' kısmı ise bizim istediğimiz klasik kare kod oluşturur
################################ FONKSİYON OLUŞTURMA ################################################################
def qr_kod_olusturucu():
    url=url_girdi.get()#girilen url'i çağırma 
    if url:
        qr_url=pyqrcode.create(url)#QR oluşturmaya yarar. oluşturduğumuz QR ise qr_url değişkenine atar
        dosya_yolu=filedialog.asksaveasfilename(defaultextension=".svg",filetypes=[("SVG DOSYASI","*.svg")])# ezber kod
        if dosya_yolu:
            qr_url.svg(dosya_yolu,scale=8)#dosya yolunu svg yaptıktan sonra dosya yolunu seçtim ve büyüklüğü 8 ayarladım (8-12 tavsiye edilir.)
            durum_etiketi.config(text="QR kod oluşturuldu ve kaydedildi.")
################################ TASARIM KISMINI OLUŞTURMA ###########################################################
uygulama_penceresi=tk.Tk()
uygulama_penceresi.title=("Dijital QR Kod oluşturucu")
etiket=tk.Label(uygulama_penceresi,text="lütfen QR kod oluşturmak istediğiniz bağlanyıyı yazınız:")
url_girdi=tk.Entry(uygulama_penceresi,width=40)
qr_kod_olustur_butonu=tk.Button(uygulama_penceresi,text="QR KOD OLUŞTUR",command=qr_kod_olusturucu)
durum_etiketi=tk.Label(uygulama_penceresi, text="")
################################ GRİD KISMI ###########################################################################
etiket.grid(row=0,column=0,padx=10,pady=10)
url_girdi.grid(row=0,column=1,padx=10,pady=10)
qr_kod_olustur_butonu.grid(row=1,column=0,columnspan=2,padx=10,pady=10)
durum_etiketi.grid(row=2,column=0,columnspan=2,padx=10,pady=10)
uygulama_penceresi.mainloop()




