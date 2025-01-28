from tkinter import Label, Tk #grafik arayüzünü kullanmak için gerekli olan kod yazılımı
import time #dijital saat için gerekli olan kütüphaneyi yazdım

uyhulama_penceresi=Tk()#bir metot oluşturuduk tk burada pencere oluşturmamızı sağladı
uyhulama_penceresi.title("Dijital saat") #başlığı verdik
uyhulama_penceresi.geometry("250x250") #boyutunu belitledik 
uyhulama_penceresi.resizable(1,1)#kullanıcının uygulama boyutunu değiştirmesine izin verdim
uyhulama_penceresi.configure(bg="black")#pencerenin arka plan rengini siyah yapmamı sağlar
background= "black"
foreground="white"
#saat etiketi
saat_etiket= Label(uyhulama_penceresi,font=("Boulder",18),bg=background, fg=foreground)
saat_etiket.grid(row=0,column=1,padx=10,pady=10)
#tarih etiketi
tarih_etiket=Label(uyhulama_penceresi,font=("Boulder",18),bg=background,fg=foreground)
tarih_etiket.grid(row=1,column=1,padx=10,pady=10)

def dijital_saat():
    time_live=time.strftime("%H:%M:%S")
    saat_etiket.config(text=time_live)
    #tarih alanı
    date_info =time.strftime("%d %B %Y")
    tarih_etiket.config(text=date_info)
    saat_etiket.after(200,dijital_saat)
dijital_saat()





uyhulama_penceresi.mainloop()#ekranda görüntü oluşturmam için gerekli olan kod kısmı burası burayı yazmazsak görüntü olmaz ve kodun en sonunda yer almak zorundadır.