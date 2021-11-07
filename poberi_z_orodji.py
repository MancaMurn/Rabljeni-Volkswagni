import orodja
import re
import requests

STEVILO_STRANI = 6
STEVILO_FILMOV_NA_STRAN = 50

vzorec = re.compile(
    r'<!--SHOW BANNER -+>.*?'
    r'<div class="row bg-white .*?'
    r'<span>(?P<ime>)</span>.*?'
    r'1.resgistracija.*?<td class=.*?>(?P<leto_prve_registracije>)</td>.*?'
    r'Prevoženih.*?<td class=.*?>(?P<prevoženi_kilometri>) km</td>.*?'
    r'Gorivo.*?<td class=.*?>(?P<vrsta_goriva>)</td>.*?'
    r'Menjalnik.*?<td class=.*?>(?P<vrsta_menjalnika>)</td>.*?'
    r'Motor.*?<td class=.*?>(?P<vrsta_motorja>)</td>.*?'
    r'<!-+ CENA -*>.*?<div class="GO-Results-Price-TXT-Regular">(?P<cena>).*?€</div>',
    flags=re.DOTALL
)

najdeni_avti = 0
for stran in range(STEVILO_STRANI):
    count = stran + 1
    url = (
        f'https://www.avto.net/Ads/results.asp?znamka=Volkswagen&model=&modelID=&tip=katerikoli%20tip&znamka2=&'
        f'model2=&tip2=katerikoli%20tip&znamka3=&model3=&tip3=katerikoli%20tip&cenaMin=0&cenaMax=999999&letnikMin=0&'
        f'letnikMax=2090&bencin=0&starost2=999&oblika=0&ccmMin=0&ccmMax=99999&mocMin=0&mocMax=999999&kmMin=0&'
        f'kmMax=9999999&kwMin=0&kwMax=999&motortakt=0&motorvalji=0&lokacija=0&sirina=0&dolzina=&dolzinaMIN=0&'
        f'dolzinaMAX=100&nosilnostMIN=0&nosilnostMAX=999999&lezisc=&presek=0&premer=0&col=0&vijakov=0&EToznaka=0&'
        f'vozilo=&airbag=&barva=&barvaint=&EQ1=1000000000&EQ2=1000000000&EQ3=1000000000&EQ4=100000000&'
        f'EQ5=1000000000&EQ6=1000000000&EQ7=1110100120&EQ8=1010000001&EQ9=1000000000&KAT=1010000000&PIA=&'
        f'PIAzero=&PSLO=&akcija=0&paketgarancije=&broker=0&prikazkategorije=0&kategorija=0&ONLvid=0&ONLnak=0&'
        f'zaloga=1&arhiv=0&presort=3&tipsort=DESC&stran={count}&'
    )
    datoteka = f'rabljeni-volkswagni/{stran}.html' 
    orodja.shrani_spletno_stran(url, datoteka)
    vsebina = orodja.vsebina_datoteke(datoteka)

    for zadetek in re.finditer(vzorec, vsebina):
        # print(zadetek.groupdict())
        najdeni_avti += 1

print(najdeni_avti)