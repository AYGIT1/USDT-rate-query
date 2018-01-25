#
# bittrex üzerindeki kriptoparaların dolar karşılığını veren basit bir program
#

import requests

def sorgula():
    veri = requests.get("https://bittrex.com/api/v1.1/public/getmarketsummaries")
    while True:
        isim = "USDT-" + input("USDT karşılığını görmek istediğiniz kriptopara kodunu yazın (Örn. : BTC, ETH)")
        isim = isim.upper()
        i=0
        try:
            while isim != veri.json()["result"][i]["MarketName"]:
                i=i+1
        except IndexError:
            print("Girilen birimin USDT karşılığı bulunamadı.")
        else: break
    print(veri.json()["result"][i]["Last"])
sorgula()

for n in range(3):
    Cevab = input("Tekrar ara?(E/H)")
    if Cevab == ('e' or 'E'):
        sorgula()
    elif Cevab == ('h' or 'H'):
        break
    else:
        print("Hatalı giriş.")
    continue
