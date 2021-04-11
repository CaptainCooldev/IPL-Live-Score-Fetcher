import requests as r
import time

def display():
    try:
        resp = r.get('http://mapps.cricbuzz.com/cbzios/match/livematches')
        data = resp.json()
        print("------Live ipl score----\n")
        print('{} VS {}\n'.format(data['matches'][0]['team1']['name'],data['matches'][0]['team2']['name']))
        print(data['matches'][0]['header']['toss']+"\n")
        print('batsman on strike : {}\n'.format(data['matches'][0]['batsman'][0]['name']))
        print('{}/{} for {} overs\n'.format(data['matches'][0]['bat_team']['innings'][0]['score'],data['matches'][0]['bat_team']['innings'][0]['wkts'],data['matches'][0]['bat_team']['innings'][0]['overs']))
        print('{}* -- ||r:{}||b:{}||4s:{}||6s:{}\n'.format(data['matches'][0]['batsman'][0]['name'],data['matches'][0]['batsman'][0]['r'],data['matches'][0]['batsman'][0]['b'],data['matches'][0]['batsman'][0]['4s'],data['matches'][0]['batsman'][0]['6s']))
        print('{} -- ||r:{}||b:{}||4s:{}||6s:{}\n'.format(data['matches'][0]['batsman'][1]['name'],data['matches'][0]['batsman'][1]['r'],data['matches'][0]['batsman'][1]['b'],data['matches'][0]['batsman'][1]['4s'],data['matches'][0]['batsman'][1]['6s']))
        print('bowler : {}\n'.format(data['matches'][0]['bowler'][0]['name']))
    except Exception as e:
        print("no data yet" + e)    

while True:
    display()
    asyncio.sleep(10)
