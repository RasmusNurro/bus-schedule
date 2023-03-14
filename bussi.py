import json
import requests
from datetime import datetime

pysakkinimi = requests.get("http://data.foli.fi/siri/sm/pretty")

while True:

    i=0

    pysakki = input("Anna pysäkin numero :")
    lataus = json.loads(pysakkinimi.text)
    lataus = pysakkinimi.json()
    eristys = lataus[pysakki]['stop_name']
    print(eristys)


    req_api = requests.get("https://data.foli.fi/siri/stops/" + pysakki)
    lataus1 = json.loads(req_api.text)
    lataus1 = req_api.json()
    lutu = lataus1['result']
    for lukku in lutu:
        if i < 10:
            aikataulut = lataus1['result'][i]['aimedarrivaltime']
            bussinmro = lataus1['result'][i]['lineref']
            paatymispaikka = lataus1['result'][i]['destinationdisplay']
            laskua = lataus1['result'][i]['expectedarrivaltime']
            aikaB = (datetime.fromtimestamp(laskua))
            aika = (datetime.fromtimestamp(aikataulut))
            laskuB = (aikaB-aika)            
            print(aika.strftime('%H:%M'), laskuB,"     ", bussinmro, paatymispaikka)
            i+=1