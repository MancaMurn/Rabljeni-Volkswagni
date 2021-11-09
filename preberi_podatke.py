import re
import orodja


#spletne strani sem shranila na roke, saj druga orodja niso delovala.

vzorec_avto = re.compile(
    r'<!-- SHOW BANNER -+>.*?'
    r'<div class="row bg-white .*?'
    r'<span>(?P<ime>.+?)</span>.*?'
    r'1.registracija.*?<td class=.*?>(?P<leto_prve_registracije>.+?)</td>.*?'
    r'Prevoženih.*?<td class=.*?>(?P<prevozeni_kilometri>.+?) km</td>.*?'
    r'Gorivo.*?<td class=.*?>(?P<vrsta_goriva>.+?)</td>.*?'
    r'Menjalnik.*?<td class=.*?>(?P<vrsta_menjalnika>.+?)</td>.*?'
    r'Motor.*?<td class=.*?>\n *(?P<vrsta_motorja>.+?)\n *</td>.*?'
    r'<div class="GO-Results.*?Price-TXT-.*?">(?P<cena>\d.*?) €?</div>',
    flags=re.DOTALL
)


vzorec_model = re.compile(
    r'[Vv]olkswagen (?P<model>.*?) .*',
    flags=re.DOTALL
)



def izloci_podatke_avta(seznam_slovarjev):
    for i in range(len(seznam_slovarjev)):
        avto = seznam_slovarjev[i]
        avto['leto_prve_registracije'] = int(avto['leto_prve_registracije'])
        avto['prevozeni_kilometri'] = int(avto['prevozeni_kilometri'])
        #avto['cena'] = int(avto['cena'])
        avto['ime'] = vzorec_model.search(avto['ime']).group(1)



avti = []
stevec = 0
for i in range(1, 22):
    stran = orodja.vsebina_datoteke(f"stran_{i}.html")
    najdeni = vzorec_avto.finditer(stran)
    for avto in najdeni:
        # print(stevec, avto.groupdict())
        stevec += 1
        avti.append(avto.groupdict())

izloci_podatke_avta(avti)
print(avti)

orodja.zapisi_json(avti, 'obdelani-podatki/avtomobili.json')
orodja.zapisi_csv(
    avti, 
    ['ime', 'leto_prve_registracije', 'prevozeni_kilometri', 'vrsta_goriva', 'vrsta_menjalnika', 'vrsta_motorja', 'cena'],
    'obdelani_podatki/avtomobili.csv')