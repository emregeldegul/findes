# Findes v2

[![N|Solid](http://i.hizliresim.com/ZZpnVg.png)](http://emregeldegul.net)

Findes | Dosya ve Klasör Tarama Programı
Linux için "locate" ve "find" benzeri bir dosya arama programı.

  - Dosya İçinde ve Dosya İsminde Tarama Yapabilme
  - Dosya Tipini Belirtme
  - Açılamayan Dosya Sayısını Bildirme
  - İstenmeyen Kelimeleri Yok Sayma

### Kurulum
Kurulum için ek kütüphaneye gerek yoktur.
Kurulum için aşağıda ki komutları terminale vermeniz yeterli.

```sh
$ git clone https://github.com/MuReCoder/findes.git
$ cd findes
$ sudo mv findes.py /usr/bin/findes
$ sudo chmod +x /usr/bin/findes
```
Bu komutlar klonlanan "findes" deposu içerisinde ki "findes.py" dosyasını global programların bulunduğu dizine göndererek istenilen yerden "findes" denilerek programın çalışmasını sağlıyor.
### Kullanımı
Yardım menüsü için" findes -h" diyebilirsiniz.
```
$ findes -h
```
Tarama yapmak için -s parametresi göndermeniz yeterli.
```
$ findes -s "mure"
```

Bu kök dizinde, dosya isimlerinde "mure" olan dosyaları ekrana basacaktır.

```
$ findes -s "mure" -d "/home/es"
```

-d parametresi hangi dizinde tarama yapılacağını belirtir. Varsayılan değer "/" (kök) dizindir.

```
$ findes -s "mure" -d "/home/es" -t "pd"
```

-t parametresi ek işlemleri belirler. Varsayılan olarak "p" değerini alır.

- p => Dosya isimlerinde arama yapar.
- c => dosya içeriklerinde arama yapar.
- d => Verilen yolun dosya mı yoksa klasör mü olduğunu belirtir.
- n => Açılamayan dosya sayısını ve yollarını belirtir.
- m => tam eşleşme yapar. Örneğin -s "mure" diye yaptığınız aramalarda "Mure" değeri olan verileri ekrana dökmez.

```
$ findes -s "mure" -d "/home/es" -t "pd" -p "hack"
```

-p parametresisinde verilen değer, eğer bulunan yolda mevcutsa veriyi ekrana basmaz.
