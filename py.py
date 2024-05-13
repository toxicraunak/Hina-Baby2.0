from rich.panel import Panel as cm
from rich import print as CM 
import webbrowser
import time

texts = ['               Telegram Channel :- Haxkx', '                Tool Status :- Paid', '              Script Type :- SafeUm Account Maker', '              Script Expire Time :- Unlimted', '              Script Owner Telegram Id :- @Toxic_Tanji ', '             Script Price :- Free For Now']
colors = ['red', 'yellow', 'blue', 'green', 'purple', 'cyan']

formatted_texts = [cm(text, style=f"bold {color}") for text, color in zip(texts, colors)]

for formatted_text in formatted_texts:
    CM(formatted_text)
    
def to(s):
    for char in s + "\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(500.0 / 8000)
        
webbrowser.open("https://t.me/haxkx")

import os
from os import system, name
from ssl import CERT_NONE
from gzip import decompress
from random import choice, choices
from concurrent.futures import ThreadPoolExecutor
from json import dumps

try:
    from websocket import create_connection
except:
    system('pip install websocket-client')
    from websocket import create_connection

failed = 0
success = 0
retry = 0
accounts = []


def work():
    global failed, success, retry
    username = choice('qwertyuiooasdfghjklzxcvpbnm1234567890') + ''.join(choices(list('qwertyuioasdfghjklzxcvbnpm1234567890'), k=16))
    try:
        con = create_connection("wss://195.13.182.213/Auth",
                                header={"app": "com.safeum.android", "host": None, "remoteIp": "195.13.182.213",
                                        "remotePort": str(8080), "sessionId": "b6cbb22d-06ca-41ff-8fda-c0ddeb148195",
                                        "time": "2024-04-11 11:00:00", "url": "wss://51.79.208.190/Auth"},
                                sslopt={"cert_reqs": CERT_NONE})
        con.send(dumps(
         {"action":"Register","subaction":"Desktop","locale":"en_IN","gmt":"+05","password":{"m1x":"0b823f3cb3d1c1c1981efc4605e108f9efaf8f051341c13b3365984ea9a30511","m1y":"f14c6f0d58eadf4b1f8aa5b66c99f53a5840bcf8080b8b2a2544aaf09dc2a1c0","m2":"148558c6f2fca435b0fea3b9c2f5242e2bcba5de4425c7dd9875f814a057c196","iv":"3e5249ae66c9405b7c4827bd982851d3","message":"d8ba0e8a44c872ab8d75caa5fbc2a68b19638f13991747048ab70270ea3dc8f126bb27c6fd011901d1583668511f628da97e3f95d35f0a5807fdb8180fb6a20258f8d576b0ccf3ac09c6e0fa7e57e0b7"},"magicword":{"m1x":"8a7a68bef400057faea06bb03a88d4a5cfbf04df9ba2b2571262ceb56ec1dde9","m1y":"8b815d8b16d2a28d8e303b82e8a4a38328d0306a0f3c89067d1974e038d8b72e","m2":"57423dfcc94eacd439260b898d395a195316f2547683a3d35ac3b003d81e0469","iv":"8dd9bac39532a4a09733e6f830db8e3c","message":"369144bc00cb9e7822cf54c6d3a66554"},"magicwordhint":"0000","login":str(username),"devicename":"Xiaomi 220733SPH","softwareversion":"1.1.0.1640","nickname":"ggjh678nn","os":"AND","deviceuid":"b0c55c7c17fddd4b","devicepushuid":"*cYwQmtN0GC4:APA91bGdy73ku9qhNJi8Inhe01e2pXa_dp-CiVULHhPMkcqgi4JFOTCMS-jHhJzxhoO5ZdmGhjFgy-qxGQFSB86l0A1iQGM9RSl3c6X33zPAqxkRQ6C1qm2Gfx94e72joG2twLFbh61E","osversion":"and_12.0.0","id":"696727312"}))
        gzip = decompress(con.recv()).decode('utf-8')
        if '"status":"Success"' in gzip:
            success += 1
            b = accounts.append(username + ':sina')
            print(b)
            with open('SafeUM_HAXKX.txt', 'a') as f:
                f.write(username + ":sina | TG : @Haxkx\n")

        else:
            failed += 1
    except:
        retry += 1


start = ThreadPoolExecutor(max_workers=1000)

while True:
    start.submit(work)
    print('\n\n\n' + ' ' * 25 + 'Success : ' + str(success) + '\n\n\n' + ' ' * 25 + 'Failed : ' + str(
        failed) + '\n\n\n' + ' ' * 25 + 'ReTry : ' + str(retry))
    hh = str(failed) + str(success) + str(retry)
    if int(success) >= 1000:
        
        print("Created Accounts Successfully Sent To Owner Group")
        
    
    if int(success) > int(0):
        z = "\n".join(accounts)
        
        print("ACCOUNTS GENERATED>>\n", z)
        

    os.system('clear')
