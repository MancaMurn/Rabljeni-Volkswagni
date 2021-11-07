import re
import orodja


vzorec_bloka = re.compile(
    r'<!-- SHOW TOP PONUDBA -*?>'
    r'.*?'
    r'<!-- SHOW BANNER -*?>',
    flags=re.DOTALL
)

vzorec_avto = re.compile(
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

vzorec_model = re.compile(
    r'[Vv]olkswagen (?P<model>) .*',
    flags=re.DOTALL
)

# vzorec_osebe = re.compile(
#     r'<a\s+href="/name/nm(?P<id>\d+)/?[^>]*?>(?P<ime>.+?)</a>',
#     flags=re.DOTALL
# )

# vzorec_povezave = re.compile(
#     r'<a.*?>(.+?)</a>',
#     flags=re.DOTALL
# )

# vzorec_zasluzka = re.compile(
#     r'Gross:.*?data-value="(?P<zasluzek>(\d|,)+)"',
#     flags=re.DOTALL
# )

# vzorec_metascore = re.compile(
#     r'<span class="metascore.*?">(?P<metascore>\d+)',
#     flags=re.DOTALL
# )

# vzorec_oznake = re.compile(
#     r'<span class="certificate">(?P<oznaka>.+?)</span>',
#     flags=re.DOTALL
# )

# vzorec_daljsi_povzetek = re.compile(
#     r'<a href="/title/tt\d+/plotsummary.*?&nbsp;&raquo;',
#     flags=re.DOTALL
# )

# vzorec_igralcev = re.compile(
#     r'Stars?:(?P<igralci>.+?)</p>.*?',
#     flags=re.DOTALL
# )


# def izloci_osebe(niz):
#     osebe = []
#     for oseba in vzorec_osebe.finditer(niz):
#         osebe.append({
#             'id': int(oseba.groupdict()['id']),
#             'ime': oseba.groupdict()['ime'],
#         })
#     return osebe

    



def izloci_podatke_avta(blok):
    avto = vzorec_avto.search(blok).groupdict()
    avto['leto_prve_registracije'] = int(avto['leto_prve_registracije'])
    avto['prevozeni_kilometri'] = int(avto['prevozeni_kilometri'])
    avto['cena'] = int(avto['cena'])
    avto['ime'] = vzorec_model.search(avto['ime'])
    return avto
 # a bo to delovalo??




# def izloci_podatke_filma(blok):
#     film = vzorec_filma.search(blok).groupdict()
#     film['id'] = int(film['id'])
#     film['dolzina'] = int(film['dolzina'])
#     film['zanri'] = film['zanri'].strip().split(', ')
#     film['leto'] = int(film['leto'])
#     # odstranimo morebitno povezavo na daljši posnetek
#     film['opis'] = vzorec_daljsi_povzetek.sub('', film['opis'])
#     # odstranimo morebitne povezave v opisu
#     film['opis'] = vzorec_povezave.sub(r'\1', film['opis'])
#     film['opis'] = film['opis'].strip()
#     film['ocena'] = float(film['ocena'])
#     film['glasovi'] = int(film['glasovi'])
#     film['reziserji'] = izloci_osebe(film['reziserji'])
#     # zabeležimo oznako, če je omenjena
#     oznaka = vzorec_oznake.search(blok)
#     if oznaka:
#         film['oznaka'] = oznaka['oznaka']
#     else:
#         film['oznaka'] = None
#     # zabeležimo igralce, če so omenjeni
#     igralci = vzorec_igralcev.search(blok)
#     if igralci:
#         film['igralci'] = izloci_osebe(igralci['igralci'])
#     else:
#         film['igralci'] = []
#     # zabeležimo zaslužek, če je omenjen
#     zasluzek = vzorec_zasluzka.search(blok)
#     if zasluzek:
#         film['zasluzek'] = int(zasluzek['zasluzek'].replace(',', ''))
#     else:
#         film['zasluzek'] = None
#     # zabeležimo metascore, če je omenjen
#     metascore = vzorec_metascore.search(blok)
#     if metascore:
#         film['metascore'] = int(metascore['metascore'])
#     else:
#         film['metascore'] = None
#     return film



def avti_na_strani(st_strani, na_stran=250):
    url = (
        f'https://www.avto.net/Ads/results.asp?znamka=Volkswagen&model=&modelID=&tip=katerikoli%20tip&znamka2=&'
        f'model2=&tip2=katerikoli%20tip&znamka3=&model3=&tip3=katerikoli%20tip&cenaMin=0&cenaMax=999999&letnikMin=0&'
        f'letnikMax=2090&bencin=0&starost2=999&oblika=0&ccmMin=0&ccmMax=99999&mocMin=0&mocMax=999999&kmMin=0&'
        f'kmMax=9999999&kwMin=0&kwMax=999&motortakt=0&motorvalji=0&lokacija=0&sirina=0&dolzina=&dolzinaMIN=0&'
        f'dolzinaMAX=100&nosilnostMIN=0&nosilnostMAX=999999&lezisc=&presek=0&premer=0&col=0&vijakov=0&EToznaka=0&'
        f'vozilo=&airbag=&barva=&barvaint=&EQ1=1000000000&EQ2=1000000000&EQ3=1000000000&EQ4=100000000&'
        f'EQ5=1000000000&EQ6=1000000000&EQ7=1110100120&EQ8=1010000001&EQ9=1000000000&KAT=1010000000&PIA=&'
        f'PIAzero=&PSLO=&akcija=0&paketgarancije=&broker=0&prikazkategorije=0&kategorija=0&ONLvid=0&ONLnak=0&'
        f'zaloga=1&arhiv=0&presort=3&tipsort=DESC&stran={st_strani}&'
    )
    ime_datoteke = 'zajeti-podatki/rabljeni-volkswagni{}.html'.format(st_strani)
    orodja.shrani_spletno_stran(url, ime_datoteke)
    vsebina = orodja.vsebina_datoteke(ime_datoteke)
    for blok in vzorec_bloka.finditer(vsebina):
        yield izloci_podatke_avta(blok.group(0))


# def izloci_gnezdene_podatke(filmi):
#     REZISER, IGRALEC = 'R', 'I'
#     osebe, vloge, zanri = [], [], []
#     videne_osebe = set()

#     def dodaj_vlogo(film, oseba, vloga, mesto):
#         if oseba['id'] not in videne_osebe:
#             videne_osebe.add(oseba['id'])
#             osebe.append(oseba)
#         vloge.append({
#             'film': film['id'],
#             'oseba': oseba['id'],
#             'vloga': vloga,
#             'mesto': mesto,
#         })


#     for film in filmi:
#         for zanr in film.pop('zanri'):
#             zanri.append({'film': film['id'], 'zanr': zanr})
#         for mesto, oseba in enumerate(film.pop('reziserji'), 1):
#             dodaj_vlogo(film, oseba, REZISER, mesto)
#         for mesto, oseba in enumerate(film.pop('igralci'), 1):
#             dodaj_vlogo(film, oseba, IGRALEC, mesto)

#     osebe.sort(key=lambda oseba: oseba['id'])
#     vloge.sort(key=lambda vloga: (vloga['film'], vloga['vloga'], vloga['mesto']))
#     zanri.sort(key=lambda zanr: (zanr['film'], zanr['zanr']))

#     return osebe, vloge, zanri


avtomobili = []
for st_strani in range(1, 7):
    for avto in avti_na_strani(st_strani):
        avtomobili.append(avto)
orodja.zapisi_json(avtomobili, 'obdelani-podatki/avtomobili.json')
orodja.zapisi_csv(
    avtomobili, 
    ['ime', 'leto_prve_registracije', 'prevoženi_kilometri', 'vrsta_goriva', 'vrsta_menjalnika', 'vrsta_motorja', 'cena'],
    'obdelani_podatki/avtomobili.csv')




# filmi = []
# for st_strani in range(1, 41):
#     for film in filmi_na_strani(st_strani, 250):
#         filmi.append(film)
# filmi.sort(key=lambda film: film['id'])
# orodja.zapisi_json(filmi, 'obdelani-podatki/filmi.json')
# osebe, vloge, zanri = izloci_gnezdene_podatke(filmi)
# orodja.zapisi_csv(
#     filmi,
#     ['id', 'naslov', 'dolzina', 'leto', 'ocena', 'metascore', 'glasovi', 'zasluzek', 'oznaka', 'opis'], 'obdelani-podatki/filmi.csv'
# )
# orodja.zapisi_csv(osebe, ['id', 'ime'], 'obdelani-podatki/osebe.csv')
# orodja.zapisi_csv(vloge, ['film', 'oseba', 'vloga', 'mesto'], 'obdelani-podatki/vloge.csv')
# orodja.zapisi_csv(zanri, ['film', 'zanr'], 'obdelani-podatki/zanri.csv')
