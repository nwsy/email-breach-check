import requests
import os

url = 'https://identityprotection.avast.com/v1/web/query/site-breaches/unauthorized-data'
head = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9,ar-AE;q=0.8,ar;q=0.7',
    'Connection': 'keep-alive',
    'Content-Length': '43',
    'Content-Type': 'application/json;charset=UTF-8',
    'Host': 'identityprotection.avast.com',
    'Origin': 'https://www.avast.com',
    'Referer': 'https://www.avast.com/',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36',
    'Vaar-Header-App-Build-Version': '1.0.0',
    'Vaar-Header-App-Product': 'hackcheck-web-avast',
    'Vaar-Header-App-Product-Name': 'hackcheck-web-avast',
    'Vaar-Version': '0'
}
def face():
    input('press enter to continue;')
    os.system('cls')
    print('''
+-------------------------------------------------------------+
+                                                             +
+                < Email breaches check  >                    +
+                  by: greedalbadi                            +
+                                                             +
+-------------------------------------------------------------+
    ''')
    email = input('\nemail: ')
    data = {
        'emailAddresses': [
            email
        ]
    }
    check(email, data)
def check(email, data):
    try:
        r = requests.post(url, json=data, headers=head)
        if '{"breaches":{},"data":{},"summary":' in r.text:
            print(f'[{email}] secured mail')
        elif 'recordsCount' in r.text:
            try:
                print(f'BREACHED EMAIL [{email}] RECORD COUNT [' + r.text.split('"recordsCount":')[1].split(',')[0] + ']')
                face()
            except:
                print(f'BREACHED EMAIL [{email}]')
                face()
            try:
                print('About the breach:')
                print(r.text.split('"description":"')[1].split('","publishDate":')[0])
            except:
                ''
                face()
        else:
            print('please wait, and try again later')
            face()
    except:
        print('error')
        face()
face()
