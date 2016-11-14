import json
import requests
import ast
import datetime
import dateutil.parser


filepath = '/Users/mohamedkane/Desktop/token.txt'
token_file= open(filepath)
token=str(token_file.read())
def step1():
    payload = {'github':'https://github.com/mhkane/api-challenge','token':token}
    url = 'http://challenge.code2040.org/api/register'
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print r.text
#step1()
def step2():
    payload = {'token':token}
    url = 'http://challenge.code2040.org/api/reverse'
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    rev_s= reverse(r.text)
    url2= 'http://challenge.code2040.org/api/reverse/validate'
    payload2 =  {'token':token,'string':rev_s}    
    r2 = requests.post(url2, data=json.dumps(payload2), headers=headers)
    print r2.text

def reverse(string):
    return string[::-1]
#step2()

def step3():
    payload = {'token':token}
    url = 'http://challenge.code2040.org/api/haystack'
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    dic2= ast.literal_eval(r.text)
    needle = dic2['needle']
    haystack = dic2['haystack']
    try:
        index = haystack.index(needle)
    except:
        index = None
    if index:
        payload= {'token':token,'needle':index}
        url = 'http://challenge.code2040.org/api/haystack/validate'
        headers = {'content-type': 'application/json'}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        print r.text
#step3()

def step4():
    payload = {'token':token}
    url = 'http://challenge.code2040.org/api/prefix'
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    dic2= ast.literal_eval(r.text)
    prefix = dic2['prefix']
    array = dic2['array']
    print prefix
    print array
    try:
        final = list(filter(lambda x: x[:len(prefix)]!=prefix,array))
        print final
    except:
        final = None
    if final:
        payload2= {'token':token,'array':final}
        url2 = 'http://challenge.code2040.org/api/prefix/validate'
        headers = {'content-type': 'application/json'}
        r2 = requests.post(url2, data=json.dumps(payload2), headers=headers)
        print r2.text
#step4()

def step5():
    payload = {'token':token}
    url = 'http://challenge.code2040.org/api/dating'
    headers = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    dic2= ast.literal_eval(r.text)
    date = dic2['datestamp']
    interval = dic2['interval']
    date_python = dateutil.parser.parse(date)
    print date
    print date_python
    print interval
    b = date_python + datetime.timedelta(seconds=int(interval))
    c= b.isoformat('T')[:19]+'Z'
    print c
    payload2= {'token':token,'datestamp':c}
    url2 = 'http://challenge.code2040.org/api/dating/validate'
    headers = {'content-type': 'application/json'}
    r2 = requests.post(url2, data=json.dumps(payload2), headers=headers)
    print r2.text
#step5()
    
    