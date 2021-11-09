import re



vzorec_bloka = re.compile(
    r'<!-- SHOW TOP PONUDBA -*?>'
    r'.*?'
    r'<!-- SHOW BANNER -*?>',
    flags=re.DOTALL
)


vzorec_avto = re.compile(
    r'<!-- SHOW BANNER -+>.*?'
    r'<div class="row bg-white .*?'
    r'<span>(?P<ime>.+?)</span>.*?'
    r'1.registracija.*?<td class=.*?>(?P<leto_prve_registracije>.+?)</td>.*?'
    r'Prevoženih.*?<td class=.*?>(?P<prevoženi_kilometri>.+?) km</td>.*?'
    r'Gorivo.*?<td class=.*?>(?P<vrsta_goriva>.+?)</td>.*?'
    r'Menjalnik.*?<td class=.*?>(?P<vrsta_menjalnika>.+?)</td>.*?'
    r'Motor.*?<td class=.*?>(?P<vrsta_motorja>.+?)</td>.*?'
    r'<!-+ CENA -*>.*?<div class="GO-Results-Top-Price-TXT-.*?">(?P<cena>.+?).*?€</div>',
    flags=re.DOTALL
)



def vsebina(dat):
    with open(dat, encoding='utf-8') as dat:
        return dat.read()


stevec = 0
niz = vsebina('stran_1.html')
najdeni = vzorec_avto.finditer(niz)
for zadetek in najdeni:
    print(stevec, zadetek)
    stevec += 1

# avti = []
# stevec = 0
# for i in range(1, 22):
#     stran = vsebina(f"stran_{i}.html")
#     najdeni = vzorec_avto.finditer(stran)
#     for avto in najdeni:
#         print(stevec, avto)
#         stevec += 1
#         avti.append(avto)


