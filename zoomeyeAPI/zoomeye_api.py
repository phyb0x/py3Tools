#!/usr/bin/env python
# coding: utf-8
#Authon:phyb0x
#zoomeyeapi

import requests
import json

access_token = ''
query = ''
page = ''
ip_list = []
user = input('[-]username :')
passwd =input('[-]password :')

def login():
    data = {
        'username' : user,
        'password' : passwd
    }
    data_encoded = json.dumps(data)  
    r = requests.post(url = 'https://api.zoomeye.org/user/login',data = data_encoded)
    r_decoded = json.loads(r.text) 
    access_token = r_decoded['access_token']
    return access_token

def saveip(file,list):
    s = '\n'.join(list)
    with open(file,'w') as output:
        output.write(s)

def main():
    query = input('[+]query:')
    page = 1
    while(True):
        try: 
            headers = { 'Authorization' : 'JWT ' + login()}
            r = requests.get(url = 'https://api.zoomeye.org/host/search?query='+str(query)+'&facet=app,os&page=' + str(page),headers = headers)
            datas = json.loads(r.text)['matches']
            for data in datas:
                print(data['ip'])
                ip_list.append(data['ip'])

        except Exception as e:
            if str(e.message) == 'matches':
                print('account was break')
                break
        else:
            if page == 10:
                break
            page += 1   
    saveip('ip_list.txt',ip_list)


if __name__ == '__main__':
    main()